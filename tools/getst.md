# 🎟️ Kerberos ST (getst)

**Protocols**: [RFC 4120](https://datatracker.ietf.org/doc/html/rfc4120) / [MS-KILE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-KILE/%5bMS-KILE%5d.pdf) / [MS-SFU](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SFU/%5bMS-SFU%5d.pdf).

Service Tickets (STs) are Kerberos credentials that grant access to a specific service on a specific host. This tool requests them from the KDC using an existing TGT, and supports S4U2Self (impersonating another user) and S4U2Proxy (constrained delegation) - making it useful for both legitimate service access and delegation abuse scenarios.

## Usage

### General

**Syntax:**
```bash
./getst -c <ccache> -s <spn> --dc <DC> -o <out> [-i <user> [--self]] [-a <evidence-ccache>]
```

**Request a service ticket for a given SPN using an existing TGT:**

```bash
./getst -c administrator@DOMAIN.LOCAL.ccache -s cifs/dc01.domain.local --dc dc01.domain.local -o cifs_dc01.ccache
```

**Request a service ticket via S4U2Proxy (impersonating a user):**

```bash
./getst -c sampleuser@DOMAIN.LOCAL.ccache -s cifs/dc01.domain.local -i sampleuser --dc dc01.domain.local -o sampleuser_cifs.ccache
```

**Request an S4U2Self evidence ticket only (no S4U2Proxy):**

```bash
./getst -c sampleuser@DOMAIN.LOCAL.ccache -i sampleuser --self --dc dc01.domain.local -o sampleuser_evidence.ccache
```

**Skip S4U2Self and perform S4U2Proxy directly using a pre-obtained evidence ticket:**

```bash
./getst -c sampleuser@DOMAIN.LOCAL.ccache -s cifs/dc01.domain.local -i sampleuser -a sampleuser_evidence.ccache --dc dc01.domain.local -o sampleuser_cifs.ccache
```
