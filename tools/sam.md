# 👤 SAM (sam)

**Protocols**: [MS-SAMR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-SAMR/%5bMS-SAMR%5d.pdf).

## Subcommands / Usage

### `domains`

```bash
./sam [auth_flags] domains
```

**List all SAM domains on the target:**

```bash
./sam [auth_flags] domains
```

### `domain`

```bash
./sam [auth_flags] domain [-d <name>]
```

**Show detailed info for a domain:**

```bash
./sam [auth_flags] domain -d EXAMPLE
```

### `set-domain`

```bash
./sam [auth_flags] set-domain [-d <name>] [--min-pwd-len <n>] [--lockout-threshold <n>] [--lockout-window <dur>] [--lockout-duration <dur>]
```

**Modify domain-level password and lockout policy:**

```bash
./sam [auth_flags] set-domain -d EXAMPLE --min-pwd-len 8 --lockout-threshold 5 --lockout-window 30m --lockout-duration 30m
```

### `password-policy`

```bash
./sam [auth_flags] password-policy [-d <name>]
```

**Query the domain password policy:**

```bash
./sam [auth_flags] password-policy -d EXAMPLE
```

### `get-acl`

```bash
./sam [auth_flags] get-acl [-d <name>]
```

**Read the domain object's security descriptor:**

```bash
./sam [auth_flags] get-acl -d EXAMPLE
```

### `set-acl`

```bash
./sam [auth_flags] set-acl --sd <hex> [-d <name>]
```

**Write a security descriptor to the domain object:**

```bash
./sam [auth_flags] set-acl --sd 01000480200000002c00000000000000 -d EXAMPLE
```

### `users`

```bash
./sam [auth_flags] users [-d <name>]
```

**Enumerate all user accounts in a domain:**

```bash
./sam [auth_flags] users -d EXAMPLE
```

### `display`

```bash
./sam [auth_flags] display [-d <name>] [--type <users|machines|groups>] [--prefix <str>]
```

**Display accounts with optional prefix filtering (users, machines, or groups):**

```bash
./sam [auth_flags] display -d EXAMPLE --type users --prefix adm
```

### `user`

```bash
./sam [auth_flags] user <username|RID> [-d <name>]
```

**Show full attributes for a user account:**

```bash
./sam [auth_flags] user Administrator -d EXAMPLE
```

### `add-user`

```bash
./sam [auth_flags] add-user <name> [-d <name>] [-N <s>] [-D <s>] [-w <s>] [--disable]
```

**Create a new user account:**

```bash
./sam [auth_flags] add-user jdoe -d EXAMPLE -N 'John Doe' -D 'Test user' -w 'P@ssw0rd!'
```

### `del-user`

```bash
./sam [auth_flags] del-user <username|RID> [-d <name>]
```

**Delete a user account:**

```bash
./sam [auth_flags] del-user jdoe -d EXAMPLE
```

### `set-user`

```bash
./sam [auth_flags] set-user <username|RID> [-d <name>] [--full-name <s>] [--description <s>] [--password <s>] [--expires <RFC3339|never>] [--enable-uac <flag>] [--disable-uac <flag>]
```

**Modify user account attributes or password:**

```bash
./sam [auth_flags] set-user jdoe -d EXAMPLE --password 'NewP@ssw0rd!' --expires never
```

### `user-groups`

```bash
./sam [auth_flags] user-groups <username|RID> [-d <name>]
```

**List all global groups a user belongs to:**

```bash
./sam [auth_flags] user-groups Administrator -d EXAMPLE
```

### `user-aliases`

```bash
./sam [auth_flags] user-aliases <username|RID> [-d <name>]
```

**List all aliases (local groups) a user belongs to:**

```bash
./sam [auth_flags] user-aliases Administrator -d EXAMPLE
```

### `validate-password`

```bash
./sam [auth_flags] validate-password <password> [-d <name>] [--operation <auth|change|reset>]
```

**Validate a password against the domain policy:**

```bash
./sam [auth_flags] validate-password 'P@ssw0rd!' -d EXAMPLE --operation auth
```

### `groups`

```bash
./sam [auth_flags] groups [-d <name>]
```

**Enumerate all global groups in a domain:**

```bash
./sam [auth_flags] groups -d EXAMPLE
```

### `group`

```bash
./sam [auth_flags] group <name|RID> [-d <name>]
```

**Show full attributes for a global group:**

```bash
./sam [auth_flags] group 'Domain Admins' -d EXAMPLE
```

### `add-group`

```bash
./sam [auth_flags] add-group <name> [-d <name>]
```

**Create a new global group:**

```bash
./sam [auth_flags] add-group TestGroup -d EXAMPLE
```

### `del-group`

```bash
./sam [auth_flags] del-group <name|RID> [-d <name>]
```

**Delete a global group:**

```bash
./sam [auth_flags] del-group TestGroup -d EXAMPLE
```

### `group-members`

```bash
./sam [auth_flags] group-members <name|RID> [-d <name>] [--resolve-sids]
```

**List members of a global group:**

```bash
./sam [auth_flags] group-members 'Domain Admins' -d EXAMPLE --resolve-sids
```

### `add-group-member`

```bash
./sam [auth_flags] add-group-member <group> <member-username|RID> [-d <name>]
```

**Add a member to a global group:**

