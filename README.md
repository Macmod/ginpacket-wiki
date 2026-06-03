# Ginpacket

﻿🍸 Ginpacket is a collection of Go tools for working with Windows / Active Directory network protocols. The philosophy is to provide a **simple** and **comprehensive** command-line interface to complex but useful protocol operations, turning researching & interacting with these protocols a simpler task.

The tools span a range of use cases, including:

- **Authentication and credentials**: obtain Kerberos tickets (`gettgt`, `getst`), replicate directory secrets (`dcsync`), retrieve DPAPI backup keys (`bkpkey`), and change passwords (`changepwd`).
- **Directory and identity services**: query and modify AD objects (`ldap`), enumerate accounts and groups (`sam`), manage LSA policy and secrets (`lsa`), resolve SIDs and names (`lookupsid`), and inspect machine domain roles (`machinerole`).
- **Network infrastructure**: manage DNS zones and records (`dns`), DHCP scopes and leases (`dhcp`), DFS namespaces (`dfs`), firewall rules (`firewall`), and certificate authorities (`cert`).
- **Host management**: interact with the registry (`reg`), services (`services`), scheduled tasks (`tasks`), WMI (`wmi`), EFS (`efs`), printers (`printer`), SMB shares and files (`smb`), server shares (`server`), initiate remote shutdowns (`shutdown`).
- **System observability**: read event logs (`eventlog`), query performance counters (`perf`), inspect Terminal Services sessions (`tsts`), probe workstation state (`wksta`), check W32Time (`time`), and enumerate RPC endpoints (`rpcdump`).
- **Authorization**: simulate access checks against security descriptors (`authz`).

Most subcommands map directly to a single protocol operation or RPC call - what you pass on the command line is what gets sent on the wire. A small number chain multiple calls to implement higher-level actions (for example, `dcsync`, `reg secrets`, and `sam dump`, `changepwd` etc).

