# ⏻ Shutdown (shutdown)

**Protocols**: [MS-RSP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-RSP/%5bMS-RSP%5d.pdf).

## Subcommands / Usage

### `initiate`

```bash
./shutdown [auth_flags] initiate [-m <msg>] [--timeout <s>] [--force] [-r] [--reason <code>] [--interface <iface>] [--use-v1]
```

**Initiate a remote shutdown with a message, timeout, force, and reboot:**

```bash
./shutdown [auth_flags] initiate -m 'maintenance' --timeout 120 --force -r --reason 'planned os maintenance'
```

**Initiate a shutdown using a numeric reason code:**

```bash
./shutdown [auth_flags] initiate --reason 0x80020001
```

**Initiate a shutdown using the legacy API (no reason codes):**

```bash
./shutdown [auth_flags] initiate --use-v1
```

### `abort`

```bash
./shutdown [auth_flags] abort
```

**Abort a pending remote shutdown:**

```bash
./shutdown [auth_flags] abort
```
