# Output

Output in Ginpacket tries to be as friendly as possible, but of course not everyone likes the same formats, so some basic customizations were implemented:

## Headers & Footers

Headers and footers are enabled by default. To remove the header (banner/version/target) and footer (usually result counts) and see only raw output from a tool, just discard `stderr`:

```bash
# Linux / macOS
./tool -t <target> -u <user>@<domain> -p Password [subcommand] 2> /dev/null

# Windows Command Prompt
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

{% hint style="info" %}
In some cases, such as the `eventlog`, `cert` and `tasks` tools, the tool has its own `--format` flag. When that happens, `-j` / `--json` is simply an alias of `--format json`.
{% endhint %}

{% hint style="info" %}
If JSON output is not supported by a subcommand, `-j` / `--json` is simply ignored.
{% endhint %}

JSON output is supported by the following tools / subcommands:

```
lookupsid
rpcdump
sam users
sam groups
sam display
sam user
sam group
sam group-members
sam user-groups
sam user-aliases
sam aliases
sam alias
sam alias-members
sam alias-membership
sam domains
sam domain
sam password-policy
sam lookup-names
sam lookup-rids
server info
server aliases
server stats
server disks
server transports
server shares
server sessions
server connections
server files
services query
services dump
services service
services deps
services get-sd
services group
services groups
services display-name
services key-name
wksta loggedon
wksta info
wksta transports
wksta join-info
wksta stats
wksta names
wksta joinable-ous
dcsync
eventlog channels
eventlog publishers
eventlog query
eventlog subscribe
eventlog watch
cert db
cert requests
cert pending
cert issued
cert failed
cert revoked
cert my-roles
cert ca-info
cert ca-props
cert restore-paths
cert request-attrs
cert request-exts
cert request-meta
tasks folders
tasks query
tasks dump
tasks get-sddl
dhcp stats
dhcp stats-v6
dhcp scopes
dhcp scope
dhcp leases
dhcp ranges
dhcp exclusions
dhcp reservations
dhcp options
dhcp option-types
dhcp config
dhcp dump
dns zones
dns zone
dns zone-stats
dns records
dns record
dns nodes
dns dump
dns server
dns server-stats
dns client-subnets
dns client-subnet
dns server-scopes
dns zone-scopes
dns policies
dns policy
firewall rules
firewall profile
firewall config
firewall products
firewall networks
firewall adapters
firewall ipsec-csrules
firewall ipsec-mmrules
firewall ipsec-authsets
firewall ipsec-cryptosets
firewall ipsec-sas
smb shares
smb ls
smb tree
smb stat
lsa trusts
lsa privileges
lsa accounts
lsa rights
lsa account-rights
lsa account-privs
lsa policy
lsa domain-policy
lsa forest-trust
tsts sessions
tsts processes
tsts listeners
printer printers
printer drivers
printer ports
printer monitors
printer server
printer jobs
printer forms
printer processors
printer datatypes
ldap search
ldap query users
ldap query groups
ldap query computers
ldap query containers
ldap query ous
ldap query service-accounts
ldap query gpos
ldap query spns
ldap query unconstrained-delegation
ldap query constrained-delegation
ldap query asreproast
ldap query never-expires
ldap query pwd-not-required
ldap query cert-templates
ldap query cert-authorities
ldap query trusts
ldap query sccm
ldap query wds
ldap query passpol
ldap query mquota
ldap query key-creds
ldap query rbcd
ldap query gmsa
ldap query laps
ldap whoami
ldap info
ldap get-gmsa
ldap get-laps
ldap dacl show
ldap keycred list
wmi query
wmi list-namespaces
wmi list-classes
wmi instance
wmi class
wmi methods
dfs namespaces
dfs dump
dfs links
dfs get-sd
efs users
efs recovery
efs file-key
efs protectors
efs encrypted-metadata
perf csets
perf dump
perf cset
perf instances
perf query
time bits
time source
time status
time provider-status
time provider-config
reg query
reg info
reg get-sd
authz info
authz check sd
authz check registry
authz check smb
authz check ldap
authz check tasks
authz check services
authz check wmi-ns
machinerole
gkdi get-key
gkdi decrypt-laps
bkpkey retrieve
bkpkey backup
bkpkey restore
```
