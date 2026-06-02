# 📦 DHCP (dhcp)

**Protocols**: [MS-DHCPM](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DHCPM/%5bMS-DHCPM%5d.pdf).

## Subcommands / Usage

### server-version

**Syntax:**
```bash
./dhcp [auth_flags] server-version
```

**Print the DHCP server version:**

```bash
./dhcp [auth_flags] server-version
```

### scopes

**Syntax:**
```bash
./dhcp [auth_flags] scopes
```

**List all DHCP scopes on the server:**

```bash
./dhcp [auth_flags] scopes
```

### scope

**Syntax:**
```bash
./dhcp [auth_flags] scope <scope-ip>
```

**Show detailed information for a specific scope:**

```bash
./dhcp [auth_flags] scope 10.0.20.0
```

### leases

**Syntax:**
```bash
./dhcp [auth_flags] leases [-s <scope-ip>]
```

**List all active DHCP leases across all scopes:**

```bash
./dhcp [auth_flags] leases
```

**List active leases for a specific scope:**

```bash
./dhcp [auth_flags] leases -s 10.0.20.0
```

### dump

**Syntax:**
```bash
./dhcp [auth_flags] dump [-s <scope-ip>] [--no-clients] [--no-options] [--no-stats]
```

**Dump a full report of all scopes, leases, options, and statistics:**

```bash
./dhcp [auth_flags] dump
```

**Dump scope configuration only, skipping clients and options:**

```bash
./dhcp [auth_flags] dump -s 10.0.20.0 --no-clients --no-options
```

### stats

**Syntax:**
```bash
./dhcp [auth_flags] stats
```

**Show DHCP server statistics:**

```bash
./dhcp [auth_flags] stats
```

### add-scope

**Syntax:**
```bash
./dhcp [auth_flags] add-scope <scope-ip> -m <mask> --name <name> [--comment <text>]
```

**Create a new DHCP scope:**

```bash
./dhcp [auth_flags] add-scope 10.0.20.0 -m 255.255.255.0 --name 'Lab' --comment 'Lab subnet'
```

### set-scope

**Syntax:**
```bash
./dhcp [auth_flags] set-scope <scope-ip> [--name <name>] [--comment <text>] [--state <enabled|disabled>]
```

**Rename and enable an existing scope:**

```bash
./dhcp [auth_flags] set-scope 10.0.20.0 --name 'Lab-Renamed' --state enabled
```

### del-scope

**Syntax:**
```bash
./dhcp [auth_flags] del-scope <scope-ip> [-f]
```

**Delete a scope, forcing removal even if active leases exist:**

```bash
./dhcp [auth_flags] del-scope 10.0.20.0 -f
```

### ranges

**Syntax:**
```bash
./dhcp [auth_flags] ranges <scope-ip>
```

**List address ranges for a scope:**

```bash
./dhcp [auth_flags] ranges 10.0.20.0
```

### add-range

**Syntax:**
```bash
./dhcp [auth_flags] add-range <scope-ip> -F <start-ip> -T <end-ip>
```

**Add an address range to a scope:**

```bash
./dhcp [auth_flags] add-range 10.0.20.0 -F 10.0.20.10 -T 10.0.20.200
```

### del-range

**Syntax:**
```bash
./dhcp [auth_flags] del-range <scope-ip> -F <start-ip> -T <end-ip> [--force]
```

**Remove an address range from a scope:**

```bash
./dhcp [auth_flags] del-range 10.0.20.0 -F 10.0.20.10 -T 10.0.20.200 --force
```

### exclusions

**Syntax:**
```bash
./dhcp [auth_flags] exclusions <scope-ip>
```

**List address exclusions for a scope:**

```bash
./dhcp [auth_flags] exclusions 10.0.20.0
```

### add-exclusion

**Syntax:**
```bash
./dhcp [auth_flags] add-exclusion <scope-ip> -F <start-ip> -T <end-ip>
```

**Exclude an IP range from assignment in a scope:**

```bash
./dhcp [auth_flags] add-exclusion 10.0.20.0 -F 10.0.20.100 -T 10.0.20.110
```

### del-exclusion

**Syntax:**
```bash
./dhcp [auth_flags] del-exclusion <scope-ip> -F <start-ip> -T <end-ip>
```

**Remove an IP exclusion range from a scope:**

```bash
./dhcp [auth_flags] del-exclusion 10.0.20.0 -F 10.0.20.100 -T 10.0.20.110
```

### reservations

**Syntax:**
```bash
./dhcp [auth_flags] reservations <scope-ip>
```

**List IP reservations for a scope:**

```bash
./dhcp [auth_flags] reservations 10.0.20.0
```

### add-reservation

**Syntax:**
```bash
./dhcp [auth_flags] add-reservation <scope-ip> --ip <ip> --mac <mac>
```

**Create a reservation binding a MAC address to an IP:**

```bash
./dhcp [auth_flags] add-reservation 10.0.20.0 --ip 10.0.20.50 --mac 00:11:22:33:44:55
```

### del-reservation

**Syntax:**
```bash
./dhcp [auth_flags] del-reservation <scope-ip> --ip <ip>
```

