# Ginpacket

🍸 Ginpacket is a collection of tools written in Go to work with network protocols, mostly aimed at Windows / Active Directory environments.

This project wraps complex protocol families behind focused commands, exposing a subset of features of these protocols under intuitive and uniform commandlines.

# Protocols implemented
* Kerberos ([RFC 4120](https://datatracker.ietf.org/doc/html/rfc4120) and [MS-KILE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-KILE/%5bMS-KILE%5d.pdf))
	* PKINIT ([MS-PKCA](https://winprotocoldoc.z19.web.core.windows.net/MS-PKCA/%5bMS-PKCA%5d.pdf) and [RFC 4556](https://datatracker.ietf.org/doc/html/rfc4556))
	* S4U ([MS-SFU](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SFU/%5bMS-SFU%5d.pdf))
	* Change / set password ([RFC 3244](https://datatracker.ietf.org/doc/html/rfc3244))
* SMB2/3 ([MS-SMB2](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SMB2/%5bMS-SMB2%5d.pdf))
* LDAP ([RFC 4511](https://datatracker.ietf.org/doc/html/rfc4511) and parts of [MS-ADTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-ADTS/%5bMS-ADTS%5d.pdf))
* MSRPC ([MS-RPCE](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-RPCE/%5bMS-RPCE%5d.pdf))
	* Endpoint mapper
	* Remote Authorization API ([MS-RAA](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-raa/))
	* Directory Replication Service ([MS-DRSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DRSR/%5bMS-DRSR%5d.pdf))
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

Ginpacket's philosophy is to be **useful**, **easy** and **comprehensive** - if a feature is exposed by Microsoft and it could be useful for any sort of research or task, I probably tried to implement a suitable interface for it, but of course not all opnums of the RPC-based protocols were implemented - some RPC calls that still exist are legacy features that don't do anything or don't work in modern systems, or features that are too niche and offer little value for most users.

Regardless, most RPC features we did implement can be thought as 1-1 maps from cmdline args to corresponding opnums, although some implement more elaborated algorithms (chaining multiple calls) to perform more specific actions (e.g. `dcsync`, `reg secrets`, `sam dump`, etc). 

For a complete reference of the commands supported by Ginpacket's tools, check the [Subcommands Map](#subcommands-map) or the [Usage](#usage) section.

## Installation

```bash
# Clone
git clone https://github.com/Macmod/ginpacket
cd ginpacket

# Build all commands into ./bin (uses build.sh)
chmod +x build.sh
./build.sh
```

## Authentication

All tools share common authentication flags through `adauth` and accept the same credential styles.

```bash
# User + Password
./tool -t <TARGET> -u 'DOMAIN\user' -p <password> <subcommand> [...]

# User + NT hash
./tool -t <TARGET> -u 'DOMAIN\user' -H <NT_HASH> <subcommand> [...]

# Kerberos with AES key
./tool -t <TARGET> -u 'DOMAIN\user' --aes-key <hex> --dc <DC> -k <subcommand> [...]

# Kerberos with ccache
./tool -t <TARGET> --ccache <user>.ccache <subcommand> [...]

# Certificate auth with PFX (PKINIT / pass-the-certificate)
./tool -t <TARGET> -u 'DOMAIN\user' --pfx <cert.pfx> <subcommand> [...]

# Certificate auth with PEM + KEY (--crt / --key)
./tool -t <TARGET> -u 'DOMAIN\user' --crt <cert.pem> --key <certkey.pem> <subcommand> [...]
```

> [!IMPORTANT]
> If using a Kerberos-based auth method, such as any method with `-k`, `--ccache`, or certificates (which use PKINIT to implicitly exchange certificates for Kerberos tickets to use in the RPC auth flow), you must either set `--dc` to your KDC or let it be resolved by your DNS (in which case you may provide `--dns` to specify a custom DNS server).

> [!IMPORTANT]
> When using cross-domain authentication, proper DNS resolution is needed for the names of all domains in the referral chain (except the first, which can be provided explicitly with `--dc`).

In the usage examples below, `[auth_flags]` is a shorthand for any combination of the flags above (e.g. `-t <TARGET> -u 'DOMAIN\user' -p <password>` or `-t <TARGET> --ccache <file>`).

`-t` / `--target` is either an IP or hostname of the target system - it's always part of `[auth_flags]` and is required for all tools except `gettgt` and `getst` (which use only `--dc` instead).