# 🔏 LSA (lsa)

**Protocols**: [MS-LSAD](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-LSAD/%5bMS-LSAD%5d.pdf).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] policy
```
{% endhint %}

### Query the LSA policy object (audit settings, domain info, quota limits)

```bash
./lsa [auth_flags] policy
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] set-audit [--enable] [--disable] [--event <category>=<none|success|failure|both>]
```
{% endhint %}

### Configure audit event categories

```bash
./lsa [auth_flags] set-audit --enable --event system=both --event logon=success
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] domain-policy
```
{% endhint %}

### Query the Kerberos domain policy (ticket lifetimes, skew)

```bash
./lsa [auth_flags] domain-policy
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] set-domain-policy [--max-service-ticket <dur>] [--max-tgt <dur>] [--max-renew <dur>] [--max-skew <dur>] [--validate-client] [--no-validate-client]
```
{% endhint %}

### Set Kerberos ticket lifetime and skew policy

```bash
./lsa [auth_flags] set-domain-policy --max-service-ticket 10h --max-tgt 10h --max-renew 168h --max-skew 5m
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] get-sd [--security-info <mask>]
```
{% endhint %}

### Read the security descriptor of the LSA policy object

```bash
./lsa [auth_flags] get-sd --security-info 4
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] set-sd --sd <hex> [--security-info <mask>]
```
{% endhint %}

### Write a security descriptor to the LSA policy object

```bash
./lsa [auth_flags] set-sd --sd 01000480200000002c00000000000000 --security-info 4
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] privileges
```
{% endhint %}

### List all privilege constants known to the LSA

```bash
./lsa [auth_flags] privileges
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] lookup-priv -n <privilege-name>
```
{% endhint %}

### Look up a privilege by name and return its LUID

```bash
./lsa [auth_flags] lookup-priv -n SeDebugPrivilege
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] priv-name --high <n> --low <n>
```
{% endhint %}

### Look up the name of a privilege from its high/low LUID components

```bash
./lsa [auth_flags] priv-name --high 0 --low 20
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] accounts
```
{% endhint %}

### List all accounts registered in the LSA policy database

```bash
./lsa [auth_flags] accounts
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] rights [-r <right1,right2>]
```
{% endhint %}

### List accounts holding specific user-rights

```bash
./lsa [auth_flags] rights -r SeServiceLogonRight,SeInteractiveLogonRight
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] account-rights <sid>
```
{% endhint %}

### List all user-rights assigned to an account SID

```bash
./lsa [auth_flags] account-rights S-1-5-21-111-222-333-500
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] account-privs <sid>
```
{% endhint %}

### List all privileges assigned to an account SID

```bash
./lsa [auth_flags] account-privs S-1-5-21-111-222-333-500
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] account-access <sid>
```
{% endhint %}

### Query the system-access flags for an account

```bash
./lsa [auth_flags] account-access S-1-5-21-111-222-333-500
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] set-account-access <sid> <access>
```
{% endhint %}

### Set the system-access flags for an account

```bash
./lsa [auth_flags] set-account-access S-1-5-21-111-222-333-500 4
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] add-rights <sid> -r <right>
```
{% endhint %}

### Grant user-rights to an account SID

```bash
./lsa [auth_flags] add-rights S-1-5-21-111-222-333-500 -r SeServiceLogonRight
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] del-rights <sid> -r <right>
```
{% endhint %}

### Revoke user-rights from an account SID

```bash
./lsa [auth_flags] del-rights S-1-5-21-111-222-333-500 -r SeServiceLogonRight
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] add-account <sid>
```
{% endhint %}

### Register an account SID in the LSA policy database

```bash
./lsa [auth_flags] add-account S-1-5-21-111-222-333-500
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] del-account <sid>
```
{% endhint %}

### Delete an account SID from the LSA policy database

```bash
./lsa [auth_flags] del-account S-1-5-21-111-222-333-500
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] add-secret <name>
```
{% endhint %}

### Create a new LSA secret object

```bash
./lsa [auth_flags] add-secret _SC_MyService
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] secret <name> [--use-tcp]
```
{% endhint %}

### Query metadata about an LSA secret (creation/modification timestamps)

```bash
./lsa [auth_flags] secret _SC_MyService
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] get-secret <name> [--use-tcp]
```
{% endhint %}

### Retrieve the current and previous value of an LSA secret

```bash
./lsa [auth_flags] get-secret _SC_MyService
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] set-secret <name> -v <hex> [--old-value <hex>]
```
{% endhint %}

### Set the current value of an LSA secret

```bash
./lsa [auth_flags] set-secret _SC_MyService -v 4f6c644e547a744d6758
```

### Set both current and previous values of an LSA secret

```bash
./lsa [auth_flags] set-secret _SC_MyService -v 4f6c644e547a744d6758 --old-value 4e65774e547a744d6758
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] del-secret <name>
```
{% endhint %}

### Delete an LSA secret object

```bash
./lsa [auth_flags] del-secret _SC_MyService
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] trusts
```
{% endhint %}

### List trusted domain objects

```bash
./lsa [auth_flags] trusts
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] trust-records -n <domain>
```
{% endhint %}

### Query the forest trust information for a trusted domain

```bash
./lsa [auth_flags] trust-records -n child.example.com
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] trust (-n <domain> | -s <sid>)
```
{% endhint %}

### Query a trust by domain name

```bash
./lsa [auth_flags] trust -n child.example.com
```

### Query a trust by domain SID

```bash
./lsa [auth_flags] trust -s S-1-5-21-111-222-333
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] set-trust -n <domain> [-D <n>] [-T <n>] [--attributes <hex>]
```
{% endhint %}

### Modify attributes of an existing trust

```bash
./lsa [auth_flags] set-trust -n child.example.com -D 3 -T 2 --attributes 0x20
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] add-trust -n <domain> --flat-name <name> -s <sid> [-w <secret>] [-D <n>] [-T <n>]
```
{% endhint %}

### Create a new trust relationship

```bash
./lsa [auth_flags] add-trust -n child.example.com --flat-name CHILD -s S-1-5-21-111-222-333 -D 2 -T 2
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] del-trust <sid>
```
{% endhint %}

### Delete a trust by domain SID

```bash
./lsa [auth_flags] del-trust S-1-5-21-111-222-333
```

{% hint style="info" %}
**Syntax**

```bash
./lsa [auth_flags] set-trust-records -n <domain> [--check]
```
{% endhint %}

### Update trust records for a trusted domain (optionally validate first)

```bash
./lsa [auth_flags] set-trust-records -n child.example.com --check
```
