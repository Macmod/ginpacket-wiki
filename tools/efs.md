# 🛡️ Encrypted Filesystem (efs)

**Protocols**: [MS-EFSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-EFSR/%5bMS-EFSR%5d.pdf).

## Subcommands / Usage

### IMPORTANT: use UNC file paths for remote EFSRPC calls.

Local paths like C:\Temp\file.txt can return ERROR_ACCESS_DENIED.  


```bash
$f='\\WIN-6BKCP1FPPCI\C$\Temp\secret.txt'
```

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] encrypt <file> [--use-v1]
```
{% endhint %}

### Default is EfsRpcEncryptFileExSrv (opnum 21).

```bash
./efs [auth_flags] encrypt $f
```

### Use legacy EfsRpcEncryptFileSrv (opnum 4) on older servers.

```bash
./efs [auth_flags] encrypt $f --use-v1
```

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] decrypt <file>
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] users <file>
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] recovery <file>
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] file-key <file> [--info-class <n>] [--use-v1]
```
{% endhint %}

### Default path uses EfsRpcFileKeyInfoEx (opnum 16) and requires --info-class.

```bash
./efs [auth_flags] file-key $f --info-class 1
```

### Legacy path uses EfsRpcFileKeyInfo (opnum 12).

```bash
./efs [auth_flags] file-key $f --use-v1
```

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] protectors <file>
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] encrypted-metadata <file>
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] set-encrypted-metadata <file> [--blob-b64 <base64>|--blob-hex <hex>]
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] open-raw <file> [--import]
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] del-users <file> --hash <sha1-cert-hash>
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] add-users <file> --users-json <file>
```
{% endhint %}

### users JSON file must be UTF-8 without BOM.

```bash
./efs [auth_flags] add-users $f --users-json users.json
```

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] clone-meta <src> <dst>
```
{% endhint %}

{% hint style="info" %}
**Syntax**

```bash
./efs [auth_flags] flush-cache
```
{% endhint %}

## Notes
> **Compatibility note:** Per MS-EFSR, `file-key` default (`EfsRpcFileKeyInfoEx`, opnum 16), `encrypted-metadata` (opnum 18), and `set-encrypted-metadata` (opnum 19) can legitimately return nonzero and are implementation-specific on many servers. On Server 2022 they commonly return `ERROR_NOT_SUPPORTED`. Use `file-key --use-v1` (opnum 12) when you need stable key-info output. `encrypt` default (`EfsRpcEncryptFileExSrv`, opnum 21) is available on modern Windows and works on Server 2022 with UNC paths. `protectors` (opnum 22) is unavailable on older systems (up to 2012 R2) and may still return `ERROR_NOT_SUPPORTED` depending on implementation/protector support.