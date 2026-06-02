# 🎟️ Kerberos ST (getst)

**Protocols**: [RFC 4120](https://datatracker.ietf.org/doc/html/rfc4120) / [MS-KILE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-KILE/%5bMS-KILE%5d.pdf) / [MS-SFU](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SFU/%5bMS-SFU%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
getst [auth_flags] -c <ccache> -s <spn> --dc <dc> -o <out> [--self -i <user>]
```

### Request a service ticket for a given SPN using an existing TGT

```bash
./getst [auth_flags] -c administrator@EXAMPLE.LOCAL.ccache -s cifs/dc01.example.com --dc dc01.example.com -o cifs_dc01.ccache
```

### Request an S4U2Self impersonation evidence ticket

```bash
./getst [auth_flags] -c svc_iis@EXAMPLE.LOCAL.ccache -i jdoe --self --dc dc01.example.com -o jdoe_evidence.ccache
```
