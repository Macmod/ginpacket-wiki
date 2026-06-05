# 🔥 Firewall (firewall)

**Protocols**: [MS-FASP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-FASP/%5bMS-FASP%5d.pdf).

The Firewall and Advanced Security Protocol (MS-FASP) exposes the Windows Firewall service for remote management via RPC. It allows enumerating, creating, and modifying firewall rules and profiles - accessible to network operators and local admins.

## Usage

### profile

**Syntax:**
```bash
./firewall [auth_flags] profile [-s <store>] [-P <profile>]
```

**Query settings for all firewall profiles:**

```bash
./firewall [auth_flags] profile
```

**Query settings for a specific profile:**

```bash
./firewall [auth_flags] profile -P public
```

### rules

**Syntax:**
```bash
./firewall [auth_flags] rules [-s <store>] [-P <profile>] [-D <direction>] [-a <allow|block>] [--enabled-only] [-n <name>]
```

**List all firewall rules:**

```bash
./firewall [auth_flags] rules
```

**Filter rules by profile, direction, and action:**

```bash
./firewall [auth_flags] rules -P private -D in -a block --enabled-only
```

**Filter rules by name:**

```bash
./firewall [auth_flags] rules -n 'Remote Desktop'
```

### products|networks|adapters|config

**Syntax:**
```bash
./firewall [auth_flags] products|networks|adapters|config
```

**List third-party firewall products registered on the host:**

```bash
./firewall [auth_flags] products
```

**List network connections visible to the firewall:**

```bash
./firewall [auth_flags] networks
```

**List network adapters and their firewall profile assignments:**

```bash
./firewall [auth_flags] adapters
```

**Query the global firewall configuration:**

```bash
./firewall [auth_flags] config
```

### set-config

**Syntax:**
```bash
./firewall [auth_flags] set-config <key> <value> [-s local]
```

**Write a global firewall configuration setting:**

```bash
./firewall [auth_flags] set-config SAIdleTime 300
```

```bash
./firewall [auth_flags] set-config CRLCheck 0
```

### ipsec-csrules|ipsec-mmrules|ipsec-authsets|ipsec-cryptosets|ipsec-sas

**Syntax:**
```bash
./firewall [auth_flags] ipsec-csrules|ipsec-mmrules|ipsec-authsets|ipsec-cryptosets|ipsec-sas
```

**List IPsec connection rules:**

```bash
./firewall [auth_flags] ipsec-csrules
```

**List IPsec main-mode rules:**

```bash
./firewall [auth_flags] ipsec-mmrules
```

**List IPsec authentication sets:**

```bash
./firewall [auth_flags] ipsec-authsets
```

**List IPsec crypto sets:**

```bash
./firewall [auth_flags] ipsec-cryptosets
```

**List active IPsec security associations:**

```bash
./firewall [auth_flags] ipsec-sas
```

### enable|disable

**Syntax:**
```bash
./firewall [auth_flags] enable|disable [-s <store>] [-P <profile>]
```

**Disable the firewall for all profiles:**

```bash
./firewall [auth_flags] disable
```

**Disable the firewall for the public profile only:**

```bash
./firewall [auth_flags] disable -P public
```

**Enable the firewall for the domain profile:**

```bash
./firewall [auth_flags] enable -P domain
```

### add-rule

**Syntax:**
```bash
./firewall [auth_flags] add-rule <name> -D <in|out> [-a <allow|block>] [--protocol <any|tcp|udp>] [-l <ports>] [-r <ports>] [-A <app>] [-P <profile>]
```

**Allow inbound RDP on all profiles:**

```bash
./firewall [auth_flags] add-rule 'Allow RDP' -D in -a allow --protocol tcp -l 3389 -P all
```

**Block outbound SMB on all profiles:**

```bash
./firewall [auth_flags] add-rule 'Block SMB out' -D out -a block --protocol tcp -r 445 -P all
```

**Allow inbound traffic for a specific application (disabled on creation):**

```bash
./firewall [auth_flags] add-rule 'MyApp In' -D in -a allow --protocol any -A 'C:\Tools\app.exe' -P private --enabled=false
```

### set-rule

**Syntax:**
```bash
./firewall [auth_flags] set-rule <rule-id> [--enabled=<bool>]
```

**Enable or disable an existing firewall rule by ID:**

```bash
./firewall [auth_flags] set-rule '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --enabled=false
```

### add-ipsec-csrule

**Syntax:**
```bash
./firewall [auth_flags] add-ipsec-csrule <name> [-a <mode>] [--phase1-auth <id>] [--phase2-crypto <id>] [--phase2-auth <id>]
```

**Add an IPsec connection rule (e.g. bypass without authentication):**

```bash
./firewall [auth_flags] add-ipsec-csrule 'Bypass test' -a do-not-secure
```

**Add an IPsec connection rule requiring mutual authentication:**

```bash
./firewall [auth_flags] add-ipsec-csrule 'Require Auth' -a secure --phase1-auth '{my-authset-id}'
```

### set-ipsec-csrule

**Syntax:**
```bash
./firewall [auth_flags] set-ipsec-csrule <rule-id> [--enabled=<bool>]
```

**Enable or disable an IPsec connection-security rule by ID:**

```bash
./firewall [auth_flags] set-ipsec-csrule '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --enabled=false
```

### add-ipsec-mmrule

**Syntax:**
```bash
./firewall [auth_flags] add-ipsec-mmrule <name> [-P <profile>] --phase1-auth <id> --phase1-crypto <id>
```

**Add an IPsec main-mode (IKE phase-1) rule:**

