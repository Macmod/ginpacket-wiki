# 🧾 Remote Authorization API (authz)



The Remote Authorization API (MS-RAA) lets you query a Windows host's authorization engine to determine what access rights a given user or security principal would have against a specific resource - without actually performing the access. Useful for auditing and validating ACLs on LDAP objects, files, services, registry keys, WMI namespaces, and more.

## Usage

### General Usage

**Syntax:**
```bash
./authz [auth_flags] [--object-uuid <uuid>] <subcommand>
```

**Show version:**

```bash
./authz [auth_flags] version
```

**Inspect token/context info classes for a SID or account Classes: all, user, groups, restricted, device-groups, user-claims, device-claims:**

```bash
./authz [auth_flags] info 'joao_couves' --class all
```

### check

**Syntax:**
```bash
./authz check <source> <SID|NAME> -T <target> [common flags]
```


Common check flags:  
--desired-access <mask>      default 0x02000000 (MAXIMUM_ALLOWED)  
--principal-self <sid|name>  PrincipalSelf substitution SID/name  
--device <sid|name>          optional device identity for compound AccessCheck  
-O, --object-types <list>    comma-separated [level:]guid entries  
-P, --privileges             request privilege computation  
--print-sd <no|dacl|sacl|all>  

**Inline SD (hex or SDDL):**

```bash
./authz [auth_flags] check sd 'DOMAIN\sampleuser' -T 'O:SYG:SYD:(A;;GA;;;BA)'
```

**LDAP object SD:**

```bash
./authz [auth_flags] check ldap 'DOMAIN\sampleuser' -T 'CN=Administrator,CN=Users,DC=domain,DC=local'
```

**Service SD:**

```bash
./authz [auth_flags] check services 'DOMAIN\sampleuser' -T Spooler
```

**Task SD:**

```bash
./authz [auth_flags] check tasks 'DOMAIN\sampleuser' -T '\Microsoft\Windows\Defrag\ScheduledDefrag'
```

**Registry key SD:**

```bash
./authz [auth_flags] check registry 'DOMAIN\sampleuser' -T 'HKLM\SOFTWARE'
```

**SMB share/file SD:**

```bash
./authz [auth_flags] check smb 'DOMAIN\sampleuser' -T 'C$\Windows'
```

**WMI namespace SD:**

```bash
./authz [auth_flags] check wmi-ns 'DOMAIN\sampleuser' -T 'root\CIMV2'
```

**AccessCheck using a compound user+device context:**

```bash
./authz [auth_flags] check ldap 'DOMAIN\sampleuser' -T 'CN=Administrator,CN=Users,DC=domain,DC=local'  \
	--device 'DOMAIN\WIN-SAMPLEPC$'
```

**ObjectTypeList examples: first entry defaults to level 0, subsequent entries default to level 1:**

```bash
./authz [auth_flags] check ldap 'DOMAIN\sampleuser' -T 'CN=Administrator,CN=Users,DC=domain,DC=local'  \
	-O '00299570-246d-11d0-a768-00aa006e0529,bf967aba-0de6-11d0-a285-00aa003049e2'
```

**explicit levels:**

```bash
./authz [auth_flags] check ldap 'DOMAIN\sampleuser' -T 'CN=Administrator,CN=Users,DC=domain,DC=local'  \
	-O '0:00299570-246d-11d0-a768-00aa006e0529,1:bf967aba-0de6-11d0-a285-00aa003049e2'
```

## Notes
**Protocols**

* [MS-RAA](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-raa/) for the access check itself.
* [RFC 4511](https://datatracker.ietf.org/doc/html/rfc4511) / [MS-ADTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-ADTS/%5bMS-ADTS%5d.pdf) to fetch SDs from LDAP objects (`check ldap`).
* [MS-SMB2](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SMB2/%5bMS-SMB2%5d.pdf) to fetch SDs from shares and file paths (`check smb`).
* [MS-RRP](https://winprotocoldoc.z19.web.core.windows.net/MS-RRP/%5bMS-RRP%5d.pdf) to fetch SDs from registry keys (`check registry`).
* [MS-SCMR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SCMR/%5bMS-SCMR%5d.pdf) to fetch SDs from services (`check services`).
* [MS-TSCH](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-TSCH/%5bMS-TSCH%5d.pdf) to fetch SDs from scheduled tasks (`check tasks`).
* [MS-WMI](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-WMI/%5bMS-WMI%5d.pdf) / [MS-DCOM](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DCOM/%5bMS-DCOM%5d.pdf) to fetch SDs from WMI namespaces (`check wmi-ns`).