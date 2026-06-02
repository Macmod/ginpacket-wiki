# 🕒 Time (time)

**Protocols**: [MS-W32T](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-W32T/%5bMS-W32T%5d.pdf).

## Subcommands / Usage

### sync

**Syntax:**
```bash
./time [auth_flags] sync [--wait <sec>] [--sync-flags <n>]
```

**Trigger a manual time synchronization:**

```bash
./time [auth_flags] sync --wait 1 --sync-flags 3
```

### bits

**Syntax:**
```bash
./time [auth_flags] bits
```

**Query the W32TM capability bits advertised by the service:**

```bash
./time [auth_flags] bits
```

### source

**Syntax:**
```bash
./time [auth_flags] source
```

**Query the current time source (NTP server) in use:**

```bash
./time [auth_flags] source
```

### config

**Syntax:**
```bash
./time [auth_flags] config
```

**Query the global W32TM service configuration:**

```bash
./time [auth_flags] config
```

### status

**Syntax:**
```bash
./time [auth_flags] status
```

**Query the current time synchronization status:**

```bash
./time [auth_flags] status
```

### log

**Syntax:**
```bash
./time [auth_flags] log
```

**Query the W32TM event log entries:**

```bash
./time [auth_flags] log
```

### provider-status

**Syntax:**
```bash
./time [auth_flags] provider-status <provider-name> [--provider-flags <n>]
```

**Query the status of a named time provider:**

```bash
./time [auth_flags] provider-status NtpClient
```

### provider-config

**Syntax:**
```bash
./time [auth_flags] provider-config <provider-name> [--provider-flags <n>]
```

**Query the configuration of a named time provider:**

```bash
./time [auth_flags] provider-config NtpClient
```
