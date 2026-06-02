# 🗂️ DFS (dfs)

**Protocols**: [MS-DFSNM](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DFSNM/%5bMS-DFSNM%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
./dfs [auth_flags] namespaces
```

### List all DFS namespaces served by the target

```bash
./dfs [auth_flags] namespaces
```

### Syntax

```bash
./dfs [auth_flags] dump
```

### Dump full details for all namespaces and their links

```bash
./dfs [auth_flags] dump
```

### Syntax

```bash
./dfs [auth_flags] links <namespace-path>
```

### Enumerate all links within a namespace

```bash
./dfs [auth_flags] links '\\EXAMPLE.LOCAL\dfs'
```

### Syntax

```bash
./dfs [auth_flags] info <path> [--gen-guid] [--version]
```

### Show full info for a namespace root or link

```bash
./dfs [auth_flags] info '\\EXAMPLE.LOCAL\dfs'
```

### Show info and regenerate the stored GUID for a namespace entry

```bash
./dfs [auth_flags] info '\\EXAMPLE.LOCAL\dfs' --gen-guid
```

### Show the protocol version negotiated for a namespace entry

```bash
./dfs [auth_flags] info '\\EXAMPLE.LOCAL\dfs' --version
```

### Syntax

```bash
./dfs [auth_flags] add-link <link-path> --server <server> -s <share>
```

### Add a new DFS link pointing to a target share

```bash
./dfs [auth_flags] add-link '\\EXAMPLE.LOCAL\dfs\apps' --server FILES01 -s Data
```

### Syntax

```bash
./dfs [auth_flags] del-link <link-path>
```

### Remove a DFS link

```bash
./dfs [auth_flags] del-link '\\EXAMPLE.LOCAL\dfs\apps'
```

### Syntax

```bash
./dfs [auth_flags] move <old-path> <new-path>
```

### Rename/move a DFS link to a new path

```bash
./dfs [auth_flags] move '\\EXAMPLE.LOCAL\dfs\old' '\\EXAMPLE.LOCAL\dfs\new'
```

### Syntax

```bash
./dfs [auth_flags] set-comment <path> -c <text>
```

### Set a descriptive comment on a namespace root or link

```bash
./dfs [auth_flags] set-comment '\\EXAMPLE.LOCAL\dfs\apps' -c 'Application share'
```

### Syntax

```bash
./dfs [auth_flags] set-state <dfs-path> -e <online|offline|resynchronize> [--server <server> -s <share>] [--pdc <dc>] [--use-v1]
```

### Set a link offline

```bash
./dfs [auth_flags] set-state '\\EXAMPLE.LOCAL\dfs\apps' -e offline
```

### Set a link online using the legacy v1 API

```bash
./dfs [auth_flags] set-state '\\EXAMPLE.LOCAL\dfs\apps' -e online --use-v1
```

### Set a specific link target online

```bash
./dfs [auth_flags] set-state '\\EXAMPLE.LOCAL\dfs\apps' --server FILES01 -s Data -e online --pdc dc01.example.com
```

### Trigger resynchronization on a namespace root

```bash
./dfs [auth_flags] set-state '\\EXAMPLE.LOCAL\dfs' -e resynchronize --pdc dc01.example.com
```

### Syntax

```bash
./dfs [auth_flags] set-timeout <dfs-path> -T <sec> [--use-v1]
```

### Set the client referral cache timeout on a link

```bash
./dfs [auth_flags] set-timeout '\\EXAMPLE.LOCAL\dfs\apps' -T 600
```

### Set the client referral timeout using the legacy v1 API

```bash
./dfs [auth_flags] set-timeout '\\EXAMPLE.LOCAL\dfs\apps' -T 300 --use-v1
```

### Syntax

```bash
./dfs [auth_flags] set-flags <dfs-path> -f <flags> [-m <mask>] [--use-v1]
```

### Set DFS flags on a link

```bash
./dfs [auth_flags] set-flags '\\EXAMPLE.LOCAL\dfs\apps' -f 32
```

### Set DFS flags using the legacy v1 API

```bash
./dfs [auth_flags] set-flags '\\EXAMPLE.LOCAL\dfs\apps' -f 8 --use-v1
```

### Set DFS flags with a bitmask (update only the masked bits)

```bash
./dfs [auth_flags] set-flags '\\EXAMPLE.LOCAL\dfs\apps' -f 0 -m 47
```

### Syntax

```bash
./dfs [auth_flags] set-priority <dfs-path> --server <server> -s <share> -c <class> -R <rank> [--use-v1]
```

### Set referral priority class and rank for a link target

```bash
./dfs [auth_flags] set-priority '\\EXAMPLE.LOCAL\dfs\apps' --server FILES01 -s Data -c 1 -R 0
```

### Set referral priority using the legacy v1 API

```bash
./dfs [auth_flags] set-priority '\\EXAMPLE.LOCAL\dfs\apps' --server FILES01 -s Data -c 2 -R 5 --use-v1
```

### Syntax

```bash
./dfs [auth_flags] get-sd <dfs-path>
```

### Read the security descriptor of a namespace root or link

```bash
./dfs [auth_flags] get-sd '\\EXAMPLE.LOCAL\dfs\apps'
```

### Syntax

```bash
./dfs [auth_flags] set-sd <dfs-path> --sd <hex>
```

### Write a security descriptor to a namespace root or link

```bash
./dfs [auth_flags] set-sd '\\EXAMPLE.LOCAL\dfs\apps' --sd '01000480...'
```

### Syntax

```bash
./dfs [auth_flags] dc-address --server <server> [--pdc <dc>]
```

### Query the DFS metadata DC currently used by a DFS server

```bash
./dfs [auth_flags] dc-address --server FILES01
```

### Syntax

```bash
./dfs [auth_flags] set-dc-address --server <server> --pdc <pdc> [--set-timeout -T <seconds>] [-i]
```

### Set the DFS metadata DC for a DFS server (server is required)

```bash
./dfs [auth_flags] set-dc-address --server FILES01 --pdc dc01.example.com
```

### Set metadata DC and explicitly apply timeout value

```bash
./dfs [auth_flags] set-dc-address --server FILES01 --pdc dc01.example.com --set-timeout -T 300
```

### Set metadata DC and request immediate metadata re-sync

```bash
./dfs [auth_flags] set-dc-address --server FILES01 --pdc dc01.example.com -i
```

### Syntax

```bash
./dfs [auth_flags] add-root <dfs-path> [--root-target <\\server\share>] [--new] [--version <0|1|2>] [--use-v1]
```

### Create a new stand-alone DFS namespace

```bash
./dfs [auth_flags] add-root '\\FILES01\dfsroot' --new
```

### Create a new domain-based DFS namespace (v2) with a root target

```bash
./dfs [auth_flags] add-root '\\EXAMPLE.LOCAL\dfs' --root-target '\\FILES01\dfsroot' --version 2 --new
```

### Add a root target to an existing domain-based namespace

```bash
./dfs [auth_flags] add-root '\\EXAMPLE.LOCAL\dfs' --root-target '\\FILES02\dfsroot'
```

### Syntax

```bash
./dfs [auth_flags] del-root <dfs-path> [--root-target <\\server\share>] [--force] [--use-v1]
```

### Delete a stand-alone DFS namespace

```bash
./dfs [auth_flags] del-root '\\FILES01\dfsroot'
```

### Remove a specific root target from a domain-based namespace

```bash
./dfs [auth_flags] del-root '\\EXAMPLE.LOCAL\dfs' --root-target '\\FILES02\dfsroot'
```

### Syntax

```bash
./dfs [auth_flags] initialize
```

### Instruct the DFS server to reload its stored configuration

```bash
./dfs [auth_flags] initialize
```

### Syntax

```bash
./dfs [auth_flags] ns-version [--origin <1|2>]
```

### Query the DFS server's supported namespace versions

```bash
./dfs [auth_flags] ns-version
```

```bash
./dfs [auth_flags] ns-version --origin 2
```

### Syntax

```bash
./dfs [auth_flags] server-version
```

### Query the DFS server version (NetrDfsManagerGetVersion)

```bash
./dfs [auth_flags] server-version
```

### Syntax

```bash
./dfs [auth_flags] flush-ft-table --pdc <dc> --namespace <name>
```

### Purge the domainv1 DFS referral cache entry on a domain controller

```bash
./dfs [auth_flags] flush-ft-table --pdc dc01.example.com --namespace dfs
```

## Notes
> [!IMPORTANT]
> `dfs set-state` uses different valid values depending on what you target:
> - link path only: `ok`, `online`, `offline`
> - namespace root only: `resynchronize`, `standby`, `force-sync`
> - specific target (`--server` + `-s`): `online`, `offline` with target-state semantics
>
> Root paths intentionally reject `online`, `offline`, and `ok` because they commonly fail with `ERROR_INVALID_PARAMETER` on Windows.

Note: Levels 105, 106 and 107 are intentionally not exposed yet due to CLI complexity.