# Output

Output in Ginpacket tries to be as friendly as possible, but of course not everyone likes the same formats, so some basic customizations were implemented:

## Headers & Footers

Headers are enabled by default. To remove the header (banner/version/target) and footer (usually result counts) and see only raw output from a tool, just discard `stderr`:

```bash
# Linux / MacOS
./tool -t <target> -u <user>@<domain> -p Password [subcommand] 2> /dev/null

# Windows Prompt
./tool.exe -t <target> -u <user>@<domain> -p Password [subcommand] 2>nul

# PowerShell
./tool.exe -t <target> -u <user>@<domain> -p Password [subcommand] 2>$null
```

## Colors

Colors are enabled by default. To remove colors just include the `-Z` / `--no-colors` flag:

```bash
./tool -t <target> -u <user>@<domain> -p <password> -Z
```

## JSON

For tool subcommands that query and return data (instead of performing changes), you can also set `-j` or `--json` to get the result as NDJSON:

```bash
./tool -t <target> -u <user>@<domain> -p <password> --json
```

JSON output is supported by the following tools / subcommands:

```bash
authz info
authz check
cert db
cert pending
cert issued
cert failed
dcsync
dfs list
dfs dump
dfs links
dhcp stats
dns zones
efs query-users
efs query-recovery
efs file-key-info
efs file-key-info-ex
efs query-protectors
efs get-encrypted-metadata
firewall rules
ldap search
lookupsid
lsa privs
lsa trust
lsa forest-trust
lsa policy
lsa accounts
lsa enum-rights
lsa account-rights
perf csets
perf dump
perf cset
perf instances
perf query
printer list
printer drivers
printer ports
printer monitors
printer jobs
reg query
reg enum
reg dump
reg export
rpcdump
sam users
sam groups
server shares
server sessions
server connections
server files
services list
smb shares
tasks list
tasks query
tasks dump
tsts sessions
tsts processes
wksta
wmi query
wmi classes
wmi instances
```
