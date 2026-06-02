# 🌐 DNS (dns)

**Protocols**: [MS-DNSP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DNSP/%5bMS-DNSP%5d.pdf).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags]
```
{% endhint %}

### List all DNS zones on the server; equivalent to the 'zones' subcommand

```bash
./dns [auth_flags]
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] zones
```
{% endhint %}

### List all DNS zones on the server

```bash
./dns [auth_flags] zones
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] records <zone> [-n <node>] [-T <A|AAAA|MX|TXT|CNAME|SRV|NS|PTR|SOA|ALL>]
```
{% endhint %}

### List all DNS records in a zone

```bash
./dns [auth_flags] records EXAMPLE.LOCAL
```

### List records of a specific node and type within a zone

```bash
./dns [auth_flags] records EXAMPLE.LOCAL -n _tcp -T SRV
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] nodes <zone> [-n <parent-node>]
```
{% endhint %}

### List all nodes in a DNS zone

```bash
./dns [auth_flags] nodes EXAMPLE.LOCAL
```

### List child nodes under a parent node in a zone

```bash
./dns [auth_flags] nodes EXAMPLE.LOCAL -n _tcp
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] dump [-z <zone>] [--skip-cache=<true|false>]
```
{% endhint %}

### Dump all DNS records from all zones

```bash
./dns [auth_flags] dump
```

### Dump all DNS records from a specific zone (optionally including cache)

```bash
./dns [auth_flags] dump -z EXAMPLE.LOCAL --skip-cache=false
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] add-record <zone> -n <node> -T <type> -v <value> [--ttl <sec>]
```
{% endhint %}

### Add a DNS resource record to a zone

```bash
./dns [auth_flags] add-record EXAMPLE.LOCAL -n myhost -T A -v 10.0.0.99 --ttl 600
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] del-record <zone> -n, --node <node> -T, --type <type> -v, --value <data> [--ttl <sec>]
```
{% endhint %}

### Delete a DNS resource record from a zone

```bash
./dns [auth_flags] del-record EXAMPLE.LOCAL -n myhost -T A -v 10.0.0.99
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] server-props [-O, --operation <name>] [--property <name>]
```
{% endhint %}

### Query a named server operation

```bash
./dns [auth_flags] server-props -O ServerInfo
```

### Query a specific server property

```bash
./dns [auth_flags] server-props --property Forwarders
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] server-stats [--clear]
```
{% endhint %}

### Query server statistics

```bash
./dns [auth_flags] server-stats
```

### Query and clear server statistics

```bash
./dns [auth_flags] server-stats --clear
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] server-scopes
```
{% endhint %}

### List DNS server scopes

```bash
./dns [auth_flags] server-scopes
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] zone <zone> [--property <name>]
```
{% endhint %}

### Query full zone configuration

```bash
./dns [auth_flags] zone EXAMPLE.LOCAL
```

### Query a specific zone property

```bash
./dns [auth_flags] zone EXAMPLE.LOCAL --property AllowUpdate
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] zone-stats <zone> [--clear]
```
{% endhint %}

### Query zone statistics

```bash
./dns [auth_flags] zone-stats EXAMPLE.LOCAL
```

### Query and clear zone statistics

```bash
./dns [auth_flags] zone-stats EXAMPLE.LOCAL --clear
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] zone-scopes <zone|..cache>
```
{% endhint %}

### List scopes for a DNS zone

```bash
./dns [auth_flags] zone-scopes EXAMPLE.LOCAL
```

### List scopes for the server cache

```bash
./dns [auth_flags] zone-scopes ..cache
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] policies [-z <zone>]
```
{% endhint %}

### List server-level DNS policies

```bash
./dns [auth_flags] policies
```

### List policies for a specific zone

```bash
./dns [auth_flags] policies -z EXAMPLE.LOCAL
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] policy <policy-name> [-z <zone>]
```
{% endhint %}

### Show a server-level policy by name

```bash
./dns [auth_flags] policy BlockAny
```

### Show a zone-level policy by name

```bash
./dns [auth_flags] policy ZonePolicy1 -z EXAMPLE.LOCAL
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] client-subnets
```
{% endhint %}

### List DNS client subnet records

```bash
./dns [auth_flags] client-subnets
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] client-subnet <subnet-record-name>
```
{% endhint %}

### Show details for a named client subnet record

```bash
./dns [auth_flags] client-subnet BranchOffice-IPv4
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] add-zone <zone> [--type <primary|secondary|stub|forwarder>] [--master <ip> ...] [--ds]
```
{% endhint %}

### Create a standard primary zone

```bash
./dns [auth_flags] add-zone NEW.LOCAL --type primary
```

### Create a DS-integrated primary zone

```bash
./dns [auth_flags] add-zone NEW.LOCAL --type primary --ds
```

### Create a secondary zone with a master server

```bash
./dns [auth_flags] add-zone NEW.LOCAL --type secondary --master 10.0.0.1
```

### Create a conditional forwarder zone

```bash
./dns [auth_flags] add-zone EXT.CORP --type forwarder --master 8.8.8.8
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] del-zone <zone>
```
{% endhint %}

### Delete a DNS zone

```bash
./dns [auth_flags] del-zone OLD.LOCAL
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] pause-zone <zone>
```
{% endhint %}

### Pause a DNS zone (stops it from answering queries)

```bash
./dns [auth_flags] pause-zone EXAMPLE.LOCAL
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] resume-zone <zone>
```
{% endhint %}

### Resume a paused DNS zone

```bash
./dns [auth_flags] resume-zone EXAMPLE.LOCAL
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] reload-zone <zone>
```
{% endhint %}

### Reload a DNS zone from its storage backend

```bash
./dns [auth_flags] reload-zone EXAMPLE.LOCAL
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] set-forwarders [--forwarder <ipv4> ...] [--timeout <sec>] [--no-recurse]
```
{% endhint %}

### Set DNS forwarders with a query timeout

```bash
./dns [auth_flags] set-forwarders --forwarder 8.8.8.8 --forwarder 8.8.4.4 --timeout 5
```

### Clear all DNS forwarders

```bash
./dns [auth_flags] set-forwarders
```

{% hint style="info" %}
**Syntax**

```bash
./dns [auth_flags] version
```
{% endhint %}

### Query the DNS server version

```bash
./dns [auth_flags] version
```
