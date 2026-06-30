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

### TGT Renewal

**Syntax:**
```bash
./getst --renew -c <tgt.ccache> [--dc <DC>] [-o <out.ccache>]
```

**Renew an existing TGT (instead of requesting a service ticket):**

{% hint style="info" %}
Output defaults to `<input>_renewed.ccache` when `-o` is not specified.
{% endhint %}

```bash
./getst --renew -c administrator@DOMAIN.LOCAL.ccache --dc dc01.domain.local
```

```bash
./getst --renew -c administrator@DOMAIN.LOCAL.ccache --dc dc01.domain.local -o renewed.ccache
```

{% hint style="warning" %}
**Cross-realm note**: when the target service is in a different realm (external or forest trust), always use the fully-qualified hostname in the SPN (e.g. `cifs/server.foreign.realm` rather than `cifs/server`). The cross-realm fallback derives the target realm from the hostname suffix; a short name provides no suffix and the fallback is skipped, causing the request to fail with `KDC_ERR_S_PRINCIPAL_UNKNOWN`.
{% endhint %}
