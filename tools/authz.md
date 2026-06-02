# 🧾 Remote Authorization API (authz)

**Protocols**: [MS-RAA](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-raa/).

## Subcommands / Usage

### Syntax

```bash
authz [auth_flags] [--object-uuid <uuid>] <subcommand>
```

### Show version

```bash
./authz [auth_flags] version
```

### Inspect token/context info classes for a SID or account

Classes: all, user, groups, restricted, device-groups, user-claims, device-claims  


```bash
./authz [auth_flags] info 'joao_couves' --class all
```

### Syntax

```bash
authz check <source> <SID|NAME> -T <target> [common flags]
```


Common check flags:  
--desired-access <mask>      default 0x02000000 (MAXIMUM_ALLOWED)  
--principal-self <sid|name>  PrincipalSelf substitution SID/name  
--device <sid|name>          optional device identity for compound AccessCheck  
-O, --object-types <list>    comma-separated [level:]guid entries  
-P, --privileges             request privilege computation  
--print-sd <no|dacl|sacl|all>  

### Inline SD (hex or SDDL)

```bash
./authz [auth_flags] check sd 'CRETA\joao_couves' -T 'O:SYG:SYD:(A;;GA;;;BA)'
```

### LDAP object SD

```bash
./authz [auth_flags] check ldap 'CRETA\joao_couves' -T 'CN=Administrator,CN=Users,DC=creta,DC=local'
```

### Service SD

```bash
./authz [auth_flags] check services 'CRETA\joao_couves' -T Spooler
```

### Task SD

```bash
./authz [auth_flags] check tasks 'CRETA\joao_couves' -T '\Microsoft\Windows\Defrag\ScheduledDefrag'
```

### Registry key SD

```bash
./authz [auth_flags] check registry 'CRETA\joao_couves' -T 'HKLM\SOFTWARE'
```

### SMB share/file SD

```bash
./authz [auth_flags] check smb 'CRETA\joao_couves' -T 'C$\Windows'
```

### WMI namespace SD

```bash
./authz [auth_flags] check wmi-ns 'CRETA\joao_couves' -T 'root\CIMV2'
```

### AccessCheck using a compound user+device context

```bash
./authz [auth_flags] check ldap 'CRETA\joao_couves' -T 'CN=Administrator,CN=Users,DC=creta,DC=local'  \
	--device 'CRETA\WIN-6BKCP1FPPCI$'
```

### ObjectTypeList examples:

first entry defaults to level 0, subsequent entries default to level 1  


```bash
./authz [auth_flags] check ldap 'CRETA\joao_couves' -T 'CN=Administrator,CN=Users,DC=creta,DC=local'  \
	-O '00299570-246d-11d0-a768-00aa006e0529,bf967aba-0de6-11d0-a285-00aa003049e2'
```

### explicit levels

```bash
./authz [auth_flags] check ldap 'CRETA\joao_couves' -T 'CN=Administrator,CN=Users,DC=creta,DC=local'  \
	-O '0:00299570-246d-11d0-a768-00aa006e0529,1:bf967aba-0de6-11d0-a285-00aa003049e2'
```
