# 🧩 RPC Endpoint Mapper (rpcdump)

**Protocols**: [MS-RPCE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-RPCE/%5bMS-RPCE%5d.pdf) Endpoint Mapper.

## Subcommands / Usage

### Syntax

```bash
./rpcdump [auth_flags] [-U <interface-uuid>] [--transport <transports>]
```

### Enumerate all registered RPC endpoints via the endpoint mapper

```bash
./rpcdump [auth_flags]
```

### Filter results by interface UUID and transport set

```bash
./rpcdump [auth_flags] -U 6bffd098-a112-610e-9fbf-00a0c90d67da --transport ncacn_ip_tcp,ncacn_np
```
