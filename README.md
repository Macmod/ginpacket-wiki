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
Despite the name, `ginpacket` is not a Go port of [impacket](https://github.com/fortra/impacket). It is an opinionated toolkit with independently reworked implementations of some features that overlap with impacket, as well as implementations that go beyond what impacket provides. The two projects share goals but differ in scope and design.
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

For a complete reference of the commands supported by Ginpacket's tools, check the [Subcommands Map](#subcommands-map) or the [Usage](#usage) section.