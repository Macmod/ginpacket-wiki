# 🧾 Registry (reg)

**Protocols**: [MS-RRP](https://winprotocoldoc.z19.web.core.windows.net/MS-RRP/%5bMS-RRP%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
./reg [auth_flags] query <key-path> [-v <value-name>] [--max-allowed]
```

### Enumerate all values under a registry key

```bash
./reg [auth_flags] query '\\dc01\HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
```

### Query a specific named value

```bash
./reg [auth_flags] query '\\dc01\HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion' -v ProductName
```

### Query a key requesting maximum allowed access

```bash
./reg [auth_flags] --max-allowed query '\\dc01\HKLM\SOFTWARE\MyKey'
```

### Syntax

```bash
./reg [auth_flags] add <key-path> -v <value-name> -T <type> -d <data>
```

### Add or overwrite a registry value

```bash
./reg [auth_flags] add '\\dc01\HKLM\SOFTWARE\MyKey' -v MyValue -T REG_SZ -d 'hello'
```

### Syntax

```bash
./reg [auth_flags] delete <key-path> -v <value-name>
```

### Delete a registry value

```bash
./reg [auth_flags] delete '\\dc01\HKLM\SOFTWARE\MyKey' -v MyValue
```

### Syntax

```bash
./reg [auth_flags] get-sd <key-path> [--parse-dacl]
```

### Read the security descriptor of a key

```bash
./reg [auth_flags] get-sd '\\dc01\HKLM\SOFTWARE\MyKey'
```

### Read and parse the DACL of a key's security descriptor

```bash
./reg [auth_flags] get-sd '\\dc01\HKLM\SOFTWARE\MyKey' --parse-dacl
```

### Syntax

```bash
./reg [auth_flags] set-sd <key-path> --sd <hex-sd>
```

### Write a security descriptor to a key

```bash
./reg [auth_flags] set-sd '\\dc01\HKLM\SOFTWARE\MyKey' --sd 01000480200000002c00000000000000
```

### Syntax

```bash
./reg [auth_flags] save <key-path> <remote-path>
```

### Save a hive subtree to a file on the remote host

```bash
./reg [auth_flags] save '\\dc01\HKLM\SAM' 'C:\Windows\Temp\sam.hiv'
```

### Syntax

```bash
./reg [auth_flags] load <key-path> <file>
```

### Load a hive file into a registry key

```bash
./reg [auth_flags] load '\\dc01\HKLM\TempHive' 'C:\Windows\Temp\sam.hiv'
```

### Syntax

```bash
./reg [auth_flags] unload <key-path>
```

### Unload a previously loaded hive

```bash
./reg [auth_flags] unload '\\dc01\HKLM\TempHive'
```

### Syntax

```bash
./reg [auth_flags] info <key-path>
```

### Query key metadata including subkey / value counts and last-write timestamp

```bash
./reg [auth_flags] info '\\dc01\HKLM\SOFTWARE\Microsoft'
```

### Syntax

```bash
./reg [auth_flags] restore <key-path> <file>
```

### Overwrite a live key with the contents of a hive file already on the target

```bash
./reg [auth_flags] restore '\\dc01\HKLM\SOFTWARE\MyKey' 'C:\Windows\Temp\mykey.hiv'
```

### Syntax

```bash
./reg [auth_flags] replace <key-path> -n <new-file> [-b <backup-file>]
```

### Schedule a hive replacement at next boot

```bash
./reg [auth_flags] replace '\\dc01\HKLM\SOFTWARE\MyKey' -n 'C:\Windows\Temp\new.hiv' -b 'C:\Windows\Temp\old.hiv'
```

### Syntax

```bash
./reg [auth_flags] flush <key-path>
```

### Force pending writes for a key to be flushed to the backing store

```bash
./reg [auth_flags] flush '\\dc01\HKLM\SOFTWARE\MyKey'
```

### Syntax

```bash
./reg [auth_flags] export <key-path> -o <file> [-R]
```

### Export a key subtree to a .reg file

```bash
./reg [auth_flags] export '\\dc01\HKLM\SOFTWARE\Microsoft' -o software.reg -R
```

### Syntax

```bash
./reg [auth_flags] import <file>
```

### Import a .reg file into the registry

```bash
./reg [auth_flags] import software.reg
```

### Syntax

```bash
./reg [auth_flags] compare <key-a> <key-b> [-R] [-O <output-mode>]
```

### Compare two registry key subtrees

```bash
./reg [auth_flags] compare '\\dc01\HKLM\SOFTWARE\A' '\\dc01\HKLM\SOFTWARE\B' -R -O od
```

### Syntax

```bash
./reg [auth_flags] copy <src-key> <dst-key> [-R]
```

### Copy a key subtree to another location

```bash
./reg [auth_flags] copy '\\dc01\HKLM\SOFTWARE\A' '\\dc01\HKLM\SOFTWARE\B' -R
```

### Syntax

```bash
./reg [auth_flags] secrets [--sam] [--lsa] [--cache]
```

### Dump SAM, LSA secrets, and cached credentials

```bash
./reg [auth_flags] secrets --sam --lsa --cache
```

### Syntax

```bash
./reg [auth_flags] shell
```


Open an interactive registry shell with persistent connection and cd/ls/get/set/add/del/info/acl  


```bash
./reg [auth_flags] shell
```

### Syntax

```bash
./reg [auth_flags] server-version [--hive <root>]
```

### Query the registry server version (defaults to HKCU)

```bash
./reg [auth_flags] server-version
```

```bash
./reg [auth_flags] server-version --hive HKLM
```