```bash
./firewall [auth_flags] add-ipsec-mmrule 'Custom MM Rule' --phase1-auth '{my-authset-id}' --phase1-crypto '{my-cryptoset-id}'
```

### set-ipsec-mmrule

**Syntax:**
```bash
./firewall [auth_flags] set-ipsec-mmrule <rule-id> [--enabled=<bool>]
```

**Enable or disable an IPsec main-mode rule by ID:**

```bash
./firewall [auth_flags] set-ipsec-mmrule '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --enabled=false
```

### add-ipsec-authset

**Syntax:**
```bash
./firewall [auth_flags] add-ipsec-authset <set-id> [-n <name>] [--phase <1|2>] [-m <method>]
```

**Add an IPsec authentication set (phase 1 by default, Kerberos):**

```bash
./firewall [auth_flags] add-ipsec-authset '{my-authset-id}' -n 'My Auth Set' --phase 1 -m kerberos
```

**Add a phase-2 authentication set using certificates:**

```bash
./firewall [auth_flags] add-ipsec-authset '{my-authset-id}' -n 'P2 Cert Auth' --phase 2 -m cert
```

### set-ipsec-authset

**Syntax:**
```bash
./firewall [auth_flags] set-ipsec-authset <set-id> [-n <name>] [--phase <1|2>] [-m <method>]
```

**Replace an IPsec authentication set (must use the same set-id):**

```bash
./firewall [auth_flags] set-ipsec-authset '{my-authset-id}' -n 'Updated Auth Set' --phase 1 -m ntlm
```

### add-ipsec-cryptoset

**Syntax:**
```bash
./firewall [auth_flags] add-ipsec-cryptoset <set-id> [-n <name>] [--phase <1|2>] [--key-exchange <alg>] [--encryption <alg>] [--hash <alg>]
```

**Add an IPsec phase-1 crypto set with AES-256 + SHA-256 + DH2048:**

```bash
./firewall [auth_flags] add-ipsec-cryptoset '{my-cryptoset-id}' -n 'My Crypto Set' --phase 1 --key-exchange dh2048 --encryption aes256 --hash sha256
```

**Add a phase-2 crypto set:**

```bash
./firewall [auth_flags] add-ipsec-cryptoset '{my-cryptoset-id}' -n 'P2 Crypto' --phase 2 --encryption aes128 --hash sha1
```

### set-ipsec-cryptoset

**Syntax:**
```bash
./firewall [auth_flags] set-ipsec-cryptoset <set-id> [-n <name>] [--phase <1|2>] [--key-exchange <alg>] [--encryption <alg>] [--hash <alg>]
```

**Replace an IPsec crypto set (must use the same set-id):**

```bash
./firewall [auth_flags] set-ipsec-cryptoset '{my-cryptoset-id}' -n 'Updated Crypto' --phase 1 --key-exchange ecdh256 --encryption aes256 --hash sha384
```

### del-rule

**Syntax:**
```bash
./firewall [auth_flags] del-rule <rule-id> | del-all-rules
```

**Delete a specific firewall rule by ID:**

```bash
./firewall [auth_flags] del-rule '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}'
```

**Delete all firewall rules:**

```bash
./firewall [auth_flags] del-all-rules
```

### del-ipsec-csrule

**Syntax:**
```bash
./firewall [auth_flags] del-ipsec-csrule <rule-id> | del-ipsec-mmrule <rule-id>
```

**Delete an IPsec connection rule by ID:**

```bash
./firewall [auth_flags] del-ipsec-csrule '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}'
```

**Delete an IPsec main-mode rule by ID:**

```bash
./firewall [auth_flags] del-ipsec-mmrule '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}'
```

### del-ipsec-authset

**Syntax:**
```bash
./firewall [auth_flags] del-ipsec-authset <set-id> [--phase <1|2>] | del-ipsec-cryptoset <set-id> [--phase <1|2>]
```

**Delete an IPsec authentication set by ID:**

```bash
./firewall [auth_flags] del-ipsec-authset '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --phase 1
```

**Delete an IPsec crypto set by ID:**

```bash
./firewall [auth_flags] del-ipsec-cryptoset '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --phase 2
```

### del-all-ipsec-csrules

**Syntax:**
```bash
./firewall [auth_flags] del-all-ipsec-csrules | del-all-ipsec-mmrules
```

**Delete all IPsec connection-security rules from the local store:**

```bash
./firewall [auth_flags] del-all-ipsec-csrules
```

**Delete all IPsec main-mode rules from the local store:**

```bash
./firewall [auth_flags] del-all-ipsec-mmrules
```

### del-all-ipsec-authsets

**Syntax:**
```bash
./firewall [auth_flags] del-all-ipsec-authsets [--phase <1|2>] | del-all-ipsec-cryptosets [--phase <1|2>]
```

**Delete all phase-1 authentication sets from the local store:**

```bash
./firewall [auth_flags] del-all-ipsec-authsets --phase 1
```

**Delete all phase-2 crypto sets from the local store:**

```bash
./firewall [auth_flags] del-all-ipsec-cryptosets --phase 2
```

### del-phase1-sas

**Syntax:**
```bash
./firewall [auth_flags] del-phase1-sas | del-phase2-sas
```

**Delete all phase-1 IPsec security associations:**

```bash
./firewall [auth_flags] del-phase1-sas
```

**Delete all phase-2 IPsec security associations:**

```bash
./firewall [auth_flags] del-phase2-sas
```

### dump

**Syntax:**
```bash
./firewall [auth_flags] dump | restore-defaults
```

**Dump the full firewall policy as text:**

```bash
./firewall [auth_flags] dump
```

**Reset the firewall to factory defaults:**

```bash
./firewall [auth_flags] restore-defaults
```
