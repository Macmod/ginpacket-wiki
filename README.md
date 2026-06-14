# Ginpacket

🍸 Ginpacket is a collection of Go tools for working with Windows / Active Directory network protocols. The philosophy is to provide a **simple** and **comprehensive** command-line interface to complex but useful protocol operations, turning researching & interacting with these protocols a simpler task.

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

For a complete reference of the commands supported by Ginpacket's tools, check the [Subcommands Map](#subcommands-map) or the Usage section for the specific [tools](https://ginpacket.gitbook.io/docs/tools/tools) you intend to use.

# Acknowledgements

Big thanks to the main libraries used in this project. Although I implemented lots of additional logic, this project is really just a "big wrapper" around these:
* [oiweiwei/go-msrpc](https://github.com/oiweiwei/go-msrpc)
* [RedTeamPentesting/adauth](https://github.com/RedTeamPentesting/adauth)
* [TheManticoreProject/winacl](https://github.com/TheManticoreProject/winacl)
* [go-ldap/ldap](https://github.com/go-ldap/ldap)

## References

Many tools/libraries were used as reference during the development of `ginpacket`, but the main ones:

* [fortra/impacket](https://github.com/fortra/impacket/)
* [trustedsec/Titanis](https://github.com/trustedsec/Titanis)
* [NeffIsBack/EVENmonitor](https://github.com/NeffIsBack/EVENmonitor) - the source for the logic behind the `eventlog watch` command.
* [p0dalirius/smbclient-ng](https://github.com/p0dalirius/smbclient-ng) - the source for the logic behind most of the `smb` commands.

# Other Tools

If you like this repo, you may also like these tools:

* [Macmod/godap](https://github.com/Macmod/godap) - A complete terminal user interface (TUI) for LDAP.
* [Macmod/sopa](https://github.com/Macmod/sopa) - A practical client for ADWS in Golang.
* [Macmod/flashingestor](https://github.com/Macmod/flashingestor) - A TUI for Active Directory collection.
* [FalconOpsLLC/goexec](https://github.com/FalconOpsLLC/goexec) - Windows remote execution multitool.
* [RedTeamPentesting/keycred](https://github.com/RedTeamPentesting/keycred) - Generate and Manage KeyCredentialLinks

# Subcommands Map

Index of provided tools, subcommands & key arguments:

<pre>
ginpacket/
+- authz
│  ├─ version
│  ├─ info                     &lt;SID|NAME&gt; [--class &lt;all|user|groups|restricted|device-groups|user-claims|device-claims&gt;]
│  ├─ check
│  │  ├─ [common flags]        --desired-access --principal-self --device -O/--object-types -P/--privileges --print-sd
│  │  ├─ sd                    &lt;SID|NAME&gt; -T &lt;hex-sd|sddl&gt; [common check flags]
│  │  ├─ ldap                  &lt;SID|NAME&gt; -T &lt;distinguished-name&gt; [--ldap-scheme &lt;ldap|ldaps&gt;] [--ldap-starttls] [common check flags]
│  │  ├─ services              &lt;SID|NAME&gt; -T &lt;service-name&gt; [common check flags]
│  │  ├─ tasks                 &lt;SID|NAME&gt; -T &lt;task-path&gt; [--task-folder] [common check flags]
│  │  ├─ registry              &lt;SID|NAME&gt; -T &lt;registry-path&gt; [common check flags]
│  │  ├─ smb                   &lt;SID|NAME&gt; -T &lt;share|share\\path&gt; [common check flags]
│  │  ├─ wmi-ns                &lt;SID|NAME&gt; -T &lt;namespace&gt; [common check flags]
+- gettgt                      -u &lt;user&gt; --dc &lt;DC&gt; -o &lt;ccache&gt; (-p &lt;password&gt; | -H &lt;LM:NT|NT&gt; | --aes-key &lt;hex&gt; | --pfx &lt;file&gt; | --crt &lt;file&gt; --key &lt;file&gt;)
+- getst                       -c &lt;ccache&gt; -s &lt;spn&gt; --dc &lt;DC&gt; -o &lt;out&gt; [-i &lt;user&gt; [--self]] [-a &lt;evidence-ccache&gt;]
+- changepwd
│  ├─ samr                     -a &lt;account&gt; -w &lt;new-password&gt; [-o &lt;old-password&gt;] [-T &lt;smb|tcp&gt;]
│  ├─ ldap                     -a &lt;account&gt; -w &lt;new-password&gt; [--scheme &lt;ldap|ldaps&gt;] [--starttls]
│  ├─ adws                     -a &lt;account&gt; -w &lt;new-password&gt;
│  ├─ kpasswd                  -a &lt;account&gt; -w &lt;new-password&gt; [-o &lt;old-password&gt;]
+- smb
│  ├─ shares                   
│  ├─ ls                       &lt;share[\path]&gt; [-l]
│  ├─ tree                     &lt;share[\path]&gt; [--max-depth &lt;n&gt;]
│  ├─ stat                     &lt;share[\path]&gt;
│  ├─ cat                      &lt;share[\file]&gt; [--max-bytes &lt;n&gt;]
│  ├─ get                      &lt;share[\remote]&gt; [&lt;local&gt;] [-R]
│  ├─ put                      &lt;local&gt; &lt;share[\remote]&gt; [-R]
│  ├─ mkdir                    &lt;share[\dir]&gt; [--parents]
│  ├─ rm                       &lt;share[\path]&gt; [-R]
│  ├─ mv                       &lt;share[\src]&gt; &lt;dst&gt;
│  ├─ cp                       &lt;share[\src]&gt; &lt;dst&gt;
│  ├─ shell                    -s &lt;share&gt;
+- ldap
│  ├─ whoami                   
│  ├─ info                     &lt;dn-or-name&gt; [--all]
│  ├─ search                   -F &lt;filter&gt; [-A &lt;attrs&gt;] [--hex] [--limit &lt;n&gt;] [--base-dn &lt;dn&gt;] [--scope &lt;scope&gt;]
│  ├─ modify                   &lt;dn&gt; --attr &lt;name&gt; --operation &lt;add|replace|delete&gt; --value &lt;value&gt;
│  ├─ query                    [-A &lt;attrs&gt;] [--hex] [--limit &lt;n&gt;] (flags apply to all subcommands)
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
│  │  ├─ user                  --name &lt;cn&gt; [--pass &lt;password&gt;] [--enabled] [--parent-dn &lt;dn&gt;] [--scheme ldaps|ldap] [--starttls]
│  │  ├─ computer              --name &lt;cn&gt; [--pass &lt;password&gt;] [--parent-dn &lt;dn&gt;] [--scheme ldaps|ldap] [--starttls]
│  │  ├─ group                 --name &lt;cn&gt; [--type &lt;GlobalSecurity|...&gt;] [--parent-dn &lt;dn&gt;]
│  │  ├─ ou                    --name &lt;name&gt; [--parent-dn &lt;dn&gt;]
│  │  ├─ container             --name &lt;name&gt; [--parent-dn &lt;dn&gt;]
│  │  ├─ custom                --template &lt;file.yaml&gt;
│  ├─ dacl
│  │  ├─ show                  &lt;target-dn&gt;
│  │  ├─ add                   &lt;target-dn&gt; &lt;grantee&gt; &lt;right&gt;
│  │  ├─ remove                &lt;target-dn&gt; &lt;grantee&gt; &lt;right&gt;
│  │  ├─ set-dcsync            &lt;domain-dn&gt; &lt;grantee&gt;
│  │  ├─ del-dcsync            &lt;domain-dn&gt; &lt;grantee&gt;
│  │  ├─ set-genericall        &lt;target-dn&gt; &lt;grantee&gt;
│  ├─ set-owner                &lt;target-dn&gt; &lt;new-owner&gt;
+- rpcdump                     [-U &lt;interface-uuid&gt;] [-T &lt;ncacn_ip_tcp,ncacn_np&gt;]
+- reg
│  ├─ query                    &lt;registry-path&gt; [-v &lt;value-name&gt;] [-s]
│  ├─ info                     &lt;registry-path&gt;
│  ├─ add                      &lt;registry-path&gt; -v &lt;value-name&gt; -T &lt;type&gt; -d &lt;data&gt;
│  ├─ set                      &lt;registry-path&gt; -v &lt;value-name&gt; -T &lt;type&gt; -d &lt;data&gt;
│  ├─ delete                   &lt;registry-path&gt; [-v &lt;value-name&gt;]
│  ├─ copy                     &lt;source-path&gt; &lt;destination-path&gt; [-R]
│  ├─ compare                  &lt;source-path&gt; &lt;destination-path&gt; [-R] [-O &lt;format&gt;]
│  ├─ export                   &lt;registry-path&gt; -o &lt;file&gt; [-R]
│  ├─ import                   &lt;file&gt;
│  ├─ save                     &lt;registry-path&gt; &lt;file&gt;
│  ├─ restore                  &lt;registry-path&gt; &lt;file&gt;
│  ├─ replace                  &lt;registry-path&gt; -f &lt;new-file&gt; [-b &lt;backup-file&gt;]
│  ├─ load                     &lt;mount-path&gt; &lt;file&gt;
│  ├─ unload                   &lt;mount-path&gt;
│  ├─ flush                    &lt;key&gt;
│  ├─ get-sd                   &lt;registry-path&gt; [--parse-dacl]
│  ├─ set-sd                   &lt;registry-path&gt; --sd &lt;hex-sd&gt;
│  ├─ secrets                  [--sam] [--lsa] [--cache]
│  ├─ server-version           [--hive &lt;HKLM|HKCU|HKCR|HKU|HKCC&gt;]
│  ├─ shell                    (interactive: ls, cd, get, set, add, del, info, acl, flush)
+- services
│  ├─ query                    [--type &lt;mask&gt;] [--state &lt;mask&gt;] [--group &lt;name&gt;]
│  ├─ dump                     [--type &lt;mask&gt;] [--state &lt;mask&gt;] [--group &lt;name&gt;]
│  ├─ service                  &lt;name&gt; [--use-v1]
│  ├─ get-sd                   &lt;name&gt; [--parse-dacl]
│  ├─ translate                (-K &lt;svc-key&gt; | -N &lt;display-name&gt;)
│  ├─ group                    &lt;name&gt;
│  ├─ enum-deps                &lt;name&gt;
│  ├─ add-service              &lt;name&gt; &lt;binpath&gt; [-N &lt;display-name&gt;] [-T &lt;start-type&gt;] [--service-type &lt;own|share|kernel|filesys&gt;] [--error-control &lt;ignore|normal|severe|critical&gt;] [--wow64] [--wow-type &lt;i386|amd64|arm64|hex&gt;]
│  ├─ set-service              &lt;name&gt; [-N &lt;display-name&gt;] [-b &lt;binpath&gt;] [-T &lt;start-type&gt;] [-a &lt;account&gt;] [--svc-password &lt;password&gt;]
│  ├─ start                    &lt;name&gt; [--arg &lt;value&gt; (repeatable)]
│  ├─ stop                     &lt;name&gt; [--reason &lt;hex&gt;] [--planned] [--comment &lt;text&gt;]
│  ├─ set-failure              &lt;name&gt; [-F &lt;command&gt;] [--reset-period &lt;sec&gt;] [--reboot-message &lt;text&gt;] [--failure-actions &lt;none|restart|reboot|run&gt;]
│  ├─ set-sd                   &lt;name&gt; --sd &lt;hex&gt;
│  ├─ del-service              &lt;name&gt;
+- tasks
│  ├─ query                    [-P &lt;path&gt;] [--include-hidden] [--use-v1]
│  ├─ task                     &lt;path&gt; [--format xml]
│  ├─ folders                  [path]
│  ├─ xml                      &lt;path&gt;
│  ├─ instances                &lt;path&gt;
│  ├─ missed-runs              &lt;path&gt;
│  ├─ dump                     [--include-hidden]
│  ├─ add                      &lt;path&gt; -X &lt;task-xml&gt; [--use-v1]
│  ├─ add-folder               &lt;path&gt;
│  ├─ rename                   &lt;path&gt; &lt;new-path&gt;
│  ├─ run                      &lt;path&gt;
│  ├─ enable                   &lt;path&gt;
│  ├─ disable                  &lt;path&gt;
│  ├─ get-sddl                 &lt;path&gt;
│  ├─ set-sddl                 &lt;path&gt; --sddl &lt;text&gt;
│  ├─ stop                     &lt;path&gt; [--instance &lt;guid&gt;]
│  ├─ del                      &lt;path&gt; [--use-v1]
│  ├─ del-folder               &lt;path&gt;
+- eventlog
│  ├─ query                    &lt;channel&gt; [-q &lt;query&gt;] [-L &lt;n&gt;] [--timeout-ms &lt;ms&gt;]
│  ├─ subscribe                &lt;channel&gt; [-q &lt;query&gt;] [-L &lt;n&gt;] [--timeout-ms &lt;ms&gt;]
│  ├─ watch                    &lt;channel&gt; [-q &lt;query&gt;] [-F &lt;text|json&gt;] [-L &lt;n&gt;] [--timeout-ms &lt;ms&gt;]
│  ├─ channels                 
│  ├─ publishers               
│  ├─ export                   &lt;channel&gt; &lt;out-path&gt; [-q &lt;query&gt;]
│  ├─ clear                    &lt;channel&gt; [-b &lt;backup-path&gt;] [--confirm]
│  ├─ channel                  [&lt;channel&gt;] [-T config|meta|all]
│  ├─ publisher                &lt;name&gt;
│  ├─ channel-publishers       [&lt;channel&gt;]
│  ├─ classic-name             &lt;name&gt;
│  ├─ set-channel              [&lt;channel&gt;] [--enabled &lt;true|false&gt;] [--max-size &lt;bytes&gt;]
+- cert
│  ├─ ping                     &lt;ca-name&gt; [--use-v1]
│  ├─ my-roles                 &lt;ca-name&gt;
│  ├─ ca-info                  &lt;ca-name&gt;
│  ├─ ca-state                 &lt;ca-name&gt;
│  ├─ ca-unregister-dcom       &lt;ca-name&gt;
│  ├─ get-sd|get-ca-sd         &lt;ca-name&gt; [--out &lt;file&gt;]
│  ├─ set-sd|set-ca-sd         &lt;ca-name&gt; &lt;value&gt; [--hex|--base64]
│  ├─ get-audit                &lt;ca-name&gt;
│  ├─ set-audit                &lt;ca-name&gt; &lt;mask&gt;
│  ├─ ca-config                &lt;ca-name&gt; &lt;node-path&gt; &lt;entry&gt;
│  ├─ set-ca-config            &lt;ca-name&gt; &lt;node-path&gt; &lt;entry&gt; &lt;value&gt; [--type &lt;string|dword&gt;]
│  ├─ ca-props                 &lt;ca-name&gt;
│  ├─ set-ca-prop              &lt;ca-name&gt; &lt;prop-id&gt; &lt;value&gt; [--type &lt;auto|long|string|binary&gt;] [--index &lt;n&gt;] [--file|--base64]
│  ├─ view-default-columns     &lt;ca-name&gt; &lt;pending|issued|failed|extension|attribute|crl|revoked&gt;
│  ├─ request                  &lt;ca-name&gt; [--csr &lt;file&gt;] [--template &lt;name&gt;] [--attrs &lt;k:v;...&gt;] [--out &lt;file&gt;] [--cms]
│  ├─ retrieve                 &lt;ca-name&gt; [&lt;request-id&gt;] [--serial &lt;hex&gt;] [--out &lt;file&gt;]
│  ├─ approve                  &lt;ca-name&gt; &lt;request-id&gt;
│  ├─ deny                     &lt;ca-name&gt; &lt;request-id&gt;
│  ├─ revoke                   &lt;ca-name&gt; &lt;serial&gt; [--reason &lt;code|name&gt;] [--date &lt;yyyy-mm-dd&gt;]
│  ├─ check                    &lt;ca-name&gt; &lt;serial&gt;
│  ├─ publish-crl              &lt;ca-name&gt; [--next &lt;yyyy-mm-dd&gt;] [--delta] [--force] [--legacy]
│  ├─ get-crl                  &lt;ca-name&gt; [--out &lt;file&gt;]
│  ├─ import-cert              &lt;ca-name&gt; &lt;file&gt; [--allow-foreign] [--existing-row]
│  ├─ import-key               &lt;ca-name&gt; &lt;request-id&gt; &lt;pkcs7-file&gt; [--cert-hash &lt;sha1&gt;] [--overwrite]
│  ├─ set-extension            &lt;ca-name&gt; &lt;request-id&gt; &lt;oid&gt; &lt;hex-der&gt; [--type &lt;1|2|3|4&gt;] [--critical] [--disabled]
│  ├─ set-attrs                &lt;ca-name&gt; &lt;request-id&gt; &lt;attributes&gt; [--file &lt;path&gt;]
│  ├─ request-attrs            &lt;ca-name&gt; &lt;request-id&gt;
│  ├─ request-exts             &lt;ca-name&gt; &lt;request-id&gt;
│  ├─ request-meta             &lt;ca-name&gt; &lt;request-id&gt;
│  ├─ restore-paths            &lt;ca-name&gt;
│  ├─ officer-rights           &lt;ca-name&gt;
│  ├─ set-officer-rights       &lt;ca-name&gt; [--enable|--disable] [--sd-file &lt;path&gt;]
│  ├─ archived-key             &lt;ca-name&gt; &lt;request-id&gt; [--out &lt;file&gt;]
│  ├─ db                       &lt;ca-name&gt; [--table &lt;request|extension|attribute|crl&gt;] [--columns c1,c2] [--offset &lt;n&gt;] [--limit &lt;n&gt;] [--format &lt;text|csv|json&gt;] [--use-v1]
│  ├─ requests                 &lt;ca-name&gt; [--columns c1,c2] [--offset &lt;n&gt;] [--limit &lt;n&gt;] [--format &lt;text|csv|json&gt;] [--use-v1]
│  ├─ pending                  &lt;ca-name&gt; [--columns c1,c2] [--offset &lt;n&gt;] [--limit &lt;n&gt;] [--format &lt;text|csv|json&gt;] [--use-v1]
│  ├─ issued                   &lt;ca-name&gt; [--columns c1,c2] [--offset &lt;n&gt;] [--limit &lt;n&gt;] [--format &lt;text|csv|json&gt;] [--use-v1]
│  ├─ failed                   &lt;ca-name&gt; [--columns c1,c2] [--offset &lt;n&gt;] [--limit &lt;n&gt;] [--format &lt;text|csv|json&gt;] [--use-v1]
│  ├─ revoked                  &lt;ca-name&gt; [--columns c1,c2] [--offset &lt;n&gt;] [--limit &lt;n&gt;] [--format &lt;text|csv|json&gt;] [--use-v1]
│  ├─ del-row                  &lt;ca-name&gt; [row-id] [--table &lt;request|extension|attribute|crl&gt;] [--expired|--pending-failed --before &lt;yyyy-mm-dd&gt;]
+- tsts
│  ├─ sessions                 [-s &lt;state&gt;] [-f &lt;username&gt;]
│  ├─ processes                [-s &lt;session-id&gt;]
│  ├─ policy
│  ├─ session                  &lt;id&gt; [-c] [-g]
│  ├─ watch                    [-e &lt;create,delete,rename,connect,disconnect,logon,logoff,statechange|all&gt;]
│  ├─ listeners
│  ├─ connect                  &lt;src-session&gt; &lt;dst-session&gt; [-P &lt;target-password&gt;]
│  ├─ message                  &lt;session-id&gt; -T &lt;title&gt; -m &lt;text&gt; [-s &lt;style&gt;] [-o &lt;seconds&gt;] [-a]
│  ├─ kill-session             &lt;id&gt; [-w]
│  ├─ logoff                   &lt;session-id&gt;
│  ├─ disconnect               &lt;session-id&gt; [-w]
│  ├─ kill-process             &lt;pid&gt; [-e &lt;exit-code&gt;]
│  ├─ stop-listener            &lt;name&gt;
│  ├─ start-listener           &lt;name&gt;
│  ├─ shutdown                 [-r] [-P] [-l]
+- wmi
│  ├─ query                    [-n &lt;namespace&gt;] &lt;wql&gt; [-f &lt;fields&gt;] [-L &lt;n&gt;]
│  ├─ namespaces               [-n &lt;namespace&gt;]
│  ├─ classes                  [-n &lt;namespace&gt;] [--superclass &lt;str&gt;] [-L &lt;n&gt;]
│  ├─ instance                 [-n &lt;namespace&gt;] &lt;object-path&gt;
│  ├─ class                    [-n &lt;namespace&gt;] &lt;class&gt;
│  ├─ methods                  [-n &lt;namespace&gt;] &lt;class&gt;
│  ├─ exec                     [-n &lt;namespace&gt;] &lt;command&gt;
│  ├─ invoke                   [-n &lt;namespace&gt;] &lt;object::method&gt; [--arg &lt;k=v&gt;]
│  ├─ del-instance             [-n &lt;namespace&gt;] &lt;object-path&gt;
+- sam
│  ├─ domains
│  ├─ domain                   [-d &lt;name&gt;]
│  ├─ set-domain               [-d &lt;name&gt;] [--min-pwd-len &lt;n&gt;] [--lockout-threshold &lt;n&gt;] [--lockout-window &lt;dur&gt;] [--lockout-duration &lt;dur&gt;]
│  ├─ password-policy          [-d &lt;name&gt;]
│  ├─ get-acl                  [-d &lt;name&gt;]
│  ├─ set-acl                  --sd &lt;hex&gt; [-d &lt;name&gt;]
│  ├─ users                    [-d &lt;name&gt;]
│  ├─ display                  [-d &lt;name&gt;] [--type &lt;users|machines|groups&gt;] [--prefix &lt;str&gt;]
│  ├─ user                     &lt;username|RID&gt; [-d &lt;name&gt;]
│  ├─ add-user                 &lt;name&gt; [-d &lt;name&gt;] [-N &lt;s&gt;] [-D &lt;s&gt;] [-w &lt;s&gt;] [--disable]
│  ├─ del-user                 &lt;username|RID&gt; [-d &lt;name&gt;]
│  ├─ set-user                 &lt;username|RID&gt; [-d &lt;name&gt;] [-N &lt;s&gt;] [-D &lt;s&gt;] [-w &lt;s&gt;] [-e &lt;RFC3339|never&gt;] [--uac-set &lt;flag&gt;] [--uac-clear &lt;flag&gt;]
│  ├─ user-groups              &lt;username|RID&gt; [-d &lt;name&gt;]
│  ├─ user-aliases             &lt;username|RID&gt; [-d &lt;name&gt;]
│  ├─ validate-password        &lt;password&gt; [-d &lt;name&gt;] [-O &lt;auth|change|reset&gt;] [--account &lt;s&gt;]
│  ├─ groups                   [-d &lt;name&gt;]
│  ├─ group                    &lt;name|RID&gt; [-d &lt;name&gt;]
│  ├─ add-group                &lt;name&gt; [-d &lt;name&gt;]
│  ├─ del-group                &lt;name|RID&gt; [-d &lt;name&gt;]
│  ├─ group-members            &lt;name|RID&gt; [-d &lt;name&gt;] [--resolve-sids]
│  ├─ add-group-member         &lt;group&gt; &lt;member&gt; [-d &lt;name&gt;]
│  ├─ del-group-member         &lt;group&gt; &lt;member&gt; [-d &lt;name&gt;]
│  ├─ set-group                &lt;name|RID&gt; [-d &lt;name&gt;] [--name &lt;s&gt;] [--description &lt;s&gt;]
│  ├─ set-member-attrs         &lt;group&gt; &lt;member&gt; [-d &lt;name&gt;] [--attributes &lt;hex&gt;]
│  ├─ aliases                  [-d &lt;name&gt;] [--builtin]
│  ├─ alias                    &lt;name|RID&gt; [-d &lt;name&gt;] [--builtin]
│  ├─ add-alias                &lt;name&gt; [-d &lt;name&gt;]
│  ├─ del-alias                &lt;name|RID&gt; [-d &lt;name&gt;] [--builtin]
│  ├─ alias-members            &lt;name|RID&gt; [-d &lt;name&gt;] [--builtin] [--resolve-sids]
│  ├─ alias-membership         &lt;sid&gt; [-d &lt;name&gt;] [--builtin]
│  ├─ add-alias-member         &lt;alias&gt; &lt;sid|username&gt; [-d &lt;name&gt;] [--builtin]
│  ├─ del-alias-member         &lt;alias&gt; &lt;sid|username&gt; [-d &lt;name&gt;] [--builtin]
│  ├─ add-alias-members        &lt;alias&gt; &lt;sid|username&gt;... [-d &lt;name&gt;] [--builtin]
│  ├─ del-alias-members        &lt;alias&gt; &lt;sid|username&gt;... [-d &lt;name&gt;] [--builtin]
│  ├─ set-alias                &lt;name|RID&gt; [-d &lt;name&gt;] [--builtin] [--name &lt;s&gt;] [--description &lt;s&gt;]
│  ├─ purge-sid                &lt;sid&gt; [-d &lt;name&gt;] [--builtin]
│  ├─ lookup-names             &lt;name&gt;... [-d &lt;name&gt;]
│  ├─ lookup-rids              &lt;rid&gt;... [-d &lt;name&gt;]
│  ├─ rid-to-sid               &lt;rid&gt;
│  ├─ set-dsrm-password        &lt;new-password&gt;
+- lsa                         [--use-tcp]
│  ├─ policy             
│  ├─ domain-policy      
│  ├─ get-sd                   [--security-info &lt;mask&gt;]
│  ├─ set-sd                   --sd &lt;hex&gt; [--security-info &lt;mask&gt;]
│  ├─ privileges               
│  ├─ lookup-priv              &lt;priv-name&gt;
│  ├─ priv-name                --high &lt;n&gt; --low &lt;n&gt;
│  ├─ accounts                 
│  ├─ rights                   [-r &lt;right,right,...&gt;]
│  ├─ account-rights           &lt;sid&gt;
│  ├─ account-privs            &lt;sid&gt;
│  ├─ account-access           &lt;sid&gt;
│  ├─ set-account-access       &lt;sid&gt; &lt;access&gt;
│  ├─ add-rights               &lt;sid&gt; -r &lt;right,right,...&gt;
│  ├─ del-rights               &lt;sid&gt; -r &lt;right,right,...&gt;
│  ├─ add-account              &lt;sid&gt;
│  ├─ del-account              &lt;sid&gt;
│  ├─ add-secret               &lt;name&gt;
│  ├─ get-secret               &lt;name&gt;
│  ├─ secret                   &lt;name&gt;
│  ├─ set-secret               &lt;name&gt; -v &lt;hex&gt;
│  ├─ del-secret               &lt;name&gt;
│  ├─ trusts                   [--use-v1]
│  ├─ trust-records            &lt;domain&gt;
│  ├─ trust                    (-n &lt;domain&gt; | -s &lt;sid&gt;) [--use-v1]
│  ├─ set-trust                (-n &lt;domain&gt; | -s &lt;sid&gt;) [-D &lt;n&gt;] [-T &lt;n&gt;] [--attributes &lt;hex&gt;]
│  ├─ add-trust                -n &lt;domain&gt; --flat-name &lt;name&gt; -s &lt;sid&gt; [-w &lt;secret&gt;] [-D &lt;n&gt;] [-T &lt;n&gt;]
│  ├─ del-trust                &lt;sid&gt;
│  ├─ set-trust-records        &lt;domain&gt; [--check]
│  ├─ set-audit                [--enable] [--disable] [--event &lt;cat=none|success|failure|both&gt;]
│  ├─ set-domain-policy        [--max-service-ticket &lt;dur&gt;] [--max-tgt &lt;dur&gt;] [--max-renew &lt;dur&gt;] [--max-skew &lt;dur&gt;] [--validate-client] [--no-validate-client]
+- lookupsid                   (-s &lt;sid&gt; | -n &lt;name&gt; | -D &lt;domain-sid&gt; -F &lt;start-rid&gt; -T &lt;end-rid&gt;) [--use-v1]
+- bkpkey
│  ├─ backup                   --in-file &lt;request.bin&gt; -o &lt;response.bin&gt;
│  ├─ restore                  (--in-file &lt;restore.bin&gt; | --in-b64 &lt;base64&gt;) [--win2k]
│  ├─ retrieve                 -o &lt;backupkey.bin&gt;
+- dfs
│  ├─ namespaces               
│  ├─ dump                     
│  ├─ links                    &lt;namespace-path&gt;
│  ├─ info                     &lt;path&gt; [--gen-guid] [--version]
│  ├─ add-link                 &lt;link-path&gt; --server &lt;server&gt; -s &lt;share&gt;
│  ├─ del-link                 &lt;link-path&gt;
│  ├─ move                     &lt;from&gt; &lt;to&gt;
│  ├─ set-comment              &lt;dfs-path&gt; -c &lt;text&gt;
│  ├─ set-state                &lt;dfs-path&gt; -e &lt;online|offline|resynchronize&gt; [--use-v1]
│  ├─ set-timeout              &lt;dfs-path&gt; -T &lt;sec&gt; [--use-v1]
│  ├─ set-flags                &lt;dfs-path&gt; -f &lt;flags&gt; [-m &lt;mask&gt;] [--use-v1]
│  ├─ set-priority             &lt;dfs-path&gt; --server &lt;server&gt; -s &lt;share&gt; -c &lt;class&gt; -R &lt;rank&gt; [--use-v1]
│  ├─ get-sd                   &lt;dfs-path&gt;
│  ├─ set-sd                   &lt;dfs-path&gt; --sd &lt;hex&gt;
│  ├─ add-root                 &lt;dfs-path&gt; [--root-target &lt;\\server\share&gt;] [--new] [--version &lt;0|1|2&gt;]
│  ├─ del-root                 &lt;dfs-path&gt; [--root-target &lt;\\server\share&gt;] [--force]
│  ├─ dc-address               --server &lt;server&gt; [--pdc &lt;dc&gt;]
│  ├─ set-dc-address           --server &lt;server&gt; --pdc &lt;pdc&gt; [--set-timeout -T &lt;seconds&gt;] [-i]
│  ├─ flush-ft-table           
│  ├─ initialize               
│  ├─ ns-version               
│  ├─ server-version           
+- efs
│  ├─ users                    &lt;file&gt;
│  ├─ recovery                 &lt;file&gt;
│  ├─ protectors               &lt;file&gt;
│  ├─ file-key                 &lt;file&gt; [--info-class &lt;n&gt;] [--flags &lt;n&gt;] [--use-v1]
│  ├─ encrypted-metadata       &lt;file&gt;
│  ├─ encrypt                  &lt;file&gt; [--use-v1]
│  ├─ decrypt                  &lt;file&gt;
│  ├─ add-users                &lt;file&gt; --users-json &lt;file&gt; [--use-v1]
│  ├─ del-users                &lt;file&gt; --hash &lt;sha1&gt;
│  ├─ set-encrypted-metadata   &lt;file&gt; --blob-b64 &lt;base64&gt;
│  ├─ clone-meta               &lt;src&gt; &lt;dst&gt;
│  ├─ open-raw                 &lt;file&gt; [--import]
│  ├─ flush-cache              
+- dns                         (defaults to `zones`)
│  ├─ zones                    
│  ├─ records                  &lt;zone&gt; [-n &lt;node&gt;] [-T &lt;A|AAAA|MX|TXT|CNAME|SRV|NS|PTR|SOA|ALL&gt;]
│  ├─ nodes                    &lt;zone&gt; [-n &lt;parent-node&gt;]
│  ├─ dump                     [-z &lt;zone&gt;] [--skip-cache=&lt;true|false&gt;]
│  ├─ add-record               &lt;zone&gt; -n &lt;node&gt; -T &lt;type&gt; -v &lt;value&gt; [--ttl &lt;sec&gt;]
│  ├─ del-record               &lt;zone&gt; -n &lt;node&gt; -T &lt;type&gt; -v &lt;value&gt; [--ttl &lt;sec&gt;]
│  ├─ server-props             [-o &lt;operation&gt;] [--property &lt;name&gt;]
│  ├─ server-stats             [--clear]
│  ├─ server-scopes            
│  ├─ zone                     &lt;zone&gt; [--property &lt;name&gt;]
│  ├─ zone-stats               &lt;zone&gt; [--clear]
│  ├─ zone-scopes              &lt;zone|..cache&gt;
│  ├─ policies                 [-z &lt;zone&gt;]
│  ├─ policy                   &lt;policy-name&gt; [-z &lt;zone&gt;]
│  ├─ client-subnets           
│  ├─ client-subnet            &lt;subnet-record-name&gt;
│  ├─ add-zone                 &lt;zone&gt; [--type &lt;primary|secondary|stub|forwarder&gt;] [--master &lt;ip&gt; (repeatable)] [--ds]
│  ├─ del-zone                 &lt;zone&gt;
│  ├─ pause-zone               &lt;zone&gt;
│  ├─ resume-zone              &lt;zone&gt;
│  ├─ reload-zone              &lt;zone&gt;
│  ├─ set-forwarders           [--forwarder &lt;ipv4&gt; (repeatable)] [--timeout &lt;sec&gt;] [--no-recurse]
│  ├─ version                  
+- dhcp
│  ├─ scopes                   
│  ├─ scope                    &lt;scope-ip&gt;
│  ├─ leases                   [-s &lt;scope-ip&gt;]
│  ├─ ranges                   &lt;scope-ip&gt;
│  ├─ exclusions               &lt;scope-ip&gt;
│  ├─ reservations             &lt;scope-ip&gt;
│  ├─ stats                    
│  ├─ add-scope                &lt;scope-ip&gt; -m &lt;netmask&gt; --name &lt;name&gt; [--comment &lt;text&gt;]
│  ├─ del-scope                &lt;scope-ip&gt; [-f]
│  ├─ set-scope                &lt;scope-ip&gt; [--name &lt;name&gt;] [--state &lt;enabled|disabled&gt;]
│  ├─ add-range                &lt;scope-ip&gt; -F &lt;start-ip&gt; -T &lt;end-ip&gt;
│  ├─ del-range                &lt;scope-ip&gt; -F &lt;start-ip&gt; -T &lt;end-ip&gt; [--force]
│  ├─ add-exclusion            &lt;scope-ip&gt; -F &lt;start-ip&gt; -T &lt;end-ip&gt;
│  ├─ del-exclusion            &lt;scope-ip&gt; -F &lt;start-ip&gt; -T &lt;end-ip&gt;
│  ├─ add-reservation          &lt;scope-ip&gt; --ip &lt;ip&gt; --mac &lt;mac&gt;
│  ├─ del-reservation          &lt;scope-ip&gt; --ip &lt;ip&gt;
│  ├─ add-lease                --ip &lt;ip&gt; --mac &lt;mac&gt; [--name &lt;name&gt;] [--comment &lt;text&gt;]
│  ├─ lease                    &lt;ip&gt;
│  ├─ set-lease                --ip &lt;ip&gt; --mac &lt;mac&gt; [--name &lt;name&gt;] [--comment &lt;text&gt;]
│  ├─ options                  [-s &lt;scope-ip&gt;]
│  ├─ set-option               &lt;option-id&gt; [-s &lt;scope-ip&gt;] --type &lt;type&gt; --value &lt;value&gt;
│  ├─ option                   &lt;option-id&gt; [-s &lt;scope-ip&gt;]
│  ├─ del-option               &lt;option-id&gt; [-s &lt;scope-ip&gt;]
│  ├─ add-option-type          &lt;option-id&gt; --name &lt;name&gt; [--type &lt;type&gt;] [--array]
│  ├─ set-option-type          &lt;option-id&gt; --name &lt;name&gt; [--type &lt;type&gt;]
│  ├─ option-type              &lt;option-id&gt;
│  ├─ option-types         
│  ├─ del-option-type          &lt;option-id&gt;
│  ├─ config               
│  ├─ set-config               [--backup-path &lt;path&gt;]
│  ├─ scan-db                  [--repair]
│  ├─ del-lease                &lt;client-ip&gt;
│  ├─ server-version           
+- firewall
│  ├─ profile                  [-s &lt;store&gt;] [-P &lt;profile&gt;]
│  ├─ rules                    [-s &lt;store&gt;] [-P &lt;profile&gt;] [-D &lt;direction&gt;] [-a &lt;allow|block&gt;] [--enabled-only] [-n &lt;name&gt;]
│  ├─ products                 
│  ├─ networks                 
│  ├─ adapters                 
│  ├─ config                   [-s &lt;store&gt;]
│  ├─ set-config               &lt;key&gt; &lt;value&gt; [-s local]
│  ├─ dump                     [-s &lt;store&gt;]
│  ├─ ipsec-csrules            
│  ├─ ipsec-mmrules            
│  ├─ ipsec-authsets           
│  ├─ ipsec-cryptosets         
│  ├─ ipsec-sas                
│  ├─ enable                   [-s &lt;store&gt;] [-P &lt;profile&gt;]
│  ├─ disable                  [-s &lt;store&gt;] [-P &lt;profile&gt;]
│  ├─ add-rule                 [-s &lt;store&gt;] &lt;name&gt; -D &lt;in|out&gt; -a &lt;allow|block&gt; [-P &lt;profile-mask&gt;]
│  ├─ set-rule                 [-s &lt;store&gt;] &lt;rule-id&gt; [--enabled &lt;true|false&gt;]
│  ├─ add-ipsec-csrule         &lt;name&gt; [-a &lt;mode&gt;] [--phase1-auth &lt;id&gt;] [--phase2-crypto &lt;id&gt;] [--phase2-auth &lt;id&gt;] [-P &lt;profile-mask&gt;]
│  ├─ set-ipsec-csrule         &lt;rule-id&gt; [--enabled &lt;true|false&gt;]
│  ├─ add-ipsec-mmrule         &lt;name&gt; [-P &lt;profile-mask&gt;] --phase1-auth &lt;id&gt; --phase1-crypto &lt;id&gt;
│  ├─ set-ipsec-mmrule         &lt;rule-id&gt; [--enabled &lt;true|false&gt;]
│  ├─ add-ipsec-authset        &lt;set-id&gt; [-n &lt;name&gt;] [--phase &lt;1|2&gt;] [-m &lt;method&gt;]
│  ├─ set-ipsec-authset        &lt;set-id&gt; [-n &lt;name&gt;] [--phase &lt;1|2&gt;] [-m &lt;method&gt;]
│  ├─ add-ipsec-cryptoset      &lt;set-id&gt; [-n &lt;name&gt;] [--phase &lt;1|2&gt;] [--key-exchange &lt;alg&gt;] [--encryption &lt;alg&gt;] [--hash &lt;alg&gt;]
│  ├─ set-ipsec-cryptoset      &lt;set-id&gt; [-n &lt;name&gt;] [--phase &lt;1|2&gt;] [--key-exchange &lt;alg&gt;] [--encryption &lt;alg&gt;] [--hash &lt;alg&gt;]
│  ├─ del-rule                 [-s &lt;store&gt;] &lt;rule-id&gt;
│  ├─ del-all-rules            
│  ├─ del-ipsec-csrule         &lt;id&gt;
│  ├─ del-all-ipsec-csrules    
│  ├─ del-ipsec-mmrule         &lt;id&gt;
│  ├─ del-all-ipsec-mmrules    
│  ├─ del-ipsec-authset        &lt;id&gt; [--phase &lt;1|2&gt;]
│  ├─ del-all-ipsec-authsets   [--phase &lt;1|2&gt;]
│  ├─ del-ipsec-cryptoset      &lt;id&gt; [--phase &lt;1|2&gt;]
│  ├─ del-all-ipsec-cryptosets [--phase &lt;1|2&gt;]
│  ├─ del-phase1-sas           [--src &lt;cidr&gt;] [--dst &lt;cidr&gt;] [--protocol &lt;num&gt;]
│  ├─ del-phase2-sas           [--src &lt;cidr&gt;] [--dst &lt;cidr&gt;] [--protocol &lt;num&gt;]
│  ├─ restore-defaults         
+- printer
│  ├─ printers                 
│  ├─ dump                     [--ports] [--monitors] [--forms] [--strict]
│  ├─ drivers                  [-e &lt;environment&gt;]
│  ├─ ports                    
│  ├─ monitors                 
│  ├─ processors               [-e &lt;environment&gt;]
│  ├─ datatypes                [-c &lt;print-processor&gt;] [-e &lt;environment&gt;]
│  ├─ server               
│  ├─ forms                    
│  ├─ info                     &lt;printer&gt;
│  ├─ jobs                     &lt;printer&gt;
│  ├─ job                      &lt;printer&gt; -j &lt;job-id&gt;
│  ├─ set-job                  &lt;printer&gt; -j &lt;job-id&gt; -a &lt;pause|resume|cancel|restart|delete|retain|release&gt;
│  ├─ form                     &lt;form&gt;
│  ├─ print                    &lt;printer&gt; -f &lt;file&gt; [-d &lt;doc-name&gt;] [-D &lt;datatype&gt;]
│  ├─ driver                   &lt;printer&gt; [-e &lt;environment&gt;]
│  ├─ driver-dir               [-e &lt;environment&gt;]
│  ├─ processor-dir            [-e &lt;environment&gt;]
│  ├─ add-printer              -n &lt;name&gt; -d &lt;driver&gt; -q &lt;port&gt; [-s &lt;share&gt;] [-C &lt;comment&gt;] [-l &lt;location&gt;] [-c &lt;processor&gt;] [-D &lt;datatype&gt;]
│  ├─ del-printer              &lt;printer&gt;
│  ├─ set-printer              &lt;printer&gt; -a &lt;pause|resume|purge&gt;
│  ├─ set-attrs                &lt;printer&gt; [-A &lt;hex&gt;] [-R &lt;hex&gt;]
│  ├─ reset-printer            &lt;printer&gt; [-D &lt;datatype&gt;]
│  ├─ add-driver               &lt;driver-name&gt; [-e &lt;environment&gt;] --driver-path &lt;path&gt; --data-file &lt;path&gt; --config-file &lt;path&gt;
│  ├─ del-driver               &lt;driver-name&gt; [-e &lt;environment&gt;]
│  ├─ add-form                 &lt;form&gt; --width &lt;mm&gt; --height &lt;mm&gt; [--x-off &lt;n&gt;] [--y-off &lt;n&gt;]
│  ├─ set-form                 &lt;form&gt; --width &lt;mm&gt; --height &lt;mm&gt; [--x-off &lt;n&gt;] [--y-off &lt;n&gt;]
│  ├─ del-form                 &lt;form&gt;
│  ├─ add-port                 &lt;port&gt; [--monitor &lt;name&gt;]
│  ├─ del-port                 &lt;port&gt;
│  ├─ add-processor            &lt;processor-name&gt; --path &lt;dll&gt; [-e &lt;environment&gt;]
│  ├─ del-processor            &lt;processor-name&gt; [-e &lt;environment&gt;]
│  ├─ del-port                 &lt;port&gt;
│  ├─ add-monitor              &lt;name&gt; --path &lt;dll&gt; [-e &lt;environment&gt;]
│  ├─ del-monitor              &lt;name&gt; [-e &lt;environment&gt;]
│  ├─ notify                   &lt;listener&gt;
+- machinerole                 [--use-named-pipe]
+- shutdown
│  ├─ initiate                 [-m &lt;message&gt;] [--timeout &lt;sec&gt;] [--force] [-r] [--reason &lt;text&gt;] [--interface &lt;initshutdown|winreg|windowsshutdown&gt;] [--use-v1]
│  ├─ abort                    [--interface &lt;initshutdown|winreg|windowsshutdown&gt;]
+- perf
│  ├─ csets                    
│  ├─ cset                     &lt;guid&gt;
│  ├─ instances                &lt;guid&gt;
│  ├─ query                    &lt;guid&gt; [-c &lt;counter-id&gt;] [--instance &lt;id&gt;]
│  ├─ dump                     [-v] [-i]
+- time
│  ├─ sync                     [--wait &lt;sec&gt;] [--sync-flags &lt;mask&gt;]
│  ├─ bits                     
│  ├─ provider-status          &lt;provider-name&gt; [--provider-flags &lt;mask&gt;]
│  ├─ source                   
│  ├─ provider-config          &lt;provider-name&gt; [--provider-flags &lt;mask&gt;]
│  ├─ config                   
│  ├─ status                   
│  ├─ log                      
+- dcsync                      --dc &lt;dc&gt; (-n &lt;name1,name2&gt; | -N &lt;file&gt; | -g &lt;object-guid&gt; | -G &lt;guids-file&gt; | -s &lt;sid&gt; | -S &lt;sid-file&gt; | -q &lt;ldap-filter&gt; | -a) [--history] [--all-keytypes] [--resume-file &lt;file&gt;]
+- server
│  ├─ dump                     
│  ├─ shares                   [--persistent]
│  ├─ share                    &lt;name&gt;
│  ├─ share-check              &lt;path&gt;
│  ├─ sessions                 [--client &lt;name&gt;] [--session-user &lt;user&gt;]
│  ├─ connections              [--qualifier &lt;share|client&gt;]
│  ├─ files                    [--base-path &lt;path&gt;] [--session-user &lt;user&gt;]
│  ├─ file                     &lt;id&gt;
│  ├─ get-file-acl             &lt;share[\path]&gt; [--security-info &lt;mask&gt;]
│  ├─ aliases                  
│  ├─ validate-name            &lt;name&gt; &lt;type&gt;
│  ├─ info                     [--detail &lt;basic|standard|full|extended|config|config-full&gt;]
│  ├─ add-share                &lt;name&gt; --path &lt;local&gt; [--remark &lt;text&gt;] [--share-type &lt;n&gt;] [--max-uses &lt;n&gt;] [--persistent=&lt;true|false&gt;]
│  ├─ set-share                &lt;name&gt; [--remark &lt;text&gt;] [--max-uses &lt;n&gt;]
│  ├─ set-server               [--comment &lt;text&gt;] [--max-users &lt;n&gt;] [--auto-disc &lt;min&gt;] [--hidden] [--announce &lt;sec&gt;] [--announce-delta &lt;ms&gt;]
│  ├─ add-alias                &lt;name&gt; --alias-target &lt;server&gt;
│  ├─ set-file-acl             &lt;share[\path]&gt; --sd &lt;hex&gt; [--security-info &lt;mask&gt;]
│  ├─ del-share                &lt;name&gt; [--persistent]
│  ├─ del-session              [--client &lt;name&gt;] [--session-user &lt;user&gt;]
│  ├─ file-close               &lt;id&gt;
│  ├─ del-alias                &lt;name&gt;
│  ├─ disks                    
│  ├─ stats                    
│  ├─ transports               
│  ├─ add-transport            &lt;transport&gt; [-A &lt;addr&gt;] [-d &lt;domain&gt;] [--flags &lt;n&gt;] [--use-v1]
│  ├─ del-transport            &lt;transport&gt; [-A &lt;addr&gt;] [-d &lt;domain&gt;] [--use-v1]
+- wksta
│  ├─ info                     [--detail &lt;basic|lan|full|config&gt;]
│  ├─ loggedon                 
│  ├─ transports               
│  ├─ join-info                
│  ├─ stats                    
│  ├─ set-info                 (--keep-conn | --sess-timeout | --dormant-file-limit) &lt;n&gt;
│  ├─ join-domain              &lt;domain&gt; [--options &lt;n&gt;]
│  ├─ unjoin-domain            [--options &lt;n&gt;]
│  ├─ rename-machine           &lt;new-name&gt; [--rename-account] [--dns-only]
│  ├─ validate-name            &lt;name&gt; [--name-type &lt;id&gt;]
│  ├─ names                    [-T &lt;primary|alternate|all&gt;]
│  ├─ joinable-ous             &lt;domain&gt;
│  ├─ add-alt-name             &lt;alt-name&gt;
│  ├─ del-alt-name             &lt;alt-name&gt;
│  ├─ set-primary-name         &lt;primary-name&gt;
│  ├─ add-transport            &lt;transport-name&gt; [--quality &lt;n&gt;]
│  ├─ del-transport            &lt;transport-name&gt; [--force-level &lt;n&gt;]
</pre>

# License

The MIT License (MIT)

Copyright (c) 2023 Artur Henrique Marzano Gonzaga

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
