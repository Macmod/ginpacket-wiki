# 🔑 Group Key Distribution (gkdi)

**Protocols**: [MS-GKDI](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-GKDI/%5bMS-GKDI%5d.pdf).

The Group Key Distribution Protocol (MS-GKDI) distributes hierarchical seed keys from a domain controller via the ISDKey RPC interface (UUID `b9785960-524f-11df-8b6d-83dcded72085`). These seed keys are used by DPAPI-NG and Windows LAPS v2 encryption. All communication uses `ncacn_ip_tcp` with mandatory packet privacy (Seal).

## Usage

### get-key

**Syntax:**
```bash
./gkdi [auth_flags] get-key --sd <sddl-or-hex> [--root-key-id <guid>] [--l0 <n>] [--l1 <n>] [--l2 <n>] [--raw]
```

**Retrieve the latest group seed key for a security descriptor:**

```bash
./gkdi [auth_flags] get-key --sd 'O:SYG:SYD:(A;;FA;;;BA)'
```

**Retrieve a seed key for a specific time index:**

```bash
./gkdi [auth_flags] get-key --sd 'O:SYG:SYD:(A;;FA;;;BA)' --l0 100 --l1 31 --l2 -1
```

**Retrieve the latest key from a specific root key:**

```bash
./gkdi [auth_flags] get-key --sd 'O:SYG:SYD:(A;;FA;;;BA)' --root-key-id 'a1b2c3d4-...'
```

**Print only the raw key bytes as hex:**

```bash
./gkdi [auth_flags] get-key --sd 'O:SYG:SYD:(A;;FA;;;BA)' --raw
```

**Flags:**

| Flag | Description |
|------|-------------|
| `--sd` | Security descriptor as SDDL or hex (required) |
| `--root-key-id` | Root key GUID (omit for latest) |
| `--l0` | L0 key index (-1 = latest) |
| `--l1` | L1 key index (-1 = latest) |
| `--l2` | L2 key index (-1 = latest) |
| `--raw` / `-r` | Print only raw key bytes as hex |

### decrypt-laps

**Syntax:**
```bash
./gkdi [auth_flags] decrypt-laps (--blob <base64> | --blob-hex <hex>)
```

**Decrypt an `msLAPS-EncryptedPassword` blob retrieved from AD:**

{% hint style="info" %}
Use `ldap get-laps <computer>` to retrieve the base64-encoded blob from AD first.
{% endhint %}

```bash
./gkdi [auth_flags] decrypt-laps --blob 'MIIB...'
```

```bash
./gkdi [auth_flags] decrypt-laps --blob-hex 'deadbeef...'
```

The command performs the full LAPS v2 decryption chain:
1. Parses the CMS EnvelopedData to extract key indices and target SID
2. Calls GetKey on the DC to retrieve the Group Key Envelope
3. Derives the Key Encryption Key (KEK) via SP800-108 CTR-HMAC
4. Unwraps the Content Encryption Key (CEK) via RFC 3394 AES key unwrap
5. Decrypts the ciphertext via AES-GCM
6. Decodes the UTF-16LE JSON result and extracts the password
