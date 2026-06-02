# 💻 Workstation (wksta)

**Protocols**: [MS-WKST](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-WKST/%5bMS-WKST%5d.pdf).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] info [--detail <basic|lan|full|config>]
```
{% endhint %}

### Query workstation configuration and identity info (default: full)

```bash
./wksta [auth_flags] info --detail full
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] loggedon
```
{% endhint %}

### List users currently logged on to the workstation interactively

```bash
./wksta [auth_flags] loggedon
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] transports
```
{% endhint %}

### Enumerate network transports bound to the workstation

```bash
./wksta [auth_flags] transports
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] join-info
```
{% endhint %}

### Query the current domain or workgroup join status

```bash
./wksta [auth_flags] join-info
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] stats
```
{% endhint %}

### Show SMB redirector statistics (bytes transferred, sessions, operations)

```bash
./wksta [auth_flags] stats
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] set-info (--keep-conn | --sess-timeout | --dormant-file-limit) <n>
```
{% endhint %}

### Set the keep-alive connection interval in seconds

```bash
./wksta [auth_flags] set-info --keep-conn 30
```

### Set the session timeout in seconds

```bash
./wksta [auth_flags] set-info --sess-timeout 45
```

### Set the dormant file handle limit

```bash
./wksta [auth_flags] set-info --dormant-file-limit 15
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] names [--type <primary|alternate|all>]
```
{% endhint %}

### List registered computer names for the workstation (default: --type all)

PrimaryComputerName is printed as a single value; AlternateComputerNames are listed.  


```bash
./wksta [auth_flags] names
```

```bash
./wksta [auth_flags] names --type alternate
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] joinable-ous <domain>
```
{% endhint %}

### Enumerate OUs in a domain that this machine can join

```bash
./wksta [auth_flags] joinable-ous EXAMPLE.LOCAL
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] join-domain <domain> [--options <n>]
```
{% endhint %}

### Join the workstation to a domain

```bash
./wksta [auth_flags] join-domain EXAMPLE.LOCAL --options 0
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] unjoin-domain [--options <n>]
```
{% endhint %}

### Remove the workstation from its domain

```bash
./wksta [auth_flags] unjoin-domain --options 0
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] rename-machine <new-name> [--rename-account] [--dns-only]
```
{% endhint %}

### Rename the machine account within the domain

--rename-account  also rename the computer account in AD (NETSETUP_ACCT_CREATE, 0x2)  
--dns-only        limit updates to DNS-based names only (NETSETUP_DNS_NAME_CHANGES_ONLY, 0x1000)  


```bash
./wksta [auth_flags] rename-machine WS02 --rename-account
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] validate-name <name> [--name-type <type>]
```
{% endhint %}

### Validate a potential machine or domain name against naming rules

```bash
./wksta [auth_flags] validate-name WS02 --name-type 1
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] add-alt-name <alt-name>
```
{% endhint %}

### Add a DNS alternate computer name to the workstation

```bash
./wksta [auth_flags] add-alt-name alias.example.local
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] del-alt-name <alt-name>
```
{% endhint %}

### Remove a DNS alternate computer name from the workstation

```bash
./wksta [auth_flags] del-alt-name alias.example.local
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] set-primary-name <primary-name>
```
{% endhint %}

### Promote an existing alternate DNS computer name to primary

```bash
./wksta [auth_flags] set-primary-name newname.example.local
```


Note: the new primary name must already exist as an alternate name.  
Example flow: add-alt-name -> set-primary-name -> (optional) del-alt-name oldname  

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] add-transport <transport-name> [--quality <n>]
```
{% endhint %}

### Add a transport protocol binding to the workstation

```bash
./wksta [auth_flags] add-transport '\Device\NetBT_Tcpip_{D1B719B7-6A4A-4E77-8EAC-E53584969BB0}'
```

{% hint style="info" %}
**Syntax**

```bash
./wksta [auth_flags] del-transport <transport-name> [--force-level <n>]
```
{% endhint %}

### Remove a transport protocol binding from the workstation

```bash
./wksta [auth_flags] del-transport '\Device\NetBT_Tcpip_{D1B719B7-6A4A-4E77-8EAC-E53584969BB0}' --force-level 2
```
