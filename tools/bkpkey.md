# 🗝️ Backup Key (bkpkey)

**Protocols**: [MS-BKRP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-BKRP/%5bMS-BKRP%5d.pdf).

The Backup Key Recovery Protocol (MS-BKRP) is used by Windows DPAPI to store and retrieve a domain-wide backup key on the Domain Controller. Possessing this key allows decryption of any DPAPI-protected secret in the domain - including credentials stored by browsers, credential manager, and other applications.

## Usage

### retrieve

**Syntax:**
```bash
./bkpkey [auth_flags] retrieve [-o <out-file>]
```

**Retrieve the domain backup key and write it to a file:**

```bash
./bkpkey [auth_flags] retrieve -o backupkey.bin
```

### encrypt

**Syntax:**
```bash
./bkpkey [auth_flags] encrypt (--in-file <file> | --in-b64 <base64>) [-o <out-file>]  (alias: backup)
```

**Wrap a DPAPI blob using the domain backup key (BACKUPKEY_BACKUP_GUID):**

```bash
./bkpkey [auth_flags] encrypt --in-file request.bin -o response.bin
```

### decrypt

**Syntax:**
```bash
./bkpkey [auth_flags] decrypt (--in-file <file> | --in-b64 <base64>) [-o <out-file>] [--win2k]  (alias: restore)
```

**Unwrap a credential blob using the DC's backup private key:**

```bash
./bkpkey [auth_flags] decrypt --in-file blob.bin
```

**Unwrap using the legacy Win2000-era action (BACKUPKEY_RESTORE_GUID_WIN2K):**

```bash
./bkpkey [auth_flags] decrypt --in-b64 'MIIB...' --win2k
```
