# 📇 LDAP (ldap)

**Protocols**: [RFC 4511](https://datatracker.ietf.org/doc/html/rfc4511) / [MS-ADTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-ADTS/%5bMS-ADTS%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
ldap [auth_flags] whoami
```

### Print the authenticated LDAP user identity

```bash
./ldap [auth_flags] whoami
```

### Syntax

```bash
ldap [auth_flags] info <dn-or-name> [--all]
```

### Dump attributes for an object by DN, sAMAccountName, UPN, or GUID

```bash
./ldap [auth_flags] info 'Administrator'
```

### Show all attributes including non-default ones

```bash
./ldap [auth_flags] info 'CN=Domain Users,CN=Users,DC=example,DC=com' --all
```

### Syntax

```bash
ldap [auth_flags] query users [--enabled] [--disabled]
```

### List all user objects in the domain

```bash
./ldap [auth_flags] query users
```

### List only enabled user accounts

```bash
./ldap [auth_flags] query users --enabled
```

### List only disabled user accounts

```bash
./ldap [auth_flags] query users --disabled
```

### Syntax

```bash
ldap [auth_flags] query groups
```

### List all group objects in the domain

```bash
./ldap [auth_flags] query groups
```

### Syntax

```bash
ldap [auth_flags] query computers
```

### List all computer accounts in the domain

```bash
./ldap [auth_flags] query computers
```

### Syntax

```bash
ldap [auth_flags] query containers
```

### List all container objects in the domain

```bash
./ldap [auth_flags] query containers
```

### Syntax

```bash
ldap [auth_flags] query ous
```

### List all organizational units in the domain

```bash
./ldap [auth_flags] query ous
```

### Syntax

```bash
ldap [auth_flags] query service-accounts
```

### List accounts with service principal names (service accounts)

```bash
./ldap [auth_flags] query service-accounts
```

### Syntax

```bash
ldap [auth_flags] query gpos
```

### List all group policy objects in the domain

```bash
./ldap [auth_flags] query gpos
```

### Syntax

```bash
ldap [auth_flags] query spns
```

### List all accounts with service principal names set

```bash
./ldap [auth_flags] query spns
```

### Syntax

```bash
ldap [auth_flags] query unconstrained-delegation
```

### List computers and users with unconstrained Kerberos delegation

```bash
./ldap [auth_flags] query unconstrained-delegation
```

### Syntax

```bash
ldap [auth_flags] query constrained-delegation
```

### List accounts configured with constrained Kerberos delegation

```bash
./ldap [auth_flags] query constrained-delegation
```

### Syntax

```bash
ldap [auth_flags] query asreproast
```

### List accounts that have Kerberos pre-authentication disabled

```bash
./ldap [auth_flags] query asreproast
```

### Syntax

```bash
ldap [auth_flags] query never-expires
```

### List accounts whose password is set to never expire

```bash
./ldap [auth_flags] query never-expires
```

### Syntax

```bash
ldap [auth_flags] query password-not-required
```

### List accounts that do not require a password

```bash
./ldap [auth_flags] query password-not-required
```

### Syntax

```bash
ldap [auth_flags] query cert-templates
```

### List certificate templates published in the domain

```bash
./ldap [auth_flags] query cert-templates
```

### Syntax

```bash
ldap [auth_flags] query cert-authorities
```

### List enterprise certification authorities in the domain

```bash
./ldap [auth_flags] query cert-authorities
```

### Syntax

```bash
ldap [auth_flags] query trusts [--transitive]
```


List domain trust relationships rendered as an ASCII tree with direction arrows and trust attribute flags
← inbound (they trust us), → outbound (we trust them), ↔ bidirectional


```bash
./ldap [auth_flags] query trusts
```

### Syntax

```bash
ldap [auth_flags] query passpol
```

### Show the domain password policy and any fine-grained PSOs

```bash
./ldap [auth_flags] query passpol
```

### Syntax

```bash
ldap [auth_flags] query mquota
```

### Show the ms-DS-MachineAccountQuota value from the domain object

```bash
./ldap [auth_flags] query mquota
```

### Syntax

```bash
ldap [auth_flags] query shadow-creds [--limit <n>]
```


List objects with msDS-KeyCredentialLink set; parse DeviceID, key type, and creation time


```bash
./ldap [auth_flags] query shadow-creds
```

### Syntax

```bash
ldap [auth_flags] query rbcd [--limit <n>]
```


List computers with msDS-AllowedToActOnBehalfOfOtherIdentity set; decode the SD DACL


```bash
./ldap [auth_flags] query rbcd
```

### Syntax

```bash
ldap [auth_flags] query gmsa [--limit <n>]
```


List Group Managed Service Accounts; show password rotation interval and who can read the password (msDS-GroupMSAMembership DACL)


```bash
./ldap [auth_flags] query gmsa
```

### Syntax

```bash
ldap [auth_flags] query laps [--limit <n>]
```


List computers that have a LAPS password set (v1: ms-Mcs-AdmPwd, v2: msLAPS-Password); show expiry timestamps


```bash
./ldap [auth_flags] query laps
```

### Syntax

```bash
ldap [auth_flags] query sccm [--limit <n>]
```


Detect SCCM/MECM management points registered in AD (objectClass=mSSMSManagementPoint)


```bash
./ldap [auth_flags] query sccm
```

### Syntax

```bash
ldap [auth_flags] query wds [--limit <n>]
```

### Detect Windows Deployment Services servers via WDSMC SPN on computer objects

```bash
./ldap [auth_flags] query wds
```

### Syntax

```bash
ldap [auth_flags] get-gmsa-password <sAMAccountName>
```


Read and decode the msDS-ManagedPassword blob for a GMSA (requires group membership listed in msDS-GroupMSAMembership)


```bash
./ldap [auth_flags] get-gmsa-password 'svc_backup$'
```

### Syntax

```bash
ldap [auth_flags] get-laps <computer>
```


Read the LAPS administrator password for a computer (v1 plaintext or v2 JSON blob); requires LAPS read rights


```bash
./ldap [auth_flags] get-laps WIN-DC01
```

```bash
./ldap [auth_flags] get-laps WIN-DC01.corp.local
```

### Syntax

```bash
ldap [auth_flags] enable <dn>
```

### Enable an AD account by clearing the ACCOUNTDISABLE userAccountControl bit

```bash
./ldap [auth_flags] enable 'CN=jdoe,CN=Users,DC=example,DC=com'
```

### Syntax

```bash
ldap [auth_flags] disable <dn>
```

### Disable an AD account by setting the ACCOUNTDISABLE userAccountControl bit

```bash
./ldap [auth_flags] disable 'CN=jdoe,CN=Users,DC=example,DC=com'
```

### Syntax

```bash
ldap [auth_flags] uac-modify <dn> <flag> <set|clear>
```

### Toggle a single userAccountControl bit by name (or numeric value)

```bash
./ldap [auth_flags] uac-modify 'CN=jdoe,CN=Users,DC=example,DC=com' DONT_REQUIRE_PREAUTH set
```

```bash
./ldap [auth_flags] uac-modify 'CN=jdoe,CN=Users,DC=example,DC=com' DONT_EXPIRE_PASSWORD set
```

```bash
./ldap [auth_flags] uac-modify 'CN=jdoe,CN=Users,DC=example,DC=com' TRUSTED_FOR_DELEGATION clear
```

### Syntax

```bash
ldap [auth_flags] search -F <filter> [-A <attrs>] [--limit <n>] [--base-dn <dn>] [--scope <scope>]
```

### Run a raw LDAP search with a custom filter and attribute projection

```bash
./ldap [auth_flags] search -F '(objectClass=user)' -A cn,mail,userAccountControl
```

### Search with a wildcard filter

```bash
./ldap [auth_flags] search -F '(cn=admin*)' -A cn,mail
```

### Filter group members with a result limit

```bash
./ldap [auth_flags] search -F '(memberof=CN=Domain Admins,CN=Groups,DC=example,DC=com)' --limit 100
```

### Search for accounts with SPNs

```bash
./ldap [auth_flags] search -F '(servicePrincipalName=*)' --limit 50
```

### Use a bitfield OID filter for password policy attributes

```bash
./ldap [auth_flags] search -F '(userAccountControl:1.2.840.113556.1.4.803:=524288)'
```

### Syntax

```bash
ldap [auth_flags] <subcommand> -f <filter-chain> -a <attr-chain> -b <base-chain>
```

### Apply ldapx obfuscation chains to a raw search

```bash
./ldap [auth_flags] search -F '(objectClass=user)' -A cn,sAMAccountName -f OGDR -a Owp -b OX
```

### Apply obfuscation chains to a predefined query

```bash
./ldap [auth_flags] query users -f OGDR -a Owp -b OX
```

### Apply obfuscation chains to an info lookup

```bash
./ldap [auth_flags] info 'Administrator' -f OGDR -b OX
```

### Syntax

```bash
ldap [auth_flags] modify <dn> --attr <name> --operation <add|replace|delete> --value <value>
```

### Replace an attribute value on an LDAP object (requires write access)

```bash
./ldap [auth_flags] modify 'CN=User,CN=Users,DC=example,DC=com' --attr description --operation replace --value 'Updated description'
```

### Add a member to a group

```bash
./ldap [auth_flags] modify 'CN=Group,CN=Users,DC=example,DC=com' --attr member --operation add --value 'CN=User,CN=Users,DC=example,DC=com'
```

### Syntax

```bash
ldap [auth_flags] --scheme ldaps|ldap [--starttls] <subcommand>
```

### Connect over LDAPS (TLS)

```bash
./ldap [auth_flags] --scheme ldaps query users
```

### Connect using StartTLS upgrade on plain LDAP

```bash
./ldap [auth_flags] --scheme ldap --starttls query users
```

### Syntax

```bash
ldap [auth_flags] create user --name <cn> [--pass <password>] [--enabled] [--parent-dn <dn>] [--scheme ldaps]
```


Create a new user account (created disabled if --pass is omitted; set password requires LDAPS/StartTLS)


```bash
./ldap [auth_flags] create user --name jdoe --scheme ldaps
```

```bash
./ldap [auth_flags] create user --name jdoe --pass 'P@ssw0rd!' --scheme ldaps
```

```bash
./ldap [auth_flags] create user --name jdoe --pass 'P@ssw0rd!' --enabled=false --scheme ldaps
```

### Create user in a custom OU

```bash
./ldap [auth_flags] create user --name svc_backup --parent-dn 'OU=ServiceAccounts,DC=example,DC=com' --scheme ldaps
```

### Syntax

```bash
ldap [auth_flags] create computer --name <cn> [--pass <password>] [--parent-dn <dn>] [--scheme ldaps]
```


Create a machine account (requires ms-DS-MachineAccountQuota >= 1 or sufficient privileges)


```bash
./ldap [auth_flags] create computer --name PENTEST$ --scheme ldaps
```

```bash
./ldap [auth_flags] create computer --name PENTEST --pass 'P@ssw0rd!' --scheme ldaps
```

### Syntax

```bash
ldap [auth_flags] create group --name <cn> [--type <group-type>] [--parent-dn <dn>]
```


Create a group (types: GlobalSecurity, GlobalDistribution, DomainLocalSecurity, DomainLocalDistribution, UniversalSecurity, UniversalDistribution)


```bash
./ldap [auth_flags] create group --name 'Pentesters'
```

```bash
./ldap [auth_flags] create group --name 'Pentesters' --type GlobalSecurity
```

```bash
./ldap [auth_flags] create group --name 'Pentesters' --parent-dn 'OU=Groups,DC=example,DC=com'
```

### Syntax

```bash
ldap [auth_flags] create ou --name <name> [--parent-dn <dn>]
```

### Create an Organizational Unit

```bash
./ldap [auth_flags] create ou --name 'RedTeam'
```

```bash
./ldap [auth_flags] create ou --name 'RedTeam' --parent-dn 'DC=example,DC=com'
```

### Syntax

```bash
ldap [auth_flags] create container --name <name> [--parent-dn <dn>]
```

### Create a container object

```bash
./ldap [auth_flags] create container --name 'TestContainer'
```

```bash
./ldap [auth_flags] create container --name 'TestContainer' --parent-dn 'DC=example,DC=com'
```

### Syntax

```bash
ldap [auth_flags] create custom --template <file.yaml>
```


Create an arbitrary AD object from a YAML template (compatible with sopa create custom templates)


```bash
./ldap [auth_flags] create custom --template myobject.yaml
```
