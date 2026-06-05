# 🌐 DNS (dns)

**Protocols**: [MS-DNSP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DNSP/%5bMS-DNSP%5d.pdf).

The DNS Server Management Protocol (MS-DNSP) allows remote administration of a Windows DNS server via RPC. It provides full control over DNS zones and records - including querying, adding, modifying, and deleting entries.

## Usage

### General

**Syntax:**
```bash
./dns [auth_flags]
```

**List all DNS zones on the server; equivalent to the 'zones' subcommand:**

```bash
./dns [auth_flags]
```

### zones

**Syntax:**
```bash
./dns [auth_flags] zones
```

**List all DNS zones on the server:**

```bash
./dns [auth_flags] zones
```

### records

**Syntax:**
```bash
./dns [auth_flags] records <zone> [-n <node>] [-T <A|AAAA|MX|TXT|CNAME|SRV|NS|PTR|SOA|ALL>]
```

**List all DNS records in a zone:**

```bash
./dns [auth_flags] records DOMAIN.LOCAL
```

**List records of a specific node and type within a zone:**

```bash
./dns [auth_flags] records DOMAIN.LOCAL -n _tcp -T SRV
```

### nodes

**Syntax:**
```bash
./dns [auth_flags] nodes <zone> [-n <parent-node>]
```

**List all nodes in a DNS zone:**

```bash
./dns [auth_flags] nodes DOMAIN.LOCAL
```

**List child nodes under a parent node in a zone:**

```bash
./dns [auth_flags] nodes DOMAIN.LOCAL -n _tcp
```

### dump

**Syntax:**
```bash
./dns [auth_flags] dump [-z <zone>] [--skip-cache=<true|false>]
```

**Dump all DNS records from all zones:**

```bash
./dns [auth_flags] dump
```

**Dump all DNS records from a specific zone (optionally including cache):**

```bash
./dns [auth_flags] dump -z DOMAIN.LOCAL --skip-cache=false
```

### add-record

**Syntax:**
```bash
./dns [auth_flags] add-record <zone> -n <node> -T <type> -v <value> [--ttl <sec>]
```

**Add a DNS resource record to a zone:**

```bash
./dns [auth_flags] add-record DOMAIN.LOCAL -n myhost -T A -v 10.0.0.99 --ttl 600
```

### del-record

**Syntax:**
```bash
./dns [auth_flags] del-record <zone> -n, --node <node> -T, --type <type> -v, --value <data> [--ttl <sec>]
```

**Delete a DNS resource record from a zone:**

```bash
./dns [auth_flags] del-record DOMAIN.LOCAL -n myhost -T A -v 10.0.0.99
```

### server-props

**Syntax:**
```bash
./dns [auth_flags] server-props [-O, --operation <name>] [--property <name>]
```

**Query a named server operation:**

```bash
./dns [auth_flags] server-props -O ServerInfo
```

**Query a specific server property:**

```bash
./dns [auth_flags] server-props --property Forwarders
```

### server-stats

**Syntax:**
```bash
./dns [auth_flags] server-stats [--clear]
```

**Query server statistics:**

```bash
./dns [auth_flags] server-stats
```

**Query and clear server statistics:**

```bash
./dns [auth_flags] server-stats --clear
```

### server-scopes

**Syntax:**
```bash
./dns [auth_flags] server-scopes
```

**List DNS server scopes:**

```bash
./dns [auth_flags] server-scopes
```

### zone

**Syntax:**
```bash
./dns [auth_flags] zone <zone> [--property <name>]
```

**Query full zone configuration:**

```bash
./dns [auth_flags] zone DOMAIN.LOCAL
```

**Query a specific zone property:**

```bash
./dns [auth_flags] zone DOMAIN.LOCAL --property AllowUpdate
```

### zone-stats

**Syntax:**
```bash
./dns [auth_flags] zone-stats <zone> [--clear]
```

**Query zone statistics:**

