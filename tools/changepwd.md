# 🔄 Password Change (changepwd)

**Protocols**: [MS-SAMR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SAMR/%5bMS-SAMR%5d.pdf), [RFC 3244](https://datatracker.ietf.org/doc/html/rfc3244) (kpasswd), [LDAP](https://datatracker.ietf.org/doc/html/rfc4511), [MS-ADCAP](https://winprotocoldoc.z19.web.core.windows.net/MS-ADCAP/%5bMS-ADCAP%5d.pdf).

Password changes in Active Directory can be performed through multiple protocols. This tool supports SAMR (over SMB or direct TCP), LDAP/LDAPS (using a password modify extended operation), [MS-ADCAP](https://winprotocoldoc.z19.web.core.windows.net/MS-ADCAP/%5bMS-ADCAP%5d.pdf) (Active Directory Web Services Custom Action Protocol), and Kerberos kpasswd. Depending on the context, some methods require knowing the old password while others can force-set a new one without it.

## Usage

### samr

**Syntax:**
```bash
./changepwd [auth_flags] samr -a <account> -w <new-password> [-o <old-password>] [--transport <smb|tcp>]
```

**Change a password via MS-SAMR over SMB named pipe:**

```bash
./changepwd [auth_flags] samr -a sampleuser -w 'NewP@ssw0rd!' --transport smb
```

**Change a password via MS-SAMR over TCP:**

```bash
./changepwd [auth_flags] samr -a sampleuser -w 'NewP@ssw0rd!' --transport tcp
```

### kpasswd

**Syntax:**
```bash
./changepwd [auth_flags] kpasswd -a <account> -w <new-password> [-o <old-password>]
```

{% hint style="info" %}
For this command, `--dc` is only considered to override the DC for PKINIT when authenticating with a client certificate. In that case, if `--dc` is not specified, the target (`-t`) will be used for both PKINIT and the operation itself.
{% endhint %}

**Change a password using the Kerberos kpasswd protocol (self-change):**

```bash
./changepwd [auth_flags] kpasswd -a sampleuser -w 'NewP@ssw0rd!' -o 'OldP@ssw0rd!'
```

**Perform an admin password reset via kpasswd:**

```bash
./changepwd [auth_flags] kpasswd -a sampleuser -w 'NewP@ssw0rd!'
```

### ldap

**Syntax:**
```bash
./changepwd [auth_flags] ldap -a <account> -w <new-password> [--scheme <ldap|ldaps>] [--starttls]
```

**Change a password via LDAPS:**

```bash
./changepwd [auth_flags] ldap -a sampleuser -w 'NewP@ssw0rd!' --scheme ldaps
```

### adws

**Syntax:**
```bash
./changepwd [auth_flags] adws -a <account> -w <new-password>
```

**Change a password via ADWS (Active Directory Web Services):**

```bash
./changepwd [auth_flags] adws -a sampleuser -w 'NewP@ssw0rd!'
```
