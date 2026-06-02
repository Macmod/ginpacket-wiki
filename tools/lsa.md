# 🔏 LSA (lsa)

**Protocols**: [MS-LSAD](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-LSAD/%5bMS-LSAD%5d.pdf).

## Subcommands / Usage

### policy

**Syntax:**
```bash
./lsa [auth_flags] policy
```

**Query the LSA policy object (audit settings, domain info, quota limits):**

```bash
./lsa [auth_flags] policy
```

### set-audit

**Syntax:**
```bash
./lsa [auth_flags] set-audit [--enable] [--disable] [--event <category>=<none|success|failure|both>]
```

**Configure audit event categories:**

```bash
./lsa [auth_flags] set-audit --enable --event system=both --event logon=success
```

### domain-policy

**Syntax:**
```bash
./lsa [auth_flags] domain-policy
```

**Query the Kerberos domain policy (ticket lifetimes, skew):**

```bash
./lsa [auth_flags] domain-policy
```

### set-domain-policy

**Syntax:**
```bash
./lsa [auth_flags] set-domain-policy [--max-service-ticket <dur>] [--max-tgt <dur>] [--max-renew <dur>] [--max-skew <dur>] [--validate-client] [--no-validate-client]
```

**Set Kerberos ticket lifetime and skew policy:**

```bash
./lsa [auth_flags] set-domain-policy --max-service-ticket 10h --max-tgt 10h --max-renew 168h --max-skew 5m
```

### get-sd

**Syntax:**
```bash
./lsa [auth_flags] get-sd [--security-info <mask>]
```

**Read the security descriptor of the LSA policy object:**

```bash
./lsa [auth_flags] get-sd --security-info 4
```

### set-sd

**Syntax:**
```bash
./lsa [auth_flags] set-sd --sd <hex> [--security-info <mask>]
```

**Write a security descriptor to the LSA policy object:**

```bash
./lsa [auth_flags] set-sd --sd 01000480200000002c00000000000000 --security-info 4
```

### privileges

**Syntax:**
```bash
./lsa [auth_flags] privileges
```

**List all privilege constants known to the LSA:**

```bash
./lsa [auth_flags] privileges
```

### lookup-priv

**Syntax:**
```bash
./lsa [auth_flags] lookup-priv -n <privilege-name>
```

**Look up a privilege by name and return its LUID:**

```bash
./lsa [auth_flags] lookup-priv -n SeDebugPrivilege
```

### priv-name

**Syntax:**
```bash
./lsa [auth_flags] priv-name --high <n> --low <n>
```

**Look up the name of a privilege from its high/low LUID components:**

```bash
./lsa [auth_flags] priv-name --high 0 --low 20
```

### accounts

**Syntax:**
```bash
./lsa [auth_flags] accounts
```

**List all accounts registered in the LSA policy database:**

```bash
./lsa [auth_flags] accounts
```

### rights

**Syntax:**
```bash
./lsa [auth_flags] rights [-r <right1,right2>]
```

**List accounts holding specific user-rights:**

```bash
./lsa [auth_flags] rights -r SeServiceLogonRight,SeInteractiveLogonRight
```

### account-rights

**Syntax:**
```bash
./lsa [auth_flags] account-rights <sid>
```

**List all user-rights assigned to an account SID:**

```bash
./lsa [auth_flags] account-rights S-1-5-21-111-222-333-500
```

### account-privs

**Syntax:**
```bash
./lsa [auth_flags] account-privs <sid>
```

**List all privileges assigned to an account SID:**

```bash
./lsa [auth_flags] account-privs S-1-5-21-111-222-333-500
```

### account-access

**Syntax:**
```bash
./lsa [auth_flags] account-access <sid>
```

**Query the system-access flags for an account:**

```bash
./lsa [auth_flags] account-access S-1-5-21-111-222-333-500
```

### set-account-access

**Syntax:**
```bash
./lsa [auth_flags] set-account-access <sid> <access>
```

**Set the system-access flags for an account:**

```bash
./lsa [auth_flags] set-account-access S-1-5-21-111-222-333-500 4
```

### add-rights

**Syntax:**
```bash
./lsa [auth_flags] add-rights <sid> -r <right>
```

**Grant user-rights to an account SID:**