```bash
./dns [auth_flags] zone-stats DOMAIN.LOCAL
```

**Query and clear zone statistics:**

```bash
./dns [auth_flags] zone-stats DOMAIN.LOCAL --clear
```

### zone-scopes

**Syntax:**
```bash
./dns [auth_flags] zone-scopes <zone|..cache>
```

**List scopes for a DNS zone:**

```bash
./dns [auth_flags] zone-scopes DOMAIN.LOCAL
```

**List scopes for the server cache:**

```bash
./dns [auth_flags] zone-scopes ..cache
```

### policies

**Syntax:**
```bash
./dns [auth_flags] policies [-z <zone>]
```

**List server-level DNS policies:**

```bash
./dns [auth_flags] policies
```

**List policies for a specific zone:**

```bash
./dns [auth_flags] policies -z DOMAIN.LOCAL
```

### policy

**Syntax:**
```bash
./dns [auth_flags] policy <policy-name> [-z <zone>]
```

**Show a server-level policy by name:**

```bash
./dns [auth_flags] policy BlockAny
```

**Show a zone-level policy by name:**

```bash
./dns [auth_flags] policy ZonePolicy1 -z DOMAIN.LOCAL
```

### client-subnets

**Syntax:**
```bash
./dns [auth_flags] client-subnets
```

**List DNS client subnet records:**

```bash
./dns [auth_flags] client-subnets
```

### client-subnet

**Syntax:**
```bash
./dns [auth_flags] client-subnet <subnet-record-name>
```

**Show details for a named client subnet record:**

```bash
./dns [auth_flags] client-subnet BranchOffice-IPv4
```

### add-zone

**Syntax:**
```bash
./dns [auth_flags] add-zone <zone> [--type <primary|secondary|stub|forwarder>] [--master <ip> ...] [--ds]
```

**Create a standard primary zone:**

```bash
./dns [auth_flags] add-zone NEW.LOCAL --type primary
```

**Create a DS-integrated primary zone:**

```bash
./dns [auth_flags] add-zone NEW.LOCAL --type primary --ds
```

**Create a secondary zone with a master server:**

```bash
./dns [auth_flags] add-zone NEW.LOCAL --type secondary --master 10.0.0.1
```

**Create a conditional forwarder zone:**

```bash
./dns [auth_flags] add-zone EXT.CORP --type forwarder --master 8.8.8.8
```

### del-zone

**Syntax:**
```bash
./dns [auth_flags] del-zone <zone>
```

**Delete a DNS zone:**

```bash
./dns [auth_flags] del-zone OLD.LOCAL
```

### pause-zone

**Syntax:**
```bash
./dns [auth_flags] pause-zone <zone>
```

**Pause a DNS zone (stops it from answering queries):**

```bash
./dns [auth_flags] pause-zone DOMAIN.LOCAL
```

### resume-zone

**Syntax:**
```bash
./dns [auth_flags] resume-zone <zone>
```

**Resume a paused DNS zone:**

```bash
./dns [auth_flags] resume-zone DOMAIN.LOCAL
```

### reload-zone

**Syntax:**
```bash
./dns [auth_flags] reload-zone <zone>
```

**Reload a DNS zone from its storage backend:**

```bash
./dns [auth_flags] reload-zone DOMAIN.LOCAL
```

### set-forwarders

**Syntax:**
```bash
./dns [auth_flags] set-forwarders [--forwarder <ipv4> ...] [--timeout <sec>] [--no-recurse]
```

**Set DNS forwarders with a query timeout:**

```bash
./dns [auth_flags] set-forwarders --forwarder 8.8.8.8 --forwarder 8.8.4.4 --timeout 5
```

**Clear all DNS forwarders:**

```bash
./dns [auth_flags] set-forwarders
```

### version

**Syntax:**
```bash
./dns [auth_flags] version
```

**Query the DNS server version:**

```bash
./dns [auth_flags] version
```
