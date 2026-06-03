# 🛡️ Encrypted Filesystem (efs)

**Protocols**: [MS-EFSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-EFSR/%5bMS-EFSR%5d.pdf).

The Encrypting File System Remote Protocol (MS-EFSR) supports remote management of encrypted files on Windows. It allows users and administrators to perform operations on encrypted data across the network, such as backing up and restoring EFS keys, or managing encrypted files on remote file servers.

## Usage

### encrypt

**Syntax:**
```bash
./efs [auth_flags] encrypt <file> [--use-v1]
```

**Default is EfsRpcEncryptFileExSrv (opnum 21).:**

```bash
./efs [auth_flags] encrypt '\\TARGET\C$\Temp\secret.txt'
```

**Use legacy EfsRpcEncryptFileSrv (opnum 4) on older servers.:**

```bash
./efs [auth_flags] encrypt '\\TARGET\C$\Temp\secret.txt' --use-v1
```

### decrypt

**Syntax:**
```bash
./efs [auth_flags] decrypt <file>
```

### users

**Syntax:**
```bash
./efs [auth_flags] users <file>
```

### recovery

**Syntax:**
```bash
./efs [auth_flags] recovery <file>
```

### file-key

**Syntax:**
```bash
./efs [auth_flags] file-key <file> [--info-class <n>] [--use-v1]
```

**Default path uses EfsRpcFileKeyInfoEx (opnum 16) and requires --info-class.:**

```bash
./efs [auth_flags] file-key '\\TARGET\C$\Temp\secret.txt' --info-class 1
```

**Legacy path uses EfsRpcFileKeyInfo (opnum 12).:**

```bash
./efs [auth_flags] file-key '\\TARGET\C$\Temp\secret.txt' --use-v1
```

### protectors

**Syntax:**
```bash
./efs [auth_flags] protectors <file>
```

### encrypted-metadata

**Syntax:**
```bash
./efs [auth_flags] encrypted-metadata <file>
```

### set-encrypted-metadata

**Syntax:**
```bash
./efs [auth_flags] set-encrypted-metadata <file> [--blob-b64 <base64>|--blob-hex <hex>]
```

### open-raw

**Syntax:**
```bash
./efs [auth_flags] open-raw <file> [--import]
```

### del-users

**Syntax:**
```bash
./efs [auth_flags] del-users <file> --hash <sha1-cert-hash>
```

### add-users

**Syntax:**
```bash
./efs [auth_flags] add-users <file> --users-json <file>
```

**users JSON file must be UTF-8 without BOM.:**

```bash
./efs [auth_flags] add-users '\\TARGET\C$\Temp\secret.txt' --users-json users.json
```

### clone-meta

**Syntax:**
```bash
./efs [auth_flags] clone-meta <src> <dst>
```

### flush-cache

**Syntax:**
```bash
./efs [auth_flags] flush-cache
```

## Notes
{% hint style="warning" %}
Use UNC file paths for remote EFSRPC calls. Local paths like C:\Temp\file.txt can return `ERROR_ACCESS_DENIED`.
{% endhint %}



{% hint style="info" %}
Per MS-EFSR, `file-key` default (`EfsRpcFileKeyInfoEx`, opnum 16), `encrypted-metadata` (opnum 18), and `set-encrypted-metadata` (opnum 19) can legitimately return nonzero and are implementation-specific on many servers. On Server 2022 they commonly return `ERROR_NOT_SUPPORTED`. Use `file-key --use-v1` (opnum 12) when you need stable key-info output. `encrypt` default (`EfsRpcEncryptFileExSrv`, opnum 21) is available on modern Windows and works on Server 2022 with UNC paths. `protectors` (opnum 22) is unavailable on older systems (up to 2012 R2) and may still return `ERROR_NOT_SUPPORTED` depending on implementation/protector support.
{% endhint %}