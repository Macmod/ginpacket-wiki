# 🎫 Kerberos TGT (gettgt)

**Protocols**: [RFC 4120](https://datatracker.ietf.org/doc/html/rfc4120) / [MS-KILE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-KILE/%5bMS-KILE%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
gettgt [auth_flags] --dc <DC> -o <ccache> (+ -p <password> | -H <LM:NT|NT> | --aes-key <hex> | --ccache <file> | --pfx <file>)
```

### Request a TGT using password credentials

```bash
./gettgt [auth_flags] -p 'P@ssw0rd!' --dc dc01.example.com -o administrator@EXAMPLE.LOCAL.ccache
```

### Request a TGT using an NT hash

```bash
./gettgt [auth_flags] -H 31d6cfe0d16ae931b73c59d7e0c089c0 --dc dc01.example.com -o administrator@EXAMPLE.LOCAL.ccache
```

### Request a TGT using an AES session key

```bash
./gettgt [auth_flags] --aes-key a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2 --dc dc01.example.com -o administrator@EXAMPLE.LOCAL.ccache
```