```bash
./sam [auth_flags] add-group-member 'Domain Admins' jdoe -d EXAMPLE
```

### `del-group-member`

```bash
./sam [auth_flags] del-group-member <group> <member-username|RID> [-d <name>]
```

**Remove a member from a global group:**

```bash
./sam [auth_flags] del-group-member 'Domain Admins' jdoe -d EXAMPLE
```

### `set-group`

```bash
./sam [auth_flags] set-group <name|RID> [-d <name>] [--name <s>] [--description <s>]
```

**Rename or update the description of a global group:**

```bash
./sam [auth_flags] set-group TestGroup -d EXAMPLE --name RenamedGroup --description 'Updated desc'
```

### `set-member-attrs`

```bash
./sam [auth_flags] set-member-attrs <group> <member-username|RID> [-d <name>] [--attributes <hex>]
```

**Set per-member attributes on a group membership:**

```bash
./sam [auth_flags] set-member-attrs 'Domain Admins' jdoe -d EXAMPLE --attributes 0x7
```

### `aliases`

```bash
./sam [auth_flags] aliases [-d <name>] [--builtin]
```

**Enumerate all aliases (local groups) in a domain:**

```bash
./sam [auth_flags] aliases -d EXAMPLE
```

### `alias`

```bash
./sam [auth_flags] alias <name|RID> [-d <name>] [--builtin]
```

**Show full attributes for an alias:**

```bash
./sam [auth_flags] alias Administrators --builtin
```

### `add-alias`

```bash
./sam [auth_flags] add-alias <name> [-d <name>]
```

**Create a new alias (local group):**

```bash
./sam [auth_flags] add-alias TestAlias -d EXAMPLE
```

### `del-alias`

```bash
./sam [auth_flags] del-alias <name|RID> [-d <name>] [--builtin]
```

**Delete an alias:**

```bash
./sam [auth_flags] del-alias TestAlias -d EXAMPLE
```

### `alias-members`

```bash
./sam [auth_flags] alias-members <name|RID> [-d <name>] [--builtin] [--resolve-sids]
```

**List members of an alias:**

```bash
./sam [auth_flags] alias-members Administrators --builtin --resolve-sids
```

### `alias-membership`

```bash
./sam [auth_flags] alias-membership <sid> [-d <name>] [--builtin]
```

**List all alias memberships for a given SID:**

```bash
./sam [auth_flags] alias-membership S-1-5-21-111-222-333-1105 -d EXAMPLE
```

### `add-alias-member`

```bash
./sam [auth_flags] add-alias-member <alias> <sid|username> [-d <name>] [--builtin]
```

**Add a member (by SID or username) to an alias:**

```bash
./sam [auth_flags] add-alias-member Administrators S-1-5-21-111-222-333-1105 --builtin
```

### `del-alias-member`

```bash
./sam [auth_flags] del-alias-member <alias> <sid|username> [-d <name>] [--builtin]
```

**Remove a member from an alias:**

```bash
./sam [auth_flags] del-alias-member Administrators S-1-5-21-111-222-333-1105 --builtin
```

### `add-alias-members`

```bash
./sam [auth_flags] add-alias-members <alias> <sid|username>... [-d <name>] [--builtin]
```

**Add multiple members to an alias in one call:**

```bash
./sam [auth_flags] add-alias-members Administrators S-1-5-21-111-222-333-1105 S-1-5-21-111-222-333-1106 --builtin
```

### `del-alias-members`

```bash
./sam [auth_flags] del-alias-members <alias> <sid|username>... [-d <name>] [--builtin]
```

**Remove multiple members from an alias in one call:**

```bash
./sam [auth_flags] del-alias-members Administrators S-1-5-21-111-222-333-1105 S-1-5-21-111-222-333-1106 --builtin
```

### `set-alias`

```bash
./sam [auth_flags] set-alias <name|RID> [-d <name>] [--builtin] [--name <s>] [--description <s>]
```

**Rename or update the description of an alias:**

```bash
./sam [auth_flags] set-alias TestAlias -d EXAMPLE --name RenamedAlias --description 'Updated desc'
```

### `purge-sid`

```bash
./sam [auth_flags] purge-sid <sid> [-d <name>] [--builtin]
```

**Remove all alias/group memberships for a stale SID (cross-domain cleanup):**

```bash
./sam [auth_flags] purge-sid S-1-5-21-111-222-333-1105 -d EXAMPLE
```

### `lookup-names`

```bash
./sam [auth_flags] lookup-names <name>... [-d <name>]
```

**Resolve one or more account names to RIDs and types:**

```bash
./sam [auth_flags] lookup-names Administrator jdoe -d EXAMPLE
```

### `lookup-rids`

```bash
./sam [auth_flags] lookup-rids <rid>... [-d <name>]
```

**Resolve one or more RIDs to account names and types:**

```bash
./sam [auth_flags] lookup-rids 500 512 -d EXAMPLE
```

### `rid-to-sid`

```bash
./sam [auth_flags] rid-to-sid <rid>
```

**Convert a RID to its full SID within the bound domain:**

```bash
./sam [auth_flags] rid-to-sid 500
```

### `set-dsrm-password`

```bash
./sam [auth_flags] set-dsrm-password <new-password>
```

**Set the Directory Services Restore Mode password on a DC:**

```bash
./sam [auth_flags] set-dsrm-password 'NewDSRM@Passw0rd!'
```
