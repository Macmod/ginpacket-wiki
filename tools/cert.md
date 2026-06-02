# 🪪 Certificates (cert)

**Protocols**: [MS-WCCE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-WCCE/%5bMS-WCCE%5d.pdf), [MS-CSRA](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-CSRA/%5bMS-CSRA%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
./cert [auth_flags] ping <ca-name> [--use-v1]
```

### Verify CA reachability and DCOM/RPC connectivity (Ping2 by default)

```bash
./cert [auth_flags] ping 'CRETA-CA'
```

```bash
./cert [auth_flags] ping 'CRETA-CA' --use-v1
```

### Syntax

```bash
./cert [auth_flags] my-roles <ca-name>
```

### Show effective CA roles for the current principal

```bash
./cert [auth_flags] my-roles 'CRETA-CA'
```

### Syntax

```bash
./cert [auth_flags] ca-info <ca-name>
```

### Show CA version/build/signing-cert metadata

```bash
./cert [auth_flags] ca-info 'CRETA-CA'
```

### Syntax

```bash
./cert [auth_flags] ca-state <ca-name>
```

### Query CA state and whether DB read access is available

```bash
./cert [auth_flags] ca-state 'CRETA-CA'
```

### Syntax

```bash
./cert [auth_flags] ca-unregister-dcom <ca-name>
```


Unregister CA DCOM interfaces (ServerControl flag 1); stops CertSvc - restart to recover  


```bash
./cert [auth_flags] ca-unregister-dcom 'CRETA-CA'
```

### Syntax

```bash
./cert [auth_flags] get-sd|get-ca-sd <ca-name> [--out <file>]
```

### Retrieve the CA security descriptor

```bash
./cert [auth_flags] get-sd 'CRETA-CA' --out ca.sd
```

### Syntax

```bash
./cert [auth_flags] set-sd|set-ca-sd <ca-name> <value> [--hex|--base64]
```

### Set the CA security descriptor from raw bytes file (default mode)

```bash
./cert [auth_flags] set-sd 'CRETA-CA' ca.sd
```

### Set the CA security descriptor from inline base64

```bash
./cert [auth_flags] set-sd 'CRETA-CA' AQAEgCAAAAAsAAAAAAA= --base64
```

### Syntax

```bash
./cert [auth_flags] get-audit <ca-name>
```

### Read the CA audit filter bitmask

```bash
./cert [auth_flags] get-audit 'CRETA-CA'
```

### Syntax

```bash
./cert [auth_flags] set-audit <ca-name> <mask>
```

### Set the CA audit filter (decimal or 0x-prefixed hex)

```bash
./cert [auth_flags] set-audit 'CRETA-CA' 0x1F
```

### Syntax

```bash
./cert [auth_flags] ca-config <ca-name> <node-path> <entry>
```

### Read a persisted CA configuration entry

```bash
./cert [auth_flags] ca-config 'CRETA-CA' PolicyModules\CertificateAuthority_MicrosoftDefault.Policy EnableRequestExtensionList
```

### Syntax

```bash
./cert [auth_flags] set-ca-config <ca-name> <node-path> <entry> <value> [--type <string|dword>]
```

### Write a persisted CA configuration entry

```bash
./cert [auth_flags] set-ca-config 'CRETA-CA' PolicyModules\CertificateAuthority_MicrosoftDefault.Policy EditFlags 0x11014e --type dword
```

### Syntax

```bash
./cert [auth_flags] ca-props <ca-name>
```

### Enumerate CA property metadata (IDs, types, flags, display names)

```bash
./cert [auth_flags] ca-props 'CRETA-CA'
```

### Syntax

```bash
./cert [auth_flags] set-ca-prop <ca-name> <prop-id> <value> [--type <auto|long|string|binary>] [--index <n>] [--file|--base64]
```

### Set selected CA properties (e.g., KRA counts / template list)

```bash
./cert [auth_flags] set-ca-prop 'CRETA-CA' 0x19 4 --type long
```

```bash
./cert [auth_flags] set-ca-prop 'CRETA-CA' 0x1d 'User:1.3.6.1.4.1.311.21.8.1234' --type string
```

### Syntax

```bash
./cert [auth_flags] view-default-columns <ca-name> <pending|issued|failed|extension|attribute|crl|revoked>
```

### Retrieve default CA DB column IDs for a predefined view set

```bash
./cert [auth_flags] view-default-columns 'CRETA-CA' issued
```

### Syntax

```bash
./cert [auth_flags] del-row <ca-name> [row-id] [--table <request|extension|attribute|crl>] [--expired|--pending-failed --before <yyyy-mm-dd>]
```

### Delete one CA DB row by ID

```bash
./cert [auth_flags] del-row 'CRETA-CA' 42 --table request
```

### Bulk delete pending/failed rows older than a cutoff date

```bash
./cert [auth_flags] del-row 'CRETA-CA' --pending-failed --before 2025-01-01
```

### Syntax

```bash
./cert [auth_flags] request <ca-name> [--csr <file>] [--template <name>] [--attrs <k:v;...>] [--out <file>] [--cms] [--include-crls]
```

### Submit a PKCS#10 CSR for enrollment

```bash
./cert [auth_flags] request 'CRETA-CA' --csr user.csr --template User
```

### Submit as CMS/PKCS#7 envelope and save DER certificate

```bash
./cert [auth_flags] request 'CRETA-CA' --csr renewal.p7b --cms --template User --out cert.der
```

### Syntax

```bash
./cert [auth_flags] retrieve <ca-name> [<request-id>] [--serial <hex>] [--out <file>]
```

### Retrieve issuance status/certificate by request ID

```bash
./cert [auth_flags] retrieve 'CRETA-CA' 42 --out cert.der
```

### Retrieve by certificate serial number

```bash
./cert [auth_flags] retrieve 'CRETA-CA' --serial 4a72ef9c2a01
```

### Syntax

```bash
./cert [auth_flags] approve|deny <ca-name> <request-id>
```

### Approve or deny a pending request

```bash
./cert [auth_flags] approve 'CRETA-CA' 42
```

```bash
./cert [auth_flags] deny 'CRETA-CA' 43
```

### Syntax

```bash
./cert [auth_flags] revoke <ca-name> <serial> [--reason <code|name>] [--date <yyyy-mm-dd>]
```

### Revoke an issued certificate

```bash
./cert [auth_flags] revoke 'CRETA-CA' 4a72ef9c2a01 --reason keyCompromise --date 2026-04-01
```

### Syntax

```bash
./cert [auth_flags] check <ca-name> <serial>
```

### Validate a certificate serial against CA revocation/status state

```bash
./cert [auth_flags] check 'CRETA-CA' 4a72ef9c2a01
```

### Syntax

```bash
./cert [auth_flags] publish-crl <ca-name> [--next <yyyy-mm-dd>] [--delta] [--force] [--legacy]
```

### Publish base CRL (default v2 path)

```bash
./cert [auth_flags] publish-crl 'CRETA-CA'
```

### Publish delta CRL and force republish

```bash
./cert [auth_flags] publish-crl 'CRETA-CA' --delta --force
```

### Use legacy v1 PublishCRL path

```bash
./cert [auth_flags] publish-crl 'CRETA-CA' --legacy --next 2026-05-01
```

### Syntax

```bash
./cert [auth_flags] get-crl <ca-name> [--out <file>]
```

### Retrieve current base CRL

```bash
./cert [auth_flags] get-crl 'CRETA-CA' --out ca.crl
```

### Syntax

```bash
./cert [auth_flags] import-cert <ca-name> <file> [--allow-foreign] [--existing-row]
```

### Import certificate material into the CA database

```bash
./cert [auth_flags] import-cert 'CRETA-CA' issued.der --allow-foreign
```

### Syntax

```bash
./cert [auth_flags] import-key <ca-name> <request-id> <pkcs7-file> [--cert-hash <sha1>] [--overwrite]
```

### Import archived key blob (key recovery)

The PKCS#7 EnvelopedData payload must carry an MS-WCCE private key BLOB  
(section 2.2.2.9), encrypted to the current CA exchange certificate.  


```bash
./cert [auth_flags] import-key 'CRETA-CA' 42 keyblob.p7b --overwrite
```

### Syntax

```bash
./cert [auth_flags] set-extension <ca-name> <request-id> <oid> <hex-der> [--type <1|2|3|4>] [--critical] [--disabled]
```

### Set/replace an extension on a pending request

```bash
./cert [auth_flags] set-extension 'CRETA-CA' 42 2.5.29.17 3011820f7777772e6578616d706c652e636f6d --type 3 --critical
```

### Syntax

```bash
./cert [auth_flags] set-attrs <ca-name> <request-id> <attributes> [--file <path>]
```

### Set request attributes from inline text

```bash
./cert [auth_flags] set-attrs 'CRETA-CA' 42 'CertificateTemplate:User\nSAN:dns=www.example.com'
```

### Set request attributes from file

```bash
./cert [auth_flags] set-attrs 'CRETA-CA' 42 dummy --file attrs.txt
```

### Syntax

```bash
./cert [auth_flags] request-attrs|request-exts|request-meta <ca-name> <request-id>
```

### Enumerate request attributes only

```bash
./cert [auth_flags] request-attrs 'CRETA-CA' 42
```

### Enumerate request extensions only

```bash
./cert [auth_flags] request-exts 'CRETA-CA' 42
```

### Show both attributes and extensions

```bash
./cert [auth_flags] request-meta 'CRETA-CA' 42
```

### Syntax

```bash
./cert [auth_flags] restore-paths <ca-name>
```

### Show CA DB/log directories used for restore operations

```bash
./cert [auth_flags] restore-paths 'CRETA-CA'
```

### Syntax

```bash
./cert [auth_flags] officer-rights <ca-name>
```

### Read officer rights configuration

```bash
./cert [auth_flags] officer-rights 'CRETA-CA'
```

### Syntax

```bash
./cert [auth_flags] set-officer-rights <ca-name> (--enable|--disable) [--sd-file <path>]
```

### Enable officer rights and set descriptor from file

```bash
./cert [auth_flags] set-officer-rights 'CRETA-CA' --enable --sd-file officer.sd
```

### Syntax

```bash
./cert [auth_flags] archived-key <ca-name> <request-id> [--out <file>]
```

### Retrieve archived key blob for a request

```bash
./cert [auth_flags] archived-key 'CRETA-CA' 42 --out archived-key.bin
```

### Syntax

```bash
./cert [auth_flags] db <ca-name> [--table <request|extension|attribute|crl>] [--columns c1,c2] [--offset <n>] [--limit <n>] [--format <text|csv|json>] [--use-v1]
```


Read CA database rows with simple paging and optional column projection (EnumViewColumnTable by default)  


```bash
./cert [auth_flags] db 'CRETA-CA' --limit 25
```

```bash
./cert [auth_flags] db 'CRETA-CA' --columns RequestID,RequesterName,Disposition --offset 50 --limit 50
```

```bash
./cert [auth_flags] db 'CRETA-CA' --table extension --limit 25
```

```bash
./cert [auth_flags] db 'CRETA-CA' --format json --limit 25
```

### Legacy v1 metadata path (request table only)

```bash
./cert [auth_flags] db 'CRETA-CA' --use-v1 --limit 25
```

### Syntax

```bash
./cert [auth_flags] requests|pending|issued|failed|revoked <ca-name> [--columns c1,c2] [--offset <n>] [--limit <n>] [--format <text|csv|json>]
```

### Convenience presets for request-table triage

```bash
./cert [auth_flags] pending 'CRETA-CA' --limit 50 --format csv
```

```bash
./cert [auth_flags] issued 'CRETA-CA' --columns RequestID,RequesterName,CommonName --limit 25
```
