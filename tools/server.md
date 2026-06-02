# 🖥️ Server (server)

**Protocols**: [MS-SRVS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SRVS/%5bMS-SRVS%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
server [auth_flags] shares [--persistent]
```

### List all shares (optionally only persistent ones)

```bash
./server [auth_flags] shares
```

### List only sticky (persistent) shares

```bash
./server [auth_flags] shares --persistent
```

### Syntax

```bash
server [auth_flags] share -s <name>
```

### Show full SHARE_INFO for a named share

```bash
./server [auth_flags] share -s C$
```

### Syntax

```bash
server [auth_flags] share-check <path>
```

### Check whether a local path is already shared

```bash
./server [auth_flags] share-check 'C:\Temp'
```

### Syntax

```bash
server [auth_flags] add-share <name> --path <local> [--remark <text>] [--share-type <n>] [--max-uses <n>] [--persistent=<true|false>]
```

### Create a new share

```bash
./server [auth_flags] add-share TempShare --path 'C:\Temp' --remark 'temporary' --share-type 0 --max-uses 10 --persistent=$false
```

### Syntax

```bash
server [auth_flags] set-share -s <name> [--remark <text>] [--max-uses <n>]
```

### Modify the remark or max-uses on an existing share

```bash
./server [auth_flags] set-share -s TempShare --remark 'renamed share' --max-uses 5
```

### Syntax

```bash
server [auth_flags] del-share -s <name> [--scope <server>] [--use-v1] [--persistent] [--two-phase]
```

### Delete a share using NetrShareDelEx (default, opnum 57)

```bash
./server [auth_flags] del-share -s TempShare
```

### Delete a share using the legacy NetrShareDel (opnum 18)

```bash
./server [auth_flags] del-share -s TempShare --use-v1
```


Clear share persistence only, keeping the runtime share (NetrShareDelSticky, opnum 19)  


```bash
./server [auth_flags] del-share -s TempShare --persistent
```


Delete a share via two-phase commit (NetrShareDelStart + NetrShareDelCommit, opnums 37+38)  


```bash
./server [auth_flags] del-share -s TempShare --two-phase
```

### Delete a scoped share on a named virtual server endpoint

```bash
./server [auth_flags] del-share -s TempShare --scope CLUS1
```

### Syntax

```bash
server [auth_flags] get-file-acl <share[\path]> [--security-info <mask>]
```

### Read the ACL on a file within a share

```bash
./server [auth_flags] get-file-acl SYSVOL
```

```bash
./server [auth_flags] get-file-acl 'SYSVOL\Policies'
```

### Syntax

```bash
server [auth_flags] set-file-acl <share[\path]> --sd <hex> [--security-info <mask>]
```

### Write an ACL to a file within a share

```bash
./server [auth_flags] set-file-acl SYSVOL --sd '01000480200000002c00000000000000'
```

```bash
./server [auth_flags] set-file-acl 'SYSVOL\Policies' --sd '01000480200000002c00000000000000'
```

### Syntax

```bash
server [auth_flags] sessions [--client <name>] [--session-user <user>]
```

### List active SMB sessions

```bash
./server [auth_flags] sessions -c '\\CLIENT' -U 'DOMAIN\user'
```

### Syntax

```bash
server [auth_flags] del-session [--client <name>] [--session-user <user>]
```

### Forcibly disconnect an SMB session

```bash
./server [auth_flags] del-session -c '\\CLIENT'
```

### Syntax

```bash
server [auth_flags] connections [--qualifier <share|client>]
```

### List active share connections

```bash
./server [auth_flags] connections --qualifier '\\CLIENT'
```

### Syntax

```bash
server [auth_flags] files [--base-path <path>] [--session-user <user>]
```

### List open files on the server

```bash
./server [auth_flags] files --base-path 'C:\' -U 'DOMAIN\user'
```

### Syntax

```bash
server [auth_flags] file <id>
```

### Show details for a specific open file by ID

```bash
./server [auth_flags] file 123
```

### Syntax

```bash
server [auth_flags] file-close <id>
```

### Force-close an open file by ID

```bash
./server [auth_flags] file-close 123
```

### Syntax

```bash
server [auth_flags] transports
```

### List all transport bindings registered on the server

```bash
./server [auth_flags] transports
```

### Syntax

```bash
server [auth_flags] add-transport <transport> [-A <addr>] [-d <domain>] [--flags <n>] [--use-v1]
```

### Add a transport binding (level 2, opnum 41)

```bash
./server [auth_flags] add-transport '\Device\NetBT_Tcpip_{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' -A '192.168.1.10'
```

### Add a transport binding with domain/flags at level 2

```bash
./server [auth_flags] add-transport '\Device\NetBT_Tcpip_{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' -d CRETA --flags 0   # level 2 (opnum 41)
```

### Add a transport binding using the legacy NetrServerTransportAdd (opnum 25)

```bash
./server [auth_flags] add-transport '\Device\NetBT_Tcpip_{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --use-v1              # NetrServerTransportAdd (opnum 25)
```

### Syntax

```bash
server [auth_flags] del-transport <transport> [-A <addr>] [-d <domain>] [--use-v1]
```

### Remove a transport binding

```bash
./server [auth_flags] del-transport '\Device\NetBT_Tcpip_{6BFFD098-A112-610E-9FBF-00A0C90D67DA}'
```

### Remove a transport binding using the legacy NetrServerTransportDel (opnum 27)

```bash
./server [auth_flags] del-transport '\Device\NetBT_Tcpip_{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --use-v1              # NetrServerTransportDel (opnum 27)
```

### Syntax

```bash
server [auth_flags] aliases
```

### List server name aliases

```bash
./server [auth_flags] aliases
```

### Syntax

```bash
server [auth_flags] add-alias <name> --alias-target <server>
```

### Register a new server name alias

```bash
./server [auth_flags] add-alias TESTDC --alias-target WIN-6BKCP1FPPCI
```

### Syntax

```bash
server [auth_flags] del-alias -a <name> [--alias-target <server>]
```

### Remove a server name alias

```bash
./server [auth_flags] del-alias -a TESTDC --alias-target WIN-6BKCP1FPPCI
```

### Syntax

```bash
server [auth_flags] validate-name <name> <type>
```

### Validate a name against a specific type (share, workgroup, etc.)

```bash
./server [auth_flags] validate-name SYSVOL share
```

### Syntax

```bash
server [auth_flags] info [--detail <basic|standard|full|extended|config|config-full>]
```

### Query server configuration at a given info detail (default: full)

```bash
./server [auth_flags] info --detail full
```

### Syntax

```bash
server [auth_flags] set-server <remark>
```

### Update the server's description/remark string

```bash
./server [auth_flags] set-server 'My DC'
```

### Syntax

```bash
server [auth_flags] stats
```

### Query server service statistics

```bash
./server [auth_flags] stats
```

### Syntax

```bash
server [auth_flags] disks
```

### List available disk drives on the server

```bash
./server [auth_flags] disks
```
