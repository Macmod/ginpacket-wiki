# 🧰 Services (services)

**Protocols**: [MS-SCMR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SCMR/%5bMS-SCMR%5d.pdf).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] dump [--type <mask>] [--state <mask>] [--group <name>]
```
{% endhint %}

### Enumerate all services with their type, state, and group

```bash
./services [auth_flags] dump
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] query [--type <mask>] [--state <mask>] [--group <name>]
```
{% endhint %}

### Query running services with optional type/state/group filters

```bash
./services [auth_flags] query
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] service <name> [--use-v1]
```
{% endhint %}

### Show full configuration info for a service

```bash
./services [auth_flags] service Spooler
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] get-sd <name> [--parse-dacl]
```
{% endhint %}

### Read the security descriptor of a service

```bash
./services [auth_flags] get-sd Spooler
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] group <group-name>
```
{% endhint %}

### Query the load-order group for a service group

```bash
./services [auth_flags] group 'NetworkProvider'
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] enum-deps <name>
```
{% endhint %}

### List all services that depend on a given service

```bash
./services [auth_flags] enum-deps Spooler
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] translate (-K <svc-key> | -N <display-name>)
```
{% endhint %}

### Translate between a service's registry key name and its display name

```bash
./services [auth_flags] translate -K Spooler
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] add-service <name> <binpath> [-N <display>] [--service-type <type>] [-T <start-type>] [--wow64] [--wow-type <arch>]
```
{% endhint %}

### Create a new service with an on-demand start type

```bash
./services [auth_flags] add-service MyService 'C:\Windows\System32\cmd.exe /c whoami > C:\temp\x.txt' -N 'My Service' -T demand --service-type own
```

### Register a service as a 32-bit WOW64 service (RCreateServiceWOW64W, opnum 45)

```bash
./services [auth_flags] add-service MySvc32 'C:\tools\agent32.exe' --wow64
```


Register a service for a specific machine architecture (RCreateWowService, opnum 60)  


```bash
./services [auth_flags] add-service MySvcArch 'C:\tools\agent.exe' --wow-type i386
```

```bash
./services [auth_flags] add-service MySvcArch 'C:\tools\agent.exe' --wow-type 0x014c
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] set-service <name> [-b <binpath>] [-T <start-type>] [-a <account>] ...
```
{% endhint %}

### Modify configuration of an existing service

```bash
./services [auth_flags] set-service MyService -b 'C:\new\path.exe' -T auto
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] set-failure <name> [-F <command>] [--reset-period <sec>]
```
{% endhint %}

### Configure failure recovery actions for a service

```bash
./services [auth_flags] set-failure MyService -F 'net start MyService' --reset-period 3600
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] set-sd <name> --sd <hex-sd>
```
{% endhint %}

### Write a custom security descriptor to a service (use hex output from get-sd)

```bash
./services [auth_flags] set-sd MyService --sd '01000480200000002c00000000000000'
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] start <name> [--arg <value> ...]
```
{% endhint %}

### Start a service, optionally passing arguments

```bash
./services [auth_flags] start Spooler --arg '-example'
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] stop <name> [--reason <hex>] [--planned] [--comment <text>]
```
{% endhint %}

### Stop a service with an optional reason code

```bash
./services [auth_flags] stop Spooler
```

{% hint style="info" %}
**Syntax**

```bash
./services [auth_flags] del-service <name>
```
{% endhint %}

### Delete a service

```bash
./services [auth_flags] del-service MyService
```
