# 🧰 Services (services)

**Protocols**: [MS-SCMR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SCMR/%5bMS-SCMR%5d.pdf).

## Subcommands / Usage

### `dump`

```bash
./services [auth_flags] dump [--type <mask>] [--state <mask>] [--group <name>]
```

**Enumerate all services with their type, state, and group:**

```bash
./services [auth_flags] dump
```

### `query`

```bash
./services [auth_flags] query [--type <mask>] [--state <mask>] [--group <name>]
```

**Query running services with optional type/state/group filters:**

```bash
./services [auth_flags] query
```

### `service`

```bash
./services [auth_flags] service <name> [--use-v1]
```

**Show full configuration info for a service:**

```bash
./services [auth_flags] service Spooler
```

### `get-sd`

```bash
./services [auth_flags] get-sd <name> [--parse-dacl]
```

**Read the security descriptor of a service:**

```bash
./services [auth_flags] get-sd Spooler
```

### `group`

```bash
./services [auth_flags] group <group-name>
```

**Query the load-order group for a service group:**

```bash
./services [auth_flags] group 'NetworkProvider'
```

### `enum-deps`

```bash
./services [auth_flags] enum-deps <name>
```

**List all services that depend on a given service:**

```bash
./services [auth_flags] enum-deps Spooler
```

### `translate`

```bash
./services [auth_flags] translate (-K <svc-key> | -N <display-name>)
```

**Translate between a service's registry key name and its display name:**

```bash
./services [auth_flags] translate -K Spooler
```

### `add-service`

```bash
./services [auth_flags] add-service <name> <binpath> [-N <display>] [--service-type <type>] [-T <start-type>] [--wow64] [--wow-type <arch>]
```

**Create a new service with an on-demand start type:**

```bash
./services [auth_flags] add-service MyService 'C:\Windows\System32\cmd.exe /c whoami > C:\temp\x.txt' -N 'My Service' -T demand --service-type own
```

**Register a service as a 32-bit WOW64 service (RCreateServiceWOW64W, opnum 45):**

```bash
./services [auth_flags] add-service MySvc32 'C:\tools\agent32.exe' --wow64
```

**Register a service for a specific machine architecture (RCreateWowService, opnum 60):**

```bash
./services [auth_flags] add-service MySvcArch 'C:\tools\agent.exe' --wow-type i386
```

```bash
./services [auth_flags] add-service MySvcArch 'C:\tools\agent.exe' --wow-type 0x014c
```

### `set-service`

```bash
./services [auth_flags] set-service <name> [-b <binpath>] [-T <start-type>] [-a <account>] ...
```

**Modify configuration of an existing service:**

```bash
./services [auth_flags] set-service MyService -b 'C:\new\path.exe' -T auto
```

### `set-failure`

```bash
./services [auth_flags] set-failure <name> [-F <command>] [--reset-period <sec>]
```

**Configure failure recovery actions for a service:**

```bash
./services [auth_flags] set-failure MyService -F 'net start MyService' --reset-period 3600
```

### `set-sd`

```bash
./services [auth_flags] set-sd <name> --sd <hex-sd>
```

**Write a custom security descriptor to a service (use hex output from get-sd):**

```bash
./services [auth_flags] set-sd MyService --sd '01000480200000002c00000000000000'
```

### `start`

```bash
./services [auth_flags] start <name> [--arg <value> ...]
```

**Start a service, optionally passing arguments:**

```bash
./services [auth_flags] start Spooler --arg '-example'
```

### `stop`

```bash
./services [auth_flags] stop <name> [--reason <hex>] [--planned] [--comment <text>]
```

**Stop a service with an optional reason code:**

```bash
./services [auth_flags] stop Spooler
```

### `del-service`

```bash
./services [auth_flags] del-service <name>
```

**Delete a service:**

```bash
./services [auth_flags] del-service MyService
```
