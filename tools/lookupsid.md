# 🆔 SID Lookup (lookupsid)

**Protocols**: [MS-LSAT](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-LSAT/%5bMS-LSAT%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
lookupsid [auth_flags] (-s <sid> | -n <name> | -D <domain-sid> -F <start-rid> -T <end-rid>) [--use-v1]
```

### Resolve a well-known or arbitrary SID to its account name

```bash
./lookupsid [auth_flags] -s S-1-5-18
```

### Resolve an account name to its SID

```bash
./lookupsid [auth_flags] -n 'DOMAIN\Administrator'
```

### Brute-force RIDs in a range under a domain SID to enumerate accounts

```bash
./lookupsid [auth_flags] -D S-1-5-21-111-222-333 -F 500 -T 560
```

### Resolve a SID using the legacy v1 LsaLookupSids API

```bash
./lookupsid [auth_flags] -s S-1-5-18 --use-v1
```