```bash
./lsa [auth_flags] add-rights S-1-5-21-111-222-333-500 -r SeServiceLogonRight
```

### del-rights

**Syntax:**
```bash
./lsa [auth_flags] del-rights <sid> -r <right>
```

**Revoke user-rights from an account SID:**

```bash
./lsa [auth_flags] del-rights S-1-5-21-111-222-333-500 -r SeServiceLogonRight
```

### add-account

**Syntax:**
```bash
./lsa [auth_flags] add-account <sid>
```

**Register an account SID in the LSA policy database:**

```bash
./lsa [auth_flags] add-account S-1-5-21-111-222-333-500
```

### del-account

**Syntax:**
```bash
./lsa [auth_flags] del-account <sid>
```

**Delete an account SID from the LSA policy database:**

```bash
./lsa [auth_flags] del-account S-1-5-21-111-222-333-500
```

### add-secret

**Syntax:**
```bash
./lsa [auth_flags] add-secret <name>
```

**Create a new LSA secret object:**

```bash
./lsa [auth_flags] add-secret _SC_MyService
```

### secret

**Syntax:**
```bash
./lsa [auth_flags] secret <name> [--use-tcp]
```

**Query metadata about an LSA secret (creation/modification timestamps):**

```bash
./lsa [auth_flags] secret _SC_MyService
```

### get-secret

**Syntax:**
```bash
./lsa [auth_flags] get-secret <name> [--use-tcp]
```

**Retrieve the current and previous value of an LSA secret:**

```bash
./lsa [auth_flags] get-secret _SC_MyService
```

### set-secret

**Syntax:**
```bash
./lsa [auth_flags] set-secret <name> -v <hex> [--old-value <hex>]
```

**Set the current value of an LSA secret:**

```bash
./lsa [auth_flags] set-secret _SC_MyService -v 4f6c644e547a744d6758
```

**Set both current and previous values of an LSA secret:**

```bash
./lsa [auth_flags] set-secret _SC_MyService -v 4f6c644e547a744d6758 --old-value 4e65774e547a744d6758
```

### del-secret

**Syntax:**
```bash
./lsa [auth_flags] del-secret <name>
```

**Delete an LSA secret object:**

```bash
./lsa [auth_flags] del-secret _SC_MyService
```

### trusts

**Syntax:**
```bash
./lsa [auth_flags] trusts
```

**List trusted domain objects:**

```bash
./lsa [auth_flags] trusts
```

### trust-records

**Syntax:**
```bash
./lsa [auth_flags] trust-records -n <domain>
```

**Query the forest trust information for a trusted domain:**

```bash
./lsa [auth_flags] trust-records -n child.example.com
```

### trust

**Syntax:**
```bash
./lsa [auth_flags] trust (-n <domain> | -s <sid>)
```

**Query a trust by domain name:**

```bash
./lsa [auth_flags] trust -n child.example.com
```

**Query a trust by domain SID:**

```bash
./lsa [auth_flags] trust -s S-1-5-21-111-222-333
```

### set-trust

**Syntax:**
```bash
./lsa [auth_flags] set-trust -n <domain> [-D <n>] [-T <n>] [--attributes <hex>]
```

**Modify attributes of an existing trust:**

```bash
./lsa [auth_flags] set-trust -n child.example.com -D 3 -T 2 --attributes 0x20
```

### add-trust

**Syntax:**
```bash
./lsa [auth_flags] add-trust -n <domain> --flat-name <name> -s <sid> [-w <secret>] [-D <n>] [-T <n>]
```

**Create a new trust relationship:**

```bash
./lsa [auth_flags] add-trust -n child.example.com --flat-name CHILD -s S-1-5-21-111-222-333 -D 2 -T 2
```

### del-trust

**Syntax:**
```bash
./lsa [auth_flags] del-trust <sid>
```

**Delete a trust by domain SID:**

```bash
./lsa [auth_flags] del-trust S-1-5-21-111-222-333
```

### set-trust-records

**Syntax:**
```bash
./lsa [auth_flags] set-trust-records -n <domain> [--check]
```

**Update trust records for a trusted domain (optionally validate first):**

```bash
./lsa [auth_flags] set-trust-records -n child.example.com --check
```
