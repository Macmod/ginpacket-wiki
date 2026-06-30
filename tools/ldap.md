# 📇 LDAP (ldap)

**Protocols**: [RFC 4511](https://datatracker.ietf.org/doc/html/rfc4511) / [MS-ADTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-ADTS/%5bMS-ADTS%5d.pdf).

LDAP is the primary protocol for querying and managing objects in Active Directory - users, groups, computers, OUs, GPOs, and more. This tool exposes a broad set of read and write operations, from simple queries to creating objects and modifying attributes, all directly against the AD LDAP interface. It also supports LDAPS and StartTLS for encrypted connections.

## Usage

### General

**Syntax:**
```bash
./ldap [auth_flags] --scheme ldaps|ldap [--starttls] [--adws] <subcommand>
```

**Connect over LDAPS (TLS):**

```bash
./ldap [auth_flags] --scheme ldaps query users
```

**Connect using StartTLS upgrade on plain LDAP:**

```bash
./ldap [auth_flags] --scheme ldap --starttls query users
```

**Use ADWS (Active Directory Web Services, port 9389) instead of LDAP:**

```bash
./ldap [auth_flags] --adws query users
```

{% hint style="info" %}
`--adws` routes queries through the ADWS endpoint (TCP/9389) using NNS/NMF transport. Incompatible with `--scheme ldaps` and `--starttls`. Useful when LDAP (TCP/389) is blocked.
{% endhint %}

### Obfuscation

**Syntax:**
```bash
./ldap [auth_flags] <subcommand> -f <filter-chain> -a <attr-chain> -b <base-chain>
```

**Apply ldapx obfuscation chains to a raw search:**

```bash
./ldap [auth_flags] search -F '(objectClass=user)' -A cn,sAMAccountName -f OGDR -a Owp -b OX
```

**Apply obfuscation chains to a predefined query:**

```bash
./ldap [auth_flags] query users -f OGDR -a Owp -b OX
```

**Apply obfuscation chains to an info lookup:**

```bash
./ldap [auth_flags] info 'Administrator' -f OGDR -b OX
```

### whoami

**Syntax:**
```bash
./ldap [auth_flags] whoami
```

**Print the authenticated LDAP user identity:**

```bash
./ldap [auth_flags] whoami
```

### info

**Syntax:**
```bash
./ldap [auth_flags] info <dn-or-name> [--hex]
```

**Dump attributes for an object by DN, sAMAccountName, UPN, or GUID:**

```bash
./ldap [auth_flags] info 'Administrator'
```

**Print all attribute values as raw hex:**

```bash
./ldap [auth_flags] info 'CN=Domain Users,CN=Users,DC=domain,DC=local' --hex
```


{% hint style="info" %}
All `query` subcommands accept `-A <attrs>`, `--hex`, `--limit <n>`, `--scheme <ldap|ldaps>`, and `--starttls`. Use `-A attr:hex` to print a specific attribute as raw hex; `--hex` prints all attributes as raw hex.
{% endhint %}

### query users

**Syntax:**
```bash
./ldap [auth_flags] query users [--enabled] [--disabled]
```

**List all user objects in the domain:**

```bash
./ldap [auth_flags] query users
```

**Show selected attributes including nTSecurityDescriptor as hex:**

```bash
./ldap [auth_flags] query users -A cn,sAMAccountName,nTSecurityDescriptor:hex
```

**List only enabled user accounts:**

```bash
./ldap [auth_flags] query users --enabled
```

**List only disabled user accounts:**

```bash
./ldap [auth_flags] query users --disabled
```

### query groups

**Syntax:**
```bash
./ldap [auth_flags] query groups
```

**List all group objects in the domain:**

```bash
./ldap [auth_flags] query groups
```

### query computers

**Syntax:**
```bash
./ldap [auth_flags] query computers
```

**List all computer accounts in the domain:**

```bash
./ldap [auth_flags] query computers
```

### query containers

**Syntax:**
```bash
./ldap [auth_flags] query containers
```

**List all container objects in the domain:**

```bash
./ldap [auth_flags] query containers
```

### query ous

**Syntax:**
```bash
./ldap [auth_flags] query ous
```

**List all organizational units in the domain:**

```bash
./ldap [auth_flags] query ous
```

### query service-accounts

**Syntax:**
```bash
./ldap [auth_flags] query service-accounts (alias: svcs)
```

**List accounts with service principal names (service accounts):**

```bash
./ldap [auth_flags] query service-accounts
```

### query gpos

**Syntax:**
```bash
./ldap [auth_flags] query gpos
```

**List all group policy objects in the domain:**

```bash
./ldap [auth_flags] query gpos
```

### query spns

**Syntax:**
```bash
./ldap [auth_flags] query spns
```

**List all accounts with service principal names set:**

```bash
./ldap [auth_flags] query spns
```

### query unconstrained-delegation

**Syntax:**
```bash
./ldap [auth_flags] query unconstrained-delegation (alias: unconst)
```

**List computers and users with unconstrained Kerberos delegation:**

```bash
./ldap [auth_flags] query unconstrained-delegation
```

### query constrained-delegation

**Syntax:**
```bash
./ldap [auth_flags] query constrained-delegation (alias: const)
```

**List accounts configured with constrained Kerberos delegation:**

```bash
./ldap [auth_flags] query constrained-delegation
```

### query asreproast

**Syntax:**
```bash
./ldap [auth_flags] query asreproast
```

**List accounts that have Kerberos pre-authentication disabled:**

```bash
./ldap [auth_flags] query asreproast
```

### query never-expires

**Syntax:**
```bash
./ldap [auth_flags] query never-expires
```

**List accounts whose password is set to never expire:**

```bash
./ldap [auth_flags] query never-expires
```

### query pwd-not-required

**Syntax:**
```bash
./ldap [auth_flags] query pwd-not-required
```

**List accounts that do not require a password:**

```bash
./ldap [auth_flags] query pwd-not-required
```

### query cert-templates

**Syntax:**
```bash
./ldap [auth_flags] query cert-templates
```

**List certificate templates published in the domain:**

```bash
./ldap [auth_flags] query cert-templates
```

### query cert-authorities

**Syntax:**
```bash
./ldap [auth_flags] query cert-authorities
```

**List enterprise certification authorities in the domain:**

```bash
./ldap [auth_flags] query cert-authorities
```

### query trusts

**Syntax:**
```bash
./ldap [auth_flags] query trusts [--transitive]
```

**List domain trusts as an ASCII tree:**

{% hint style="info" %}
← inbound (they trust us), → outbound (we trust them), ↔ bidirectional.
{% endhint %}

```bash
./ldap [auth_flags] query trusts
```

### query passpol

**Syntax:**
```bash
./ldap [auth_flags] query passpol
```

**Show the domain password policy and any fine-grained PSOs:**

```bash
./ldap [auth_flags] query passpol
```

### query mquota

**Syntax:**
```bash
./ldap [auth_flags] query mquota
```

**Show the ms-DS-MachineAccountQuota value from the domain object:**

```bash
./ldap [auth_flags] query mquota
```

### query shadow-creds

**Syntax:**
```bash
./ldap [auth_flags] query shadow-creds [--limit <n>]
```

**List objects with msDS-KeyCredentialLink set:**

```bash
./ldap [auth_flags] query shadow-creds
```

### query key-creds

**Syntax:**
```bash
./ldap [auth_flags] query key-creds [--limit <n>]
```

**List objects with msDS-KeyCredentialLink set; parse DeviceID, key type, and creation time:**

```bash
./ldap [auth_flags] query key-creds
```

### query rbcd

**Syntax:**
```bash
./ldap [auth_flags] query rbcd [--limit <n>]
```

**List computers with msDS-AllowedToActOnBehalfOfOtherIdentity set:**

```bash
./ldap [auth_flags] query rbcd
```

### query gmsa

**Syntax:**
```bash
./ldap [auth_flags] query gmsa [--limit <n>]
```

**List Group Managed Service Accounts:**

```bash
./ldap [auth_flags] query gmsa
```

### query laps

**Syntax:**
```bash
./ldap [auth_flags] query laps [--limit <n>]
```

**List computers with a LAPS password set:**

{% hint style="info" %}
Checks both v1 (ms-Mcs-AdmPwd) and v2 (msLAPS-Password), and shows expiry timestamps.
{% endhint %}

```bash
./ldap [auth_flags] query laps
```

### query sccm

**Syntax:**
```bash
./ldap [auth_flags] query sccm [--limit <n>]
```

**Detect SCCM/MECM management points registered in AD (objectClass=mSSMSManagementPoint):**

```bash
./ldap [auth_flags] query sccm
```

### query wds

**Syntax:**
```bash
./ldap [auth_flags] query wds [--limit <n>]
```

**Detect Windows Deployment Services servers via WDSMC SPN on computer objects:**

```bash
./ldap [auth_flags] query wds
```

### get-gmsa-password

**Syntax:**
```bash
./ldap [auth_flags] get-gmsa-password <sAMAccountName>
```

**Read and decode the msDS-ManagedPassword blob for a GMSA:**

{% hint style="info" %}
Requires membership in the group listed in msDS-GroupMSAMembership.
{% endhint %}

```bash
./ldap [auth_flags] get-gmsa-password 'sampleuser$'
```

### get-laps

**Syntax:**
```bash
./ldap [auth_flags] get-laps <computer>
```

**Read the LAPS administrator password for a computer:**

{% hint style="info" %}
Requires LAPS read rights. Plaintext (v1/v2) is shown directly. Encrypted v2 (`msLAPS-EncryptedPassword`) is printed as base64 and can be decrypted with [`gkdi decrypt-laps --blob <value>`](gkdi.md#decrypt-laps).
{% endhint %}

```bash
./ldap [auth_flags] get-laps WIN-DC01
```

```bash
./ldap [auth_flags] get-laps WIN-DC01.domain.local
```

### enable

**Syntax:**
```bash
./ldap [auth_flags] enable <dn>
```

**Enable an AD account:**

```bash
./ldap [auth_flags] enable 'CN=sampleuser,CN=Users,DC=domain,DC=local'
```

### disable

**Syntax:**
```bash
./ldap [auth_flags] disable <dn>
```

**Disable an AD account:**

```bash
./ldap [auth_flags] disable 'CN=sampleuser,CN=Users,DC=domain,DC=local'
```

### uac-modify

**Syntax:**
```bash
./ldap [auth_flags] uac-modify <dn> <flag> <set|clear>
```

**Toggle a single userAccountControl bit by name (or numeric value):**

```bash
./ldap [auth_flags] uac-modify 'CN=sampleuser,CN=Users,DC=domain,DC=local' DONT_REQUIRE_PREAUTH set
```

```bash
./ldap [auth_flags] uac-modify 'CN=sampleuser,CN=Users,DC=domain,DC=local' DONT_EXPIRE_PASSWORD set
```

```bash
./ldap [auth_flags] uac-modify 'CN=sampleuser,CN=Users,DC=domain,DC=local' TRUSTED_FOR_DELEGATION clear
```

### search

**Syntax:**
```bash
./ldap [auth_flags] search -F <filter> [-A <attrs>] [--hex] [--limit <n>] [--base-dn <dn>] [--scope <scope>]
```

**Run a raw LDAP search with a custom filter and attribute projection:**

```bash
./ldap [auth_flags] search -F '(objectClass=user)' -A cn,mail,userAccountControl
```

**Search with a wildcard filter:**

```bash
./ldap [auth_flags] search -F '(cn=admin*)' -A cn,mail
```

**Filter group members with a result limit:**

```bash
./ldap [auth_flags] search -F '(memberof=CN=Domain Admins,CN=Groups,DC=domain,DC=local)' --limit 100
```

**Search for accounts with SPNs:**

```bash
./ldap [auth_flags] search -F '(servicePrincipalName=*)' --limit 50
```

**Use a bitfield OID filter for password policy attributes:**

```bash
./ldap [auth_flags] search -F '(userAccountControl:1.2.840.113556.1.4.803:=524288)'
```

**Print all attributes as raw hex:**

```bash
./ldap [auth_flags] search -F '(objectClass=user)' --hex -A cn,objectSid
```

**Print a specific attribute as hex using the per-attribute :hex suffix:**

```bash
./ldap [auth_flags] search -F '(objectClass=user)' -A cn,nTSecurityDescriptor:hex
```

### modify

**Syntax:**
```bash
./ldap [auth_flags] modify <dn> --attr <name> --operation <add|replace|delete> --value <value>
```

**Replace an attribute value on an LDAP object:**

```bash
./ldap [auth_flags] modify 'CN=User,CN=Users,DC=domain,DC=local' --attr description --operation replace --value 'Updated description'
```

**Add a member to a group:**

```bash
./ldap [auth_flags] modify 'CN=Group,CN=Users,DC=domain,DC=local' --attr member --operation add --value 'CN=User,CN=Users,DC=domain,DC=local'
```

### create user

**Syntax:**
```bash
./ldap [auth_flags] create user --name <cn> [--pass <password>] [--enabled] [--parent-dn <dn>] [--scheme ldaps]
```

**Create a new user account:**

{% hint style="info" %}
Created disabled if --pass is omitted. Setting a password requires LDAPS or StartTLS.
{% endhint %}

```bash
./ldap [auth_flags] create user --name sampleuser --scheme ldaps
```

```bash
./ldap [auth_flags] create user --name sampleuser --pass 'P@ssw0rd!' --scheme ldaps
```

```bash
./ldap [auth_flags] create user --name sampleuser --pass 'P@ssw0rd!' --enabled=false --scheme ldaps
```

**Create user in a custom OU:**

```bash
./ldap [auth_flags] create user --name sampleuser --parent-dn 'OU=ServiceAccounts,DC=domain,DC=local' --scheme ldaps
```

### create computer

**Syntax:**
```bash
./ldap [auth_flags] create computer --name <cn> [--pass <password>] [--parent-dn <dn>] [--scheme ldaps]
```

**Create a machine account:**

{% hint style="info" %}
Requires ms-DS-MachineAccountQuota >= 1 or sufficient privileges.
{% endhint %}

```bash
./ldap [auth_flags] create computer --name PENTEST$ --scheme ldaps
```

```bash
./ldap [auth_flags] create computer --name PENTEST --pass 'P@ssw0rd!' --scheme ldaps
```

### create group

**Syntax:**
```bash
./ldap [auth_flags] create group --name <cn> [--type <group-type>] [--parent-dn <dn>]
```

**Create a group:**

{% hint style="info" %}
Available types: GlobalSecurity, GlobalDistribution, DomainLocalSecurity, DomainLocalDistribution, UniversalSecurity, UniversalDistribution.
{% endhint %}

```bash
./ldap [auth_flags] create group --name 'Pentesters'
```

```bash
./ldap [auth_flags] create group --name 'Pentesters' --type GlobalSecurity
```

```bash
./ldap [auth_flags] create group --name 'Pentesters' --parent-dn 'OU=Groups,DC=domain,DC=local'
```

### create ou

**Syntax:**
```bash
./ldap [auth_flags] create ou --name <name> [--parent-dn <dn>]
```

**Create an Organizational Unit:**

```bash
./ldap [auth_flags] create ou --name 'RedTeam'
```

```bash
./ldap [auth_flags] create ou --name 'RedTeam' --parent-dn 'DC=domain,DC=local'
```

### create container

**Syntax:**
```bash
./ldap [auth_flags] create container --name <name> [--parent-dn <dn>]
```

**Create a container object:**

```bash
./ldap [auth_flags] create container --name 'TestContainer'
```

```bash
./ldap [auth_flags] create container --name 'TestContainer' --parent-dn 'DC=domain,DC=local'
```

### create custom

**Syntax:**
```bash
./ldap [auth_flags] create custom --template <file.yaml>
```

**Create an arbitrary AD object from a YAML template (compatible with sopa create custom templates):**

```bash
./ldap [auth_flags] create custom --template myobject.yaml
```

### dacl show

**Syntax:**
```bash
./ldap [auth_flags] dacl show <target-dn> [--scheme <ldap|ldaps>] [--starttls]
```

**Display all ACEs in an object's DACL:**

```bash
./ldap [auth_flags] dacl show 'CN=Administrator,CN=Users,DC=domain,DC=local'
```

### dacl add

**Syntax:**
```bash
./ldap [auth_flags] dacl add <target-dn> <grantee> <right> [--scheme <ldap|ldaps>] [--starttls]
```

{% hint style="info" %}
Known named rights: `genericall`, `writedacl`, `writeowner`, `genericwrite`, `allextended`, `forcechangepassword`, `addmember`, `ds-replication-get-changes`, `ds-replication-get-changes-all`, `dcsync`, `certs-enrollment`, `certs-autoenrollment`, `shadow-cred`, `keycredlink-write`.
{% endhint %}

**Grant WriteDACL on an object:**

```bash
./ldap [auth_flags] dacl add 'CN=User,CN=Users,DC=domain,DC=local' svc_account writedacl
```

**Grant GenericAll on an object:**

```bash
./ldap [auth_flags] dacl add 'CN=User,CN=Users,DC=domain,DC=local' svc_account genericall
```

### dacl remove

**Syntax:**
```bash
./ldap [auth_flags] dacl remove <target-dn> <grantee> <right> [--scheme <ldap|ldaps>] [--starttls]
```

**Remove a WriteDACL ACE from an object:**

```bash
./ldap [auth_flags] dacl remove 'CN=User,CN=Users,DC=domain,DC=local' svc_account writedacl
```

### dacl set-dcsync

**Syntax:**
```bash
./ldap [auth_flags] dacl set-dcsync <domain-dn> <grantee> [--scheme <ldap|ldaps>] [--starttls]
```

**Grant DCSync rights (DS-Replication-Get-Changes + DS-Replication-Get-Changes-All):**

```bash
./ldap [auth_flags] dacl set-dcsync 'DC=domain,DC=local' svc_account
```

### dacl del-dcsync

**Syntax:**
```bash
./ldap [auth_flags] dacl del-dcsync <domain-dn> <grantee> [--scheme <ldap|ldaps>] [--starttls]
```

**Revoke DCSync rights:**

```bash
./ldap [auth_flags] dacl del-dcsync 'DC=domain,DC=local' svc_account
```

### dacl set-genericall

**Syntax:**
```bash
./ldap [auth_flags] dacl set-genericall <target-dn> <grantee> [--scheme <ldap|ldaps>] [--starttls]
```

**Grant GenericAll (full control) on an object:**

```bash
./ldap [auth_flags] dacl set-genericall 'CN=User,CN=Users,DC=domain,DC=local' svc_account
```

### set-owner

**Syntax:**
```bash
./ldap [auth_flags] set-owner <target-dn> <new-owner> [--scheme <ldap|ldaps>] [--starttls]
```

{% hint style="info" %}
Requires WriteOwner right on the target object. `<new-owner>` may be a sAMAccountName or a SID string (S-1-...).
{% endhint %}

**Change the owner of an AD object:**

```bash
./ldap [auth_flags] set-owner 'CN=User,CN=Users,DC=domain,DC=local' svc_account
```

### keycred list

**Syntax:**
```bash
./ldap [auth_flags] keycred list <target>
```

**List all Key Credential Links on an object:**

```bash
./ldap [auth_flags] keycred list jsmith
```

```bash
./ldap [auth_flags] keycred list 'CN=jsmith,CN=Users,DC=domain,DC=local'
```

### keycred add

**Syntax:**
```bash
./ldap [auth_flags] keycred add <target> [--out-pfx <file>] [--out-cert <file>] [--subject <cn>] [--device-id <guid>] [--key-size <bits>] [--pfx-password <pass>]
```

**Add a shadow credential (Key Credential Link) to an object:**

{% hint style="info" %}
Generates an RSA key pair and certificate, creates a `KeyCredentialLink` blob, and appends it to `msDS-KeyCredentialLink`. Use the generated PFX with certificate-based Kerberos tools.
{% endhint %}

```bash
./ldap [auth_flags] keycred add jsmith --out-pfx jsmith.pfx
```

```bash
./ldap [auth_flags] keycred add jsmith --out-pfx jsmith.pfx --out-cert jsmith.pem --pfx-password 'secret'
```

### keycred clear

**Syntax:**
```bash
./ldap [auth_flags] keycred clear <target> [--device-id <uuid>]
```

**Remove all key credentials from an object:**

```bash
./ldap [auth_flags] keycred clear jsmith
```

**Remove only a specific key credential by device ID:**

```bash
./ldap [auth_flags] keycred clear jsmith --device-id 'a1b2c3d4-...'
```