**Remove a reservation from a scope:**

```bash
./dhcp [auth_flags] del-reservation 10.0.20.0 --ip 10.0.20.50
```

### reservation

**Syntax:**
```bash
./dhcp [auth_flags] reservation <scope-ip> <ip>
```

**Show details for a single IP reservation:**

```bash
./dhcp [auth_flags] reservation 10.0.20.0 10.0.20.50
```

### set-reservation

**Syntax:**
```bash
./dhcp [auth_flags] set-reservation <scope-ip> <ip> <new-mac>
```

**Update the MAC address of an existing reservation:**

```bash
./dhcp [auth_flags] set-reservation 10.0.20.0 10.0.20.50 00:11:22:33:44:AA
```

### options

**Syntax:**
```bash
./dhcp [auth_flags] options [-s <scope-ip>]
```

**List server-level option values:**

```bash
./dhcp [auth_flags] options
```

**List scope-level option values:**

```bash
./dhcp [auth_flags] options -s 10.0.20.0
```

### set-option

**Syntax:**
```bash
./dhcp [auth_flags] set-option <option-id> [-s <scope-ip>] --type <type> --value <value>
```

**Set a scope-level DHCP option (e.g. DNS servers):**

```bash
./dhcp [auth_flags] set-option 6 -s 10.0.20.0 --type ip --value 10.0.20.2
```

### option

**Syntax:**
```bash
./dhcp [auth_flags] option <option-id> [-s <scope-ip>]
```

**Read a server-level DHCP option value:**

```bash
./dhcp [auth_flags] option 6
```

**Read a scope-level DHCP option value:**

```bash
./dhcp [auth_flags] option 6 -s 10.0.20.0
```

### del-option

**Syntax:**
```bash
./dhcp [auth_flags] del-option <option-id> [-s <scope-ip>]
```

**Remove a scope-level option value:**

```bash
./dhcp [auth_flags] del-option 6 -s 10.0.20.0
```

### add-option-type

**Syntax:**
```bash
./dhcp [auth_flags] add-option-type <option-id> --name <name> --type <type> [--array]
```

**Define a new custom DHCP option type:**

```bash
./dhcp [auth_flags] add-option-type 222 --name 'MyOption' --type string
```

### set-option-type

**Syntax:**
```bash
./dhcp [auth_flags] set-option-type <option-id> --name <name> [--type <type>]
```

**Update a custom DHCP option type definition:**

```bash
./dhcp [auth_flags] set-option-type 222 --name 'MyOption-Renamed'
```

### option-type

**Syntax:**
```bash
./dhcp [auth_flags] option-type <option-id>
```

**Read the definition of a custom option type:**

```bash
./dhcp [auth_flags] option-type 222
```

### option-types

**Syntax:**
```bash
./dhcp [auth_flags] option-types
```

**List all registered DHCP option type definitions:**

```bash
./dhcp [auth_flags] option-types
```

### del-option-type

**Syntax:**
```bash
./dhcp [auth_flags] del-option-type <option-id>
```

**Delete a custom DHCP option type definition:**

```bash
./dhcp [auth_flags] del-option-type 222
```

### add-lease

**Syntax:**
```bash
./dhcp [auth_flags] add-lease --ip <ip> --mac <mac> [--name <name>] [--comment <text>]
```

**Add a DHCP lease record:**

```bash
./dhcp [auth_flags] add-lease --ip 10.0.20.80 --mac 00:11:22:33:44:66 --name ws01 --comment 'lab workstation'
```

### lease

**Syntax:**
```bash
./dhcp [auth_flags] lease <ip>
```

**Look up a DHCP lease record by IP:**

```bash
./dhcp [auth_flags] lease 10.0.20.80
```

### set-lease

**Syntax:**
```bash
./dhcp [auth_flags] set-lease --ip <ip> --mac <mac> [--name <name>] [--comment <text>]
```

**Update a DHCP lease record:**

```bash
./dhcp [auth_flags] set-lease --ip 10.0.20.80 --mac 00:11:22:33:44:66 --name ws01-renamed
```

### config

**Syntax:**
```bash
./dhcp [auth_flags] config
```

**Show the current DHCP server configuration:**

```bash
./dhcp [auth_flags] config
```

### set-config

**Syntax:**
```bash
./dhcp [auth_flags] set-config [--backup-path <path>] [--db-path <path>] [--backup-interval <n>] ...
```

**Change the DHCP server backup path:**

```bash
./dhcp [auth_flags] set-config --backup-path 'C:\DHCP\Backup'
```

### scan-db

**Syntax:**
```bash
./dhcp [auth_flags] scan-db [-s <scope-ip>] [--repair]
```

**Scan the DHCP database for inconsistencies:**

```bash
./dhcp [auth_flags] scan-db
```

**Scan and repair database inconsistencies for a specific scope:**

```bash
./dhcp [auth_flags] scan-db -s 10.0.20.0 --repair
```

### del-lease

**Syntax:**
```bash
./dhcp [auth_flags] del-lease <client-ip>
```

**Force-expire an active DHCP lease:**

```bash
./dhcp [auth_flags] del-lease 10.0.20.80
```
