# 💻 Workstation (wksta)

**Protocols**: [MS-WKST](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-WKST/%5bMS-WKST%5d.pdf).

The Workstation Service Remote Protocol (MS-WKST) provides information about a Windows workstation's network configuration and active sessions. It allows querying the domain and machine name, enumerating currently logged-on users, and listing active network connections.

## Usage

### info

**Syntax:**
```bash
./wksta [auth_flags] info [--detail <basic|lan|full|config>]
```

**Query workstation configuration and identity info (default: full):**

```bash
./wksta [auth_flags] info --detail full
```

### loggedon

**Syntax:**
```bash
./wksta [auth_flags] loggedon
```

**List users currently logged on to the workstation interactively:**

```bash
./wksta [auth_flags] loggedon
```

### transports

**Syntax:**
```bash
./wksta [auth_flags] transports
```

**Enumerate network transports bound to the workstation:**

```bash
./wksta [auth_flags] transports
```

### join-info

**Syntax:**
```bash
./wksta [auth_flags] join-info
```

**Query the current domain or workgroup join status:**

```bash
./wksta [auth_flags] join-info
```

### stats

**Syntax:**
```bash
./wksta [auth_flags] stats
```

**Show SMB redirector statistics (bytes transferred, sessions, operations):**

```bash
./wksta [auth_flags] stats
```

### set-info

**Syntax:**
```bash
./wksta [auth_flags] set-info (--keep-conn | --sess-timeout | --dormant-file-limit) <n>
```

**Set the keep-alive connection interval in seconds:**

```bash
./wksta [auth_flags] set-info --keep-conn 30
```

**Set the session timeout in seconds:**

```bash
./wksta [auth_flags] set-info --sess-timeout 45
```

**Set the dormant file handle limit:**

```bash
./wksta [auth_flags] set-info --dormant-file-limit 15
```

### names

**Syntax:**
```bash
./wksta [auth_flags] names [--type <primary|alternate|all>]
```

**List registered computer names for the workstation (default: --type all) PrimaryComputerName is printed as a single value; AlternateComputerNames are listed.:**

```bash
./wksta [auth_flags] names
```

```bash
./wksta [auth_flags] names --type alternate
```

### joinable-ous

**Syntax:**
```bash
./wksta [auth_flags] joinable-ous <domain>
```

**Enumerate OUs in a domain that this machine can join:**

```bash
./wksta [auth_flags] joinable-ous DOMAIN.LOCAL
```

### join-domain

**Syntax:**
```bash
./wksta [auth_flags] join-domain <domain> [--options <n>]
```

**Join the workstation to a domain:**

```bash
./wksta [auth_flags] join-domain DOMAIN.LOCAL --options 0
```

### unjoin-domain

**Syntax:**
```bash
./wksta [auth_flags] unjoin-domain [--options <n>]
```

**Remove the workstation from its domain:**

```bash
./wksta [auth_flags] unjoin-domain --options 0
```

### rename-machine

**Syntax:**
```bash
./wksta [auth_flags] rename-machine <new-name> [--rename-account] [--dns-only]
```

**Rename the machine account within the domain --rename-account  also rename the computer account in AD (NETSETUP_ACCT_CREATE, 0x2) --dns-only        limit updates to DNS-based names only (NETSETUP_DNS_NAME_CHANGES_ONLY, 0x1000):**

```bash
./wksta [auth_flags] rename-machine WS02 --rename-account
```

### validate-name

**Syntax:**
```bash
./wksta [auth_flags] validate-name <name> [--name-type <type>]
```

**Validate a potential machine or domain name against naming rules:**

```bash
./wksta [auth_flags] validate-name WS02 --name-type 1
```

### add-alt-name

**Syntax:**
```bash
./wksta [auth_flags] add-alt-name <alt-name>
```

**Add a DNS alternate computer name to the workstation:**

```bash
./wksta [auth_flags] add-alt-name alias.DOMAIN.LOCAL
```

### del-alt-name

**Syntax:**
```bash
./wksta [auth_flags] del-alt-name <alt-name>
```

**Remove a DNS alternate computer name from the workstation:**

```bash
./wksta [auth_flags] del-alt-name alias.DOMAIN.LOCAL
```

### set-primary-name

**Syntax:**
```bash
./wksta [auth_flags] set-primary-name <primary-name>
```

**Promote an existing alternate DNS computer name to primary:**

```bash
./wksta [auth_flags] set-primary-name newname.DOMAIN.LOCAL
```


Note: the new primary name must already exist as an alternate name.  
Example flow: add-alt-name -> set-primary-name -> (optional) del-alt-name oldname  

### add-transport

**Syntax:**
```bash
./wksta [auth_flags] add-transport <transport-name> [--quality <n>]
```

**Add a transport protocol binding to the workstation:**

```bash
./wksta [auth_flags] add-transport '\Device\NetBT_Tcpip_{D1B719B7-6A4A-4E77-8EAC-E53584969BB0}'
```

### del-transport

**Syntax:**
```bash
./wksta [auth_flags] del-transport <transport-name> [--force-level <n>]
```

**Remove a transport protocol binding from the workstation:**

```bash
./wksta [auth_flags] del-transport '\Device\NetBT_Tcpip_{D1B719B7-6A4A-4E77-8EAC-E53584969BB0}' --force-level 2
```
