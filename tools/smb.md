# 📂 SMB2/3 (smb)

**Protocols**: [MS-SMB2](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SMB2/%5bMS-SMB2%5d.pdf) (direct TCP/445 - non-RPC).

## Subcommands / Usage

### Syntax

```bash
./smb [auth_flags] shares
```

### List available SMB shares on the target

```bash
./smb [auth_flags] shares
```

### Syntax

```bash
./smb [auth_flags] ls <share[\path]> [-l]
```

### List directory contents of a share

```bash
./smb [auth_flags] ls C$
```

### List with long format (permissions, size, timestamps)

```bash
./smb [auth_flags] ls 'C$\Windows' -l
```

### Syntax

```bash
./smb [auth_flags] tree <share[\path]> [--max-depth <n>]
```

### Recursively print the directory tree of a share

```bash
./smb [auth_flags] tree C$ --max-depth 3
```

### Syntax

```bash
./smb [auth_flags] stat <share[\path]>
```

### Show metadata for a remote file or directory

```bash
./smb [auth_flags] stat 'C$\Windows\System32'
```

### Syntax

```bash
./smb [auth_flags] cat <share[\file]> [--max-bytes <n>]
```

### Print the contents of a remote file to stdout

```bash
./smb [auth_flags] cat 'C$\Windows\win.ini' --max-bytes 1024
```

### Syntax

```bash
./smb [auth_flags] get <share[\remote]> [<local>] [-R]
```

### Download a remote file

```bash
./smb [auth_flags] get 'C$\Temp\file.txt' local.txt
```

### Download a remote directory recursively

```bash
./smb [auth_flags] get 'C$\Temp\Data' local_data -R
```

### Syntax

```bash
./smb [auth_flags] put <local> <share[\remote]> [-R]
```

### Upload a local file to the share

```bash
./smb [auth_flags] put local.txt 'C$\Temp\remote.txt'
```

### Upload a local directory recursively

```bash
./smb [auth_flags] put local_data 'C$\Temp\remote_data' -R
```

### Syntax

```bash
./smb [auth_flags] mkdir <share[\dir]> [--parents]
```

### Create a remote directory

```bash
./smb [auth_flags] mkdir 'C$\Temp\NewDir'
```

### Create a remote directory and any missing parent directories

```bash
./smb [auth_flags] mkdir 'C$\Temp\deep\nested\path' --parents
```

### Syntax

```bash
./smb [auth_flags] rm <share[\path]> [-R]
```

### Remove a remote file

```bash
./smb [auth_flags] rm 'C$\Temp\file.txt'
```

### Remove a remote directory recursively

```bash
./smb [auth_flags] rm 'C$\Temp\Data' -R
```

### Syntax

```bash
./smb [auth_flags] mv <share[\src]> <dst>
```

### Rename or move a remote file or directory within the share

```bash
./smb [auth_flags] mv 'C$\Temp\old.txt' 'Temp\new.txt'
```

### Syntax

```bash
./smb [auth_flags] cp <share[\src]> <dst>
```

### Copy a remote file within the same share

```bash
./smb [auth_flags] cp 'C$\Temp\file.txt' 'Temp\backup.txt'
```

### Syntax

```bash
./smb [auth_flags] -s <share> shell
```

### Start an interactive SMB shell for the share

```bash
./smb [auth_flags] -s C$ shell
```

### Syntax

```bash
./smb [auth_flags] [--require-signing] [--encrypt] [--dialect <ver>] <subcommand>
```

### List share contents with required SMB signing

```bash
./smb [auth_flags] --require-signing ls C$
```

### List with message encryption enabled

```bash
./smb [auth_flags] --encrypt ls C$
```

### Force a specific SMB dialect

```bash
./smb [auth_flags] --dialect 3.1.1 ls C$
```

## Notes
> [!NOTE]
> Recursive operations are supported for `get`, `put`, and `rm` commands. The interactive `shell` command reuses a single connection and supports both remote and local workflow commands.