# 🎫 Kerberos TGT (gettgt)

**Protocols**: [RFC 4120](https://datatracker.ietf.org/doc/html/rfc4120) / [MS-KILE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-KILE/%5bMS-KILE%5d.pdf).

Kerberos is the primary authentication protocol in Active Directory. A Ticket Granting Ticket (TGT) is the initial credential obtained from the Key Distribution Center (KDC) after authentication, and it is used to request access to individual services without re-authenticating. This tool supports multiple authentication methods including password, NTLM hash, AES key, an existing ccache, and certificate-based (PKINIT) authentication.

## Usage

### General

**Syntax:**
```bash
./gettgt -u <user> --dc <DC> -o <ccache> (-p <password> | -H <LM:NT|NT> | --aes-key <hex> | --pfx <file> | --crt <file> --key <file>)
```

**Request a TGT using password credentials:**

```bash
./gettgt -u 'DOMAIN\Administrator' -p 'P@ssw0rd!' --dc dc01.domain.local -o administrator@DOMAIN.LOCAL.ccache
```

**Request a TGT using an NT hash:**

```bash
./gettgt -u 'DOMAIN\Administrator' -H 31d6cfe0d16ae931b73c59d7e0c089c0 --dc dc01.domain.local -o administrator@DOMAIN.LOCAL.ccache
```

**Request a TGT using an AES session key:**

```bash
./gettgt -u 'DOMAIN\Administrator' --aes-key a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2 --dc dc01.domain.local -o administrator@DOMAIN.LOCAL.ccache
```

**Request a TGT via PKINIT using a PFX certificate:**

```bash
./gettgt -u 'DOMAIN\Administrator' --pfx administrator.pfx --dc dc01.domain.local -o administrator@DOMAIN.LOCAL.ccache
```

**Request a TGT via PKINIT using separate PEM certificate and key:**

```bash
./gettgt -u 'DOMAIN\Administrator' --crt administrator.crt --key administrator.key --dc dc01.domain.local -o administrator@DOMAIN.LOCAL.ccache
```