{% hint style="info" %}
Despite the name, [ginpacket](https://github.com/Macmod/ginpacket) is **not** a Go port of [impacket](https://github.com/fortra/impacket). It is an opinionated toolkit with independently reworked implementations of some features that overlap with impacket, as well as implementations that go beyond what impacket provides. The two projects share goals but differ in scope and design.
{% endhint %}

# Protocols implemented
* Kerberos ([RFC 4120](https://datatracker.ietf.org/doc/html/rfc4120) and [MS-KILE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-KILE/%5bMS-KILE%5d.pdf))
	* PKINIT ([MS-PKCA](https://winprotocoldoc.z19.web.core.windows.net/MS-PKCA/%5bMS-PKCA%5d.pdf) and [RFC 4556](https://datatracker.ietf.org/doc/html/rfc4556))
	* S4U ([MS-SFU](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SFU/%5bMS-SFU%5d.pdf))
	* Change / set password ([RFC 3244](https://datatracker.ietf.org/doc/html/rfc3244))
* SMB2/3 ([MS-SMB2](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SMB2/%5bMS-SMB2%5d.pdf))
* LDAP ([RFC 4511](https://datatracker.ietf.org/doc/html/rfc4511) and parts of [MS-ADTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-ADTS/%5bMS-ADTS%5d.pdf))
* MSRPC ([MS-RPCE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-RPCE/%5bMS-RPCE%5d.pdf))
	* Endpoint mapper
	* Directory Replication Service ([MS-DRSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DRSR/%5bMS-DRSR%5d.pdf))
	* Remote Authorization API ([MS-RAA](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-raa/))
	* Remote Registry ([MS-RRP](https://winprotocoldoc.z19.web.core.windows.net/MS-RRP/%5bMS-RRP%5d.pdf))
	* Service Control Manager ([MS-SCMR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SCMR/%5bMS-SCMR%5d.pdf))
	* Task Scheduler ([MS-TSCH](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-TSCH/%5bMS-TSCH%5d.pdf))
	* EventLog Remoting v6 ([MS-EVEN6](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-EVEN6/%5bMS-EVEN6%5d.pdf))
	* Certificate Services Administration and Enrollment ([MS-CSRA](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-CSRA/%5bMS-CSRA%5d.pdf) and [MS-WCCE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-WCCE/%5bMS-WCCE%5d.pdf))
	* Terminal Services Terminal Server Runtime Interface ([MS-TSTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-TSTS/%5bMS-TSTS%5d.pdf))
	* Windows Management Instrumentation ([MS-WMI](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-WMI/%5bMS-WMI%5d.pdf) and [MS-DCOM](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DCOM/%5bMS-DCOM%5d.pdf))
	* Security Accounts Manager ([MS-SAMR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SAMR/%5bMS-SAMR%5d.pdf))
	* LSA ([MS-LSAD](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-LSAD/%5bMS-LSAD%5d.pdf) and [MS-LSAT](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-LSAT/%5bMS-LSAT%5d.pdf))
	* Backup Key Retrieval ([MS-BKRP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-BKRP/%5bMS-BKRP%5d.pdf))
	* Server Service ([MS-SRVS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SRVS/%5bMS-SRVS%5d.pdf))
	* Workstation Service ([MS-WKST](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-WKST/%5bMS-WKST%5d.pdf))
	* DFS Namespace Management ([MS-DFSNM](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DFSNM/%5bMS-DFSNM%5d.pdf))
	* Encrypting File System Remote ([MS-EFSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-EFSR/%5bMS-EFSR%5d.pdf))
	* DNS Server Management ([MS-DNSP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DNSP/%5bMS-DNSP%5d.pdf))
	* DHCP Server Management ([MS-DHCPM](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DHCPM/%5bMS-DHCPM%5d.pdf))
	* Firewall and Advanced Security ([MS-FASP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-FASP/%5bMS-FASP%5d.pdf))
	* Print System Remote ([MS-RPRN](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-RPRN/%5bMS-RPRN%5d.pdf))
	* Directory Services Setup ([MS-DSSP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DSSP/%5bMS-DSSP%5d.pdf))
	* Remote Shutdown ([MS-RSP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-RSP/%5bMS-RSP%5d.pdf))
	* Performance Counter Query ([MS-PCQ](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-PCQ/%5bMS-PCQ%5d.pdf))
	* Windows Time Service ([MS-W32T](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-W32T/%5bMS-W32T%5d.pdf))

For a complete reference of the commands supported by Ginpacket's tools, check the subcommands map below or the usage examples for the specific [tools](https://ginpacket.gitbook.io/docs/tools/tools) you intend to use.


# Subcommands Map

Index of provided tools, subcommands & key arguments:

ginpacket/
+- authz
│  ├─ version
│  ├─ info                     <SID|NAME> [--class <all|user|groups|restricted|device-groups|user-claims|device-claims>]
│  ├─ check
│  │  ├─ [common flags]        --desired-access --principal-self --device -O/--object-types -P/--privileges --print-sd
│  │  ├─ sd                    <SID|NAME> -T <hex-sd|sddl> [common check flags]
│  │  ├─ ldap                  <SID|NAME> -T <distinguished-name> [--ldap-scheme <ldap|ldaps>] [--ldap-starttls] [common check flags]
│  │  ├─ services              <SID|NAME> -T <service-name> [common check flags]
│  │  ├─ tasks                 <SID|NAME> -T <task-path> [--task-folder] [common check flags]
│  │  ├─ registry              <SID|NAME> -T <registry-path> [common check flags]
│  │  ├─ smb                   <SID|NAME> -T <share|share\\path> [common check flags]
│  │  ├─ wmi-ns                <SID|NAME> -T <namespace> [common check flags]
+- gettgt                      -u <user> --dc <DC> -o <ccache> (-p <password> | -H <LM:NT|NT> | --aes-key <hex> | --pfx <file> | --crt <file> --key <file>)
+- getst                       -c <ccache> -s <spn> --dc <DC> -o <out> [-i <user> [--self]] [-a <evidence-ccache>]
+- changepwd
│  ├─ samr                     -a <account> -w <new-password> [-o <old-password>] [-T <smb|tcp>]
│  ├─ ldap                     -a <account> -w <new-password> [--scheme <ldap|ldaps>] [--starttls]
│  ├─ adws                     -a <account> -w <new-password>
│  ├─ kpasswd                  -a <account> -w <new-password> [-o <old-password>]
+- smb
│  ├─ shares                   
│  ├─ ls                       <share[\path]> [-l]
│  ├─ tree                     <share[\path]> [--max-depth <n>]
│  ├─ stat                     <share[\path]>
│  ├─ cat                      <share[\file]> [--max-bytes <n>]
│  ├─ get                      <share[\remote]> [<local>] [-R]
│  ├─ put                      <local> <share[\remote]> [-R]
│  ├─ mkdir                    <share[\dir]> [--parents]
│  ├─ rm                       <share[\path]> [-R]
│  ├─ mv                       <share[\src]> <dst>
│  ├─ cp                       <share[\src]> <dst>
│  ├─ shell                    -s <share>
+- ldap
│  ├─ whoami                   
│  ├─ info                     <dn-or-name> [--all]
│  ├─ search                   -F <filter> [-A <attrs>] [--hex] [--limit <n>] [--base-dn <dn>] [--scope <scope>]
│  ├─ modify                   <dn> --attr <name> --operation <add|replace|delete> --value <value>
│  ├─ query                    [-A <attrs>] [--hex] [--limit <n>] (flags apply to all subcommands)
│  │  ├─ users                 [--enabled] [--disabled]
│  │  ├─ groups                
│  │  ├─ computers             
│  │  ├─ containers            
│  │  ├─ ous                   
│  │  ├─ service-accounts (svcs)
│  │  ├─ gpos                  
│  │  ├─ spns                  
│  │  ├─ unconstrained-delegation (unconst)
│  │  ├─ constrained-delegation (const)
│  │  ├─ asreproast            
│  │  ├─ never-expires         
│  │  ├─ pwd-not-required      
│  │  ├─ cert-templates        
│  │  ├─ cert-authorities      
│  │  ├─ trusts                
│  ├─ create
│  │  ├─ user                  --name <cn> [--pass <password>] [--enabled] [--parent-dn <dn>] [--scheme ldaps|ldap] [--starttls]
│  │  ├─ computer              --name <cn> [--pass <password>] [--parent-dn <dn>] [--scheme ldaps|ldap] [--starttls]
│  │  ├─ group                 --name <cn> [--type <GlobalSecurity|...>] [--parent-dn <dn>]
│  │  ├─ ou                    --name <name> [--parent-dn <dn>]
│  │  ├─ container             --name <name> [--parent-dn <dn>]
│  │  ├─ custom                --template <file.yaml>
+- rpcdump                     [-U <interface-uuid>] [-T <ncacn_ip_tcp,ncacn_np>]
+- reg
│  ├─ query                    <registry-path> [-v <value-name>] [-s]
│  ├─ info                     <registry-path>
│  ├─ add                      <registry-path> -v <value-name> -T <type> -d <data>
│  ├─ set                      <registry-path> -v <value-name> -T <type> -d <data>
│  ├─ delete                   <registry-path> [-v <value-name>]
│  ├─ copy                     <source-path> <destination-path> [-R]
│  ├─ compare                  <source-path> <destination-path> [-R] [-O <format>]
│  ├─ export                   <registry-path> -o <file> [-R]
│  ├─ import                   <file>
│  ├─ save                     <registry-path> <file>
│  ├─ restore                  <registry-path> <file>
│  ├─ replace                  <registry-path> -f <new-file> [-b <backup-file>]
│  ├─ load                     <mount-path> <file>
│  ├─ unload                   <mount-path>
│  ├─ flush                    <key>
│  ├─ get-sd                   <registry-path> [--parse-dacl]
│  ├─ set-sd                   <registry-path> --sd <hex-sd>
│  ├─ secrets                  [--sam] [--lsa] [--cache]
│  ├─ server-version           [--hive <HKLM|HKCU|HKCR|HKU|HKCC>]
│  ├─ shell                    (interactive: ls, cd, get, set, add, del, info, acl, flush)
+- services
│  ├─ query                    [--type <mask>] [--state <mask>] [--group <name>]
│  ├─ dump                     [--type <mask>] [--state <mask>] [--group <name>]
│  ├─ service                  <name> [--use-v1]
│  ├─ get-sd                   <name> [--parse-dacl]
│  ├─ translate                (-K <svc-key> | -N <display-name>)
│  ├─ group                    <name>
│  ├─ enum-deps                <name>
│  ├─ add-service              <name> <binpath> [-N <display-name>] [-T <start-type>] [--service-type <own|share|kernel|filesys>] [--error-control <ignore|normal|severe|critical>] [--wow64] [--wow-type <i386|amd64|arm64|hex>]
│  ├─ set-service              <name> [-N <display-name>] [-b <binpath>] [-T <start-type>] [-a <account>] [--svc-password <password>]
│  ├─ start                    <name> [--arg <value> (repeatable)]
│  ├─ stop                     <name> [--reason <hex>] [--planned] [--comment <text>]
│  ├─ set-failure              <name> [-F <command>] [--reset-period <sec>] [--reboot-message <text>] [--failure-actions <none|restart|reboot|run>]
│  ├─ set-sd                   <name> --sd <hex>
│  ├─ del-service              <name>
+- tasks
│  ├─ query                    [-P <path>] [--include-hidden] [--use-v1]
│  ├─ task                     <path> [--format xml]
│  ├─ folders                  [path]
│  ├─ xml                      <path>
│  ├─ instances                <path>
│  ├─ missed-runs              <path>
│  ├─ dump                     [--include-hidden]
│  ├─ add                      <path> -X <task-xml> [--use-v1]
│  ├─ add-folder               <path>
│  ├─ rename                   <path> <new-path>
│  ├─ run                      <path>
│  ├─ enable                   <path>
│  ├─ disable                  <path>
│  ├─ get-sddl                 <path>
│  ├─ set-sddl                 <path> --sddl <text>
│  ├─ stop                     <path> [--instance <guid>]
│  ├─ del                      <path> [--use-v1]
│  ├─ del-folder               <path>
+- eventlog
│  ├─ query                    <channel> [-q <query>] [-L <n>] [--timeout-ms <ms>]
│  ├─ subscribe                <channel> [-q <query>] [-L <n>] [--timeout-ms <ms>]
│  ├─ watch                    <channel> [-q <query>] [-F <text|json>] [-L <n>] [--timeout-ms <ms>]
│  ├─ channels                 
│  ├─ publishers               
│  ├─ export                   <channel> <out-path> [-q <query>]
│  ├─ clear                    <channel> [-b <backup-path>] [--confirm]
│  ├─ channel                  [<channel>] [-T config|meta|all]
│  ├─ publisher                <name>
│  ├─ channel-publishers       [<channel>]
│  ├─ classic-name             <name>
│  ├─ set-channel              [<channel>] [--enabled <true|false>] [--max-size <bytes>]
+- cert
│  ├─ ping                     <ca-name> [--use-v1]
│  ├─ my-roles                 <ca-name>
│  ├─ ca-info                  <ca-name>
│  ├─ ca-state                 <ca-name>
│  ├─ ca-unregister-dcom       <ca-name>
│  ├─ get-sd|get-ca-sd         <ca-name> [--out <file>]
│  ├─ set-sd|set-ca-sd         <ca-name> <value> [--hex|--base64]
│  ├─ get-audit                <ca-name>
│  ├─ set-audit                <ca-name> <mask>
│  ├─ ca-config                <ca-name> <node-path> <entry>
│  ├─ set-ca-config            <ca-name> <node-path> <entry> <value> [--type <string|dword>]
│  ├─ ca-props                 <ca-name>
│  ├─ set-ca-prop              <ca-name> <prop-id> <value> [--type <auto|long|string|binary>] [--index <n>] [--file|--base64]
│  ├─ view-default-columns     <ca-name> <pending|issued|failed|extension|attribute|crl|revoked>
│  ├─ request                  <ca-name> [--csr <file>] [--template <name>] [--attrs <k:v;...>] [--out <file>] [--cms]
│  ├─ retrieve                 <ca-name> [<request-id>] [--serial <hex>] [--out <file>]
│  ├─ approve                  <ca-name> <request-id>
│  ├─ deny                     <ca-name> <request-id>
│  ├─ revoke                   <ca-name> <serial> [--reason <code|name>] [--date <yyyy-mm-dd>]
│  ├─ check                    <ca-name> <serial>
│  ├─ publish-crl              <ca-name> [--next <yyyy-mm-dd>] [--delta] [--force] [--legacy]
│  ├─ get-crl                  <ca-name> [--out <file>]
│  ├─ import-cert              <ca-name> <file> [--allow-foreign] [--existing-row]
│  ├─ import-key               <ca-name> <request-id> <pkcs7-file> [--cert-hash <sha1>] [--overwrite]
│  ├─ set-extension            <ca-name> <request-id> <oid> <hex-der> [--type <1|2|3|4>] [--critical] [--disabled]
│  ├─ set-attrs                <ca-name> <request-id> <attributes> [--file <path>]
│  ├─ request-attrs            <ca-name> <request-id>
│  ├─ request-exts             <ca-name> <request-id>
│  ├─ request-meta             <ca-name> <request-id>
│  ├─ restore-paths            <ca-name>
│  ├─ officer-rights           <ca-name>
│  ├─ set-officer-rights       <ca-name> [--enable|--disable] [--sd-file <path>]
│  ├─ archived-key             <ca-name> <request-id> [--out <file>]
│  ├─ db                       <ca-name> [--table <request|extension|attribute|crl>] [--columns c1,c2] [--offset <n>] [--limit <n>] [--format <text|csv|json>] [--use-v1]
│  ├─ requests                 <ca-name> [--columns c1,c2] [--offset <n>] [--limit <n>] [--format <text|csv|json>] [--use-v1]
│  ├─ pending                  <ca-name> [--columns c1,c2] [--offset <n>] [--limit <n>] [--format <text|csv|json>] [--use-v1]
│  ├─ issued                   <ca-name> [--columns c1,c2] [--offset <n>] [--limit <n>] [--format <text|csv|json>] [--use-v1]
│  ├─ failed                   <ca-name> [--columns c1,c2] [--offset <n>] [--limit <n>] [--format <text|csv|json>] [--use-v1]
│  ├─ revoked                  <ca-name> [--columns c1,c2] [--offset <n>] [--limit <n>] [--format <text|csv|json>] [--use-v1]
│  ├─ del-row                  <ca-name> [row-id] [--table <request|extension|attribute|crl>] [--expired|--pending-failed --before <yyyy-mm-dd>]
+- tsts
│  ├─ sessions                 [-s <state>] [-f <username>]
│  ├─ processes                [-s <session-id>]
│  ├─ policy
│  ├─ session                  <id> [-c] [-g]
│  ├─ watch                    [-e <create,delete,rename,connect,disconnect,logon,logoff,statechange|all>]
│  ├─ listeners
│  ├─ connect                  <src-session> <dst-session> [-P <target-password>]
│  ├─ message                  <session-id> -T <title> -m <text> [-s <style>] [-o <seconds>] [-a]
│  ├─ kill-session             <id> [-w]
│  ├─ logoff                   <session-id>
│  ├─ disconnect               <session-id> [-w]
│  ├─ kill-process             <pid> [-e <exit-code>]
│  ├─ stop-listener            <name>
│  ├─ start-listener           <name>
│  ├─ shutdown                 [-r] [-P] [-l]
+- wmi
│  ├─ query                    [-n <namespace>] <wql> [-f <fields>] [-L <n>]
│  ├─ namespaces               [-n <namespace>]
│  ├─ classes                  [-n <namespace>] [--superclass <str>] [-L <n>]
│  ├─ instance                 [-n <namespace>] <object-path>
│  ├─ class                    [-n <namespace>] <class>
│  ├─ methods                  [-n <namespace>] <class>
│  ├─ exec                     [-n <namespace>] <command>
│  ├─ invoke                   [-n <namespace>] <object::method> [--arg <k=v>]
│  ├─ del-instance             [-n <namespace>] <object-path>
+- sam
│  ├─ domains
│  ├─ domain                   [-d <name>]
│  ├─ set-domain               [-d <name>] [--min-pwd-len <n>] [--lockout-threshold <n>] [--lockout-window <dur>] [--lockout-duration <dur>]
│  ├─ password-policy          [-d <name>]
│  ├─ get-acl                  [-d <name>]
│  ├─ set-acl                  --sd <hex> [-d <name>]
│  ├─ users                    [-d <name>]
│  ├─ display                  [-d <name>] [--type <users|machines|groups>] [--prefix <str>]
│  ├─ user                     <username|RID> [-d <name>]
│  ├─ add-user                 <name> [-d <name>] [-N <s>] [-D <s>] [-w <s>] [--disable]
│  ├─ del-user                 <username|RID> [-d <name>]
│  ├─ set-user                 <username|RID> [-d <name>] [-N <s>] [-D <s>] [-w <s>] [-e <RFC3339|never>] [--uac-set <flag>] [--uac-clear <flag>]
│  ├─ user-groups              <username|RID> [-d <name>]
│  ├─ user-aliases             <username|RID> [-d <name>]
│  ├─ validate-password        <password> [-d <name>] [-O <auth|change|reset>] [--account <s>]
│  ├─ groups                   [-d <name>]
│  ├─ group                    <name|RID> [-d <name>]
│  ├─ add-group                <name> [-d <name>]
│  ├─ del-group                <name|RID> [-d <name>]
│  ├─ group-members            <name|RID> [-d <name>] [--resolve-sids]
│  ├─ add-group-member         <group> <member> [-d <name>]
│  ├─ del-group-member         <group> <member> [-d <name>]
│  ├─ set-group                <name|RID> [-d <name>] [--name <s>] [--description <s>]
│  ├─ set-member-attrs         <group> <member> [-d <name>] [--attributes <hex>]
│  ├─ aliases                  [-d <name>] [--builtin]
│  ├─ alias                    <name|RID> [-d <name>] [--builtin]
│  ├─ add-alias                <name> [-d <name>]
│  ├─ del-alias                <name|RID> [-d <name>] [--builtin]
│  ├─ alias-members            <name|RID> [-d <name>] [--builtin] [--resolve-sids]
│  ├─ alias-membership         <sid> [-d <name>] [--builtin]
│  ├─ add-alias-member         <alias> <sid|username> [-d <name>] [--builtin]
│  ├─ del-alias-member         <alias> <sid|username> [-d <name>] [--builtin]
│  ├─ add-alias-members        <alias> <sid|username>... [-d <name>] [--builtin]
│  ├─ del-alias-members        <alias> <sid|username>... [-d <name>] [--builtin]
│  ├─ set-alias                <name|RID> [-d <name>] [--builtin] [--name <s>] [--description <s>]
│  ├─ purge-sid                <sid> [-d <name>] [--builtin]
│  ├─ lookup-names             <name>... [-d <name>]
│  ├─ lookup-rids              <rid>... [-d <name>]
│  ├─ rid-to-sid               <rid>
│  ├─ set-dsrm-password        <new-password>
+- lsa                         [--use-tcp]
│  ├─ policy             
│  ├─ domain-policy      
│  ├─ get-sd                   [--security-info <mask>]
│  ├─ set-sd                   --sd <hex> [--security-info <mask>]
│  ├─ privileges               
│  ├─ lookup-priv              <priv-name>
│  ├─ priv-name                --high <n> --low <n>
│  ├─ accounts                 
│  ├─ rights                   [-r <right,right,...>]
│  ├─ account-rights           <sid>
│  ├─ account-privs            <sid>
│  ├─ account-access           <sid>
│  ├─ set-account-access       <sid> <access>
│  ├─ add-rights               <sid> -r <right,right,...>
│  ├─ del-rights               <sid> -r <right,right,...>
│  ├─ add-account              <sid>
│  ├─ del-account              <sid>
│  ├─ add-secret               <name>
│  ├─ get-secret               <name>
│  ├─ secret                   <name>
│  ├─ set-secret               <name> -v <hex>
│  ├─ del-secret               <name>
│  ├─ trusts                   [--use-v1]
│  ├─ trust-records            <domain>
│  ├─ trust                    (-n <domain> | -s <sid>) [--use-v1]
│  ├─ set-trust                (-n <domain> | -s <sid>) [-D <n>] [-T <n>] [--attributes <hex>]
│  ├─ add-trust                -n <domain> --flat-name <name> -s <sid> [-w <secret>] [-D <n>] [-T <n>]
│  ├─ del-trust                <sid>
│  ├─ set-trust-records        <domain> [--check]
│  ├─ set-audit                [--enable] [--disable] [--event <cat=none|success|failure|both>]
│  ├─ set-domain-policy        [--max-service-ticket <dur>] [--max-tgt <dur>] [--max-renew <dur>] [--max-skew <dur>] [--validate-client] [--no-validate-client]
+- lookupsid                   (-s <sid> | -n <name> | -D <domain-sid> -F <start-rid> -T <end-rid>) [--use-v1]
+- bkpkey
│  ├─ backup                   --in-file <request.bin> -o <response.bin>
│  ├─ restore                  (--in-file <restore.bin> | --in-b64 <base64>) [--win2k]
│  ├─ retrieve                 -o <backupkey.bin>
+- dfs
│  ├─ namespaces               
│  ├─ dump                     
│  ├─ links                    <namespace-path>
│  ├─ info                     <path> [--gen-guid] [--version]
│  ├─ add-link                 <link-path> --server <server> -s <share>
│  ├─ del-link                 <link-path>
│  ├─ move                     <from> <to>
│  ├─ set-comment              <dfs-path> -c <text>
│  ├─ set-state                <dfs-path> -e <online|offline|resynchronize> [--use-v1]
│  ├─ set-timeout              <dfs-path> -T <sec> [--use-v1]
│  ├─ set-flags                <dfs-path> -f <flags> [-m <mask>] [--use-v1]
│  ├─ set-priority             <dfs-path> --server <server> -s <share> -c <class> -R <rank> [--use-v1]
│  ├─ get-sd                   <dfs-path>
│  ├─ set-sd                   <dfs-path> --sd <hex>
│  ├─ add-root                 <dfs-path> [--root-target <\\server\share>] [--new] [--version <0|1|2>]
│  ├─ del-root                 <dfs-path> [--root-target <\\server\share>] [--force]
│  ├─ dc-address               --server <server> [--pdc <dc>]
│  ├─ set-dc-address           --server <server> --pdc <pdc> [--set-timeout -T <seconds>] [-i]
│  ├─ flush-ft-table           
│  ├─ initialize               
│  ├─ ns-version               
│  ├─ server-version           
+- efs
│  ├─ users                    <file>
│  ├─ recovery                 <file>
│  ├─ protectors               <file>
│  ├─ file-key                 <file> [--info-class <n>] [--flags <n>] [--use-v1]
│  ├─ encrypted-metadata       <file>
│  ├─ encrypt                  <file> [--use-v1]
│  ├─ decrypt                  <file>
│  ├─ add-users                <file> --users-json <file> [--use-v1]
│  ├─ del-users                <file> --hash <sha1>
│  ├─ set-encrypted-metadata   <file> --blob-b64 <base64>
│  ├─ clone-meta               <src> <dst>
│  ├─ open-raw                 <file> [--import]
│  ├─ flush-cache              
+- dns                         (defaults to `zones`)
│  ├─ zones                    
│  ├─ records                  <zone> [-n <node>] [-T <A|AAAA|MX|TXT|CNAME|SRV|NS|PTR|SOA|ALL>]
│  ├─ nodes                    <zone> [-n <parent-node>]
│  ├─ dump                     [-z <zone>] [--skip-cache=<true|false>]
│  ├─ add-record               <zone> -n <node> -T <type> -v <value> [--ttl <sec>]
│  ├─ del-record               <zone> -n <node> -T <type> -v <value> [--ttl <sec>]
│  ├─ server-props             [-o <operation>] [--property <name>]
│  ├─ server-stats             [--clear]
│  ├─ server-scopes            
│  ├─ zone                     <zone> [--property <name>]
│  ├─ zone-stats               <zone> [--clear]
│  ├─ zone-scopes              <zone|..cache>
│  ├─ policies                 [-z <zone>]
│  ├─ policy                   <policy-name> [-z <zone>]
│  ├─ client-subnets           
│  ├─ client-subnet            <subnet-record-name>
│  ├─ add-zone                 <zone> [--type <primary|secondary|stub|forwarder>] [--master <ip> (repeatable)] [--ds]
│  ├─ del-zone                 <zone>
│  ├─ pause-zone               <zone>
│  ├─ resume-zone              <zone>
│  ├─ reload-zone              <zone>
│  ├─ set-forwarders           [--forwarder <ipv4> (repeatable)] [--timeout <sec>] [--no-recurse]
│  ├─ version                  
+- dhcp
│  ├─ scopes                   
│  ├─ scope                    <scope-ip>
│  ├─ leases                   [-s <scope-ip>]
│  ├─ ranges                   <scope-ip>
│  ├─ exclusions               <scope-ip>
│  ├─ reservations             <scope-ip>
│  ├─ stats                    
│  ├─ add-scope                <scope-ip> -m <netmask> --name <name> [--comment <text>]
│  ├─ del-scope                <scope-ip> [-f]
│  ├─ set-scope                <scope-ip> [--name <name>] [--state <enabled|disabled>]
│  ├─ add-range                <scope-ip> -F <start-ip> -T <end-ip>
│  ├─ del-range                <scope-ip> -F <start-ip> -T <end-ip> [--force]
│  ├─ add-exclusion            <scope-ip> -F <start-ip> -T <end-ip>
│  ├─ del-exclusion            <scope-ip> -F <start-ip> -T <end-ip>
│  ├─ add-reservation          <scope-ip> --ip <ip> --mac <mac>
│  ├─ del-reservation          <scope-ip> --ip <ip>
│  ├─ add-lease                --ip <ip> --mac <mac> [--name <name>] [--comment <text>]
│  ├─ lease                    <ip>
│  ├─ set-lease                --ip <ip> --mac <mac> [--name <name>] [--comment <text>]
│  ├─ options                  [-s <scope-ip>]
│  ├─ set-option               <option-id> [-s <scope-ip>] --type <type> --value <value>
│  ├─ option                   <option-id> [-s <scope-ip>]
│  ├─ del-option               <option-id> [-s <scope-ip>]
│  ├─ add-option-type          <option-id> --name <name> [--type <type>] [--array]
│  ├─ set-option-type          <option-id> --name <name> [--type <type>]
│  ├─ option-type              <option-id>
│  ├─ option-types         
│  ├─ del-option-type          <option-id>
│  ├─ config               
│  ├─ set-config               [--backup-path <path>]
│  ├─ scan-db                  [--repair]
│  ├─ del-lease                <client-ip>
│  ├─ server-version           
+- firewall
│  ├─ profile                  [-s <store>] [-P <profile>]
│  ├─ rules                    [-s <store>] [-P <profile>] [-D <direction>] [-a <allow|block>] [--enabled-only] [-n <name>]
│  ├─ products                 
│  ├─ networks                 
│  ├─ adapters                 
│  ├─ config                   [-s <store>]
│  ├─ set-config               <key> <value> [-s local]
│  ├─ dump                     [-s <store>]
│  ├─ ipsec-csrules            
│  ├─ ipsec-mmrules            
│  ├─ ipsec-authsets           
│  ├─ ipsec-cryptosets         
│  ├─ ipsec-sas                
│  ├─ enable                   [-s <store>] [-P <profile>]
│  ├─ disable                  [-s <store>] [-P <profile>]
│  ├─ add-rule                 [-s <store>] <name> -D <in|out> -a <allow|block> [-P <profile-mask>]
│  ├─ set-rule                 [-s <store>] <rule-id> [--enabled <true|false>]
│  ├─ add-ipsec-csrule         <name> [-a <mode>] [--phase1-auth <id>] [--phase2-crypto <id>] [--phase2-auth <id>] [-P <profile-mask>]
│  ├─ set-ipsec-csrule         <rule-id> [--enabled <true|false>]
│  ├─ add-ipsec-mmrule         <name> [-P <profile-mask>] --phase1-auth <id> --phase1-crypto <id>
│  ├─ set-ipsec-mmrule         <rule-id> [--enabled <true|false>]
│  ├─ add-ipsec-authset        <set-id> [-n <name>] [--phase <1|2>] [-m <method>]
│  ├─ set-ipsec-authset        <set-id> [-n <name>] [--phase <1|2>] [-m <method>]
│  ├─ add-ipsec-cryptoset      <set-id> [-n <name>] [--phase <1|2>] [--key-exchange <alg>] [--encryption <alg>] [--hash <alg>]
│  ├─ set-ipsec-cryptoset      <set-id> [-n <name>] [--phase <1|2>] [--key-exchange <alg>] [--encryption <alg>] [--hash <alg>]
│  ├─ del-rule                 [-s <store>] <rule-id>
│  ├─ del-all-rules            
│  ├─ del-ipsec-csrule         <id>
│  ├─ del-all-ipsec-csrules    
│  ├─ del-ipsec-mmrule         <id>
│  ├─ del-all-ipsec-mmrules    
│  ├─ del-ipsec-authset        <id> [--phase <1|2>]
│  ├─ del-all-ipsec-authsets   [--phase <1|2>]
│  ├─ del-ipsec-cryptoset      <id> [--phase <1|2>]
│  ├─ del-all-ipsec-cryptosets [--phase <1|2>]
│  ├─ del-phase1-sas           [--src <cidr>] [--dst <cidr>] [--protocol <num>]
│  ├─ del-phase2-sas           [--src <cidr>] [--dst <cidr>] [--protocol <num>]
│  ├─ restore-defaults         
+- printer
│  ├─ printers                 
│  ├─ dump                     [--ports] [--monitors] [--forms] [--strict]
│  ├─ drivers                  [-e <environment>]
│  ├─ ports                    
│  ├─ monitors                 
│  ├─ processors               [-e <environment>]
│  ├─ datatypes                [-c <print-processor>] [-e <environment>]
│  ├─ server               
│  ├─ forms                    
│  ├─ info                     <printer>
│  ├─ jobs                     <printer>
│  ├─ job                      <printer> -j <job-id>
│  ├─ set-job                  <printer> -j <job-id> -a <pause|resume|cancel|restart|delete|retain|release>
│  ├─ form                     <form>
│  ├─ print                    <printer> -f <file> [-d <doc-name>] [-D <datatype>]
│  ├─ driver                   <printer> [-e <environment>]
│  ├─ driver-dir               [-e <environment>]
│  ├─ processor-dir            [-e <environment>]
│  ├─ add-printer              -n <name> -d <driver> -q <port> [-s <share>] [-C <comment>] [-l <location>] [-c <processor>] [-D <datatype>]
│  ├─ del-printer              <printer>
│  ├─ set-printer              <printer> -a <pause|resume|purge>
│  ├─ set-attrs                <printer> [-A <hex>] [-R <hex>]
│  ├─ reset-printer            <printer> [-D <datatype>]
│  ├─ add-driver               <driver-name> [-e <environment>] --driver-path <path> --data-file <path> --config-file <path>
│  ├─ del-driver               <driver-name> [-e <environment>]
│  ├─ add-form                 <form> --width <mm> --height <mm> [--x-off <n>] [--y-off <n>]
│  ├─ set-form                 <form> --width <mm> --height <mm> [--x-off <n>] [--y-off <n>]
│  ├─ del-form                 <form>
│  ├─ add-port                 <port> [--monitor <name>]
│  ├─ del-port                 <port>
│  ├─ add-processor            <processor-name> --path <dll> [-e <environment>]
│  ├─ del-processor            <processor-name> [-e <environment>]
│  ├─ del-port                 <port>
│  ├─ add-monitor              <name> --path <dll> [-e <environment>]
│  ├─ del-monitor              <name> [-e <environment>]
│  ├─ notify                   <listener>
+- machinerole                 [--use-named-pipe]
+- shutdown
│  ├─ initiate                 [-m <message>] [--timeout <sec>] [--force] [-r] [--reason <text>] [--interface <initshutdown|winreg|windowsshutdown>] [--use-v1]
│  ├─ abort                    [--interface <initshutdown|winreg|windowsshutdown>]
+- perf
│  ├─ csets                    
│  ├─ cset                     <guid>
│  ├─ instances                <guid>
│  ├─ query                    <guid> [-c <counter-id>] [--instance <id>]
│  ├─ dump                     [-v] [-i]
+- time
│  ├─ sync                     [--wait <sec>] [--sync-flags <mask>]
│  ├─ bits                     
│  ├─ provider-status          <provider-name> [--provider-flags <mask>]
│  ├─ source                   
│  ├─ provider-config          <provider-name> [--provider-flags <mask>]
│  ├─ config                   
│  ├─ status                   
│  ├─ log                      
+- dcsync                      --dc <dc> (-n <name1,name2> | -N <file> | -g <object-guid> | -s <sid> | -S <sid-file> | -q <ldap-filter> | -a) [--history] [--all ektypes] [--resume-file <file>]
+- server
│  ├─ shares                   [--persistent]
│  ├─ share                    <name>
│  ├─ share-check              <path>
│  ├─ sessions                 [--client <name>] [--session-user <user>]
│  ├─ connections              [--qualifier <share|client>]
│  ├─ files                    [--base-path <path>] [--session-user <user>]
│  ├─ file                     <id>
│  ├─ get-file-acl             <share[\path]> [--security-info <mask>]
│  ├─ aliases                  
│  ├─ validate-name            <name> <type>
│  ├─ info                     [--detail <basic|standard|full|extended|config|config-full>]
│  ├─ add-share                <name> --path <local> [--remark <text>] [--share-type <n>] [--max-uses <n>] [--persistent=<true|false>]
│  ├─ set-share                <name> [--remark <text>] [--max-uses <n>]
│  ├─ set-server               <remark>
│  ├─ add-alias                <name> --alias-target <server>
│  ├─ set-file-acl             <share[\path]> --sd <hex> [--security-info <mask>]
│  ├─ del-share                <name> [--persistent]
│  ├─ del-session              [--client <name>] [--session-user <user>]
│  ├─ file-close               <id>
│  ├─ del-alias                <name>
│  ├─ disks                    
│  ├─ stats                    
│  ├─ transports               
│  ├─ add-transport            <transport> [-A <addr>] [-d <domain>] [--flags <n>] [--use-v1]
│  ├─ del-transport            <transport> [-A <addr>] [-d <domain>] [--use-v1]
+- wksta
│  ├─ info                     [--detail <basic|lan|full|config>]
│  ├─ loggedon                 
│  ├─ transports               
│  ├─ join-info                
│  ├─ stats                    
│  ├─ set-info                 (--keep-conn | --sess-timeout | --dormant-file-limit) <n>
│  ├─ join-domain              <domain> [--options <n>]
│  ├─ unjoin-domain            [--options <n>]
│  ├─ rename-machine           <new-name> [--rename-account] [--dns-only]
│  ├─ validate-name            <name> [--name-type <id>]
│  ├─ names                    [-T <primary|alternate|all>]
│  ├─ joinable-ous             <domain>
│  ├─ add-alt-name             <alt-name>
│  ├─ del-alt-name             <alt-name>
│  ├─ set-primary-name         <primary-name>
│  ├─ add-transport            <transport-name> [--quality <n>]
│  ├─ del-transport            <transport-name> [--force-level <n>]

# License

The MIT License (MIT)

Copyright (c) 2023 Artur Henrique Marzano Gonzaga

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
