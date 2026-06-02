# 📜 Event Log (eventlog)

**Protocols**: [MS-EVEN6](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-EVEN6/%5bMS-EVEN6%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
./eventlog [auth_flags] channels
```

### List all event log channels on the host

```bash
./eventlog [auth_flags] channels
```

### Syntax

```bash
./eventlog [auth_flags] publishers
```

### List all registered event publishers

```bash
./eventlog [auth_flags] publishers
```

### Syntax

```bash
./eventlog [auth_flags] query <channel> [-q <xpath>] [-L <n>] [-T <ms>]
```

### Query events from a channel using an XPath filter

```bash
./eventlog [auth_flags] query Security -q "*" -L 10 -T 5000
```

### Syntax

```bash
./eventlog [auth_flags] subscribe <channel> [-q <xpath>] [-L <n>] [-T <ms>]
```

### Subscribe to a channel and receive events as they arrive

```bash
./eventlog [auth_flags] subscribe Security -q "*" -L 10 -T 5000
```

### Syntax

```bash
./eventlog [auth_flags] watch <channel> [--event-id <ids>] [--grep <str>] [-L <n>] [-F <text|json>]
```

### Live-tail a channel for future events, with optional filtering

```bash
./eventlog [auth_flags] watch Security
```

```bash
./eventlog [auth_flags] watch Security --event-id 4624,4625 -L 20
```

### Syntax

```bash
./eventlog [auth_flags] export <channel> <out-path>
./eventlog [auth_flags] export --evtx-file <in-path> <out-path>
```

### Export a live channel to an .evtx file

```bash
./eventlog [auth_flags] export Security 'C:\temp\security.evtx'
```

### Export from an existing .evtx file to another .evtx file

```bash
./eventlog [auth_flags] export --evtx-file 'C:\temp\in.evtx' 'C:\temp\out.evtx'
```

### Syntax

```bash
./eventlog [auth_flags] clear <channel> [-b <backup-path>] [--confirm]
```

### Clear a channel and optionally save a backup

```bash
./eventlog [auth_flags] clear Security -b 'C:\temp\security-backup.evtx' --confirm
```

### Syntax

```bash
./eventlog [auth_flags] channel [<channel>] [-T config|meta|all]
```


Show channel information: config (EvtRpcGetChannelConfig), meta (EvtRpcGetLogFileInfo), or all (default)  


```bash
./eventlog [auth_flags] channel Security
```

```bash
./eventlog [auth_flags] channel Security -T config
```

```bash
./eventlog [auth_flags] channel Security -T meta
```

### Syntax

```bash
./eventlog [auth_flags] publisher <name>
```

### Show metadata for a registered event publisher (GUID, schema path, etc.)

```bash
./eventlog [auth_flags] publisher 'Microsoft-Windows-Security-Auditing'
```

### Syntax

```bash
./eventlog [auth_flags] channel-publishers [<channel>]
```

### List publishers registered to write to a specific channel

```bash
./eventlog [auth_flags] channel-publishers Security
```

### Syntax

```bash
./eventlog [auth_flags] classic-name <name>
```

### Resolve a classic event log name to its display name

```bash
./eventlog [auth_flags] classic-name Security
```

### Syntax

```bash
./eventlog [auth_flags] set-channel [<channel>] [--enabled <true|false>] [--max-size <bytes>]
```

### Enable or disable a channel and/or change its maximum log file size

```bash
./eventlog [auth_flags] set-channel Security --enabled false
```

```bash
./eventlog [auth_flags] set-channel Security --max-size 67108864
```
