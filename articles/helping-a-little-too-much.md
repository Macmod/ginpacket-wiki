# Helping a Little Too Much: The DFS Replication Helper

For reasons that are unknown to me, one day I decided to read through the `MS-DFSRH` spec. I think I was looking for more methods related to DFS as I thought at the time that `MS-DFSNM` (DFS Namespace Management protocol) didn't have all methods that were relevant for DFS management. One thing stood out immediately - the "DFS Replication Helper" protocol includes DCOM interfaces called `IADProxy` / `IADProxy2` and basically states that these can be used by any local admin to perform write-only LDAP operations (Create, Modify, Delete):

<figure><img src="../.gitbook/assets/615389929-a05a4f92-9ef6-4689-817d-0bc25f6500e2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/615390062-2c966c48-ae95-4272-b1ad-26dc617509ee.png" alt=""><figcaption></figcaption></figure>

I had no idea (and still don't) why is it that DFS needs this sort of thing - maybe to look up important information about AD-integrated DFS namespaces or something like that. All it takes for these interfaces to exist is the **DFS Replication** feature installed on the host.

Let's look at the `Create` call, as `Modify` and `Delete` aren't much different:

<figure><img src="../.gitbook/assets/615390188-3bec1a94-31cb-4369-accf-cf0181e78a4b.png" alt=""><figcaption></figcaption></figure>

Two things are interesting here: the first is the fact the actions are performed with the target's computer account. This is often a "feature", as many organizations still grant sensitive Allow ACEs (Full Control, Generic Write, etc) on critical objects to the `Domain Computers` group or to specific computer objects.

The second is that you can specify the domain controller to receive the operation in the call arguments. Can it be any address, I wondered? The answer is yes: you could even run `Responder` on a VPS, issue one of these calls to a target, and capture NetNTLM hashes for the target's computer account from the LDAP bind, or maybe run ntlmrelayx on a pivot host and relay the credentials into the real DC for a full LDAP shell (confirm):

<figure><img src="../.gitbook/assets/615399073-d8c8afba-2000-49c9-a41f-32ac626f5cc9.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/615397616-31c8ed06-e07d-4237-a7e0-2424b6ad8f7a.png" alt=""><figcaption></figcaption></figure>

If the DC itself has the **DFS Replication** feature, you can also ask it to **connect to itself**, but then the security context would be tied to the `NETWORK SERVICE` user instead of the computer account, changing the scope of actions that can actually be performed. Whenever the DC passed in the call is different from the host receiving it, the call must go through the network, so the `TARGET$` computer account is used instead of the `NETWORK SERVICE` principal. This is standard behavior of virtual accounts such as `NETWORK SERVICE`, as described in [Becoming the Machine, A Virtual Account's Guide To Total Control](https://www.abdulmhsblog.com/posts/iammachine/) by Abdul Mhanni.

What this means is that:

1) If you have admin privileges on a host with DFS Replication, you can take control of its computer account with these calls instead of other well known coercion methods;
2) Instead of capturing NetNTLM or relaying it, you could just use the `Create` / `Modify` / `Delete` calls directly to tell DFSRHelper to perform the action for you;
3) If there are two DCs and one has DFS Replication, you could ask it to perform actions on the other DC's LDAP using its' own computer account;
4) If there is only one DC, you could ask it to perform actions on behalf of `NETWORK SERVICE` if any object allows this principal explicitly in its' DACL.

## Shadow Credentials

One relevant example of what can be accomplished here is using `repldap` to manage the `msDS-KeyCredentialLink` value on the target computer object pointing to a keypair you control (aka "shadow credentials"), giving you the ability to use the matching private key to request a TGT as that computer account via PKINIT, effectively giving persistent Kerberos access to its user without touching LSASS or modifying passwords:

```bash
./repldap [auth_flags] --target-dc WIN-6BKCP1FPPCI keycred add 'CN=WIN-6BKCP1FPPCI,OU=Domain Controllers,DC=creta,DC=local'
```

<figure><img src="../.gitbook/assets/617124036-808d808e-a407-4702-854a-bc00dd55eda5.png" alt=""><figcaption></figcaption></figure>

What makes the DFSRHelper path interesting here is that the write goes through the target's own machine account, so if the machine account has write access to its own msDS-KeyCredentialLink (which is the default), you can do this with a single ./repldap modify call (as long as the target is different from the supplied DC).

## Changing Passwords

### Admin Resets

Both the `changepwd dfsrh` or `repldap modify` subcommands can be used to issue admin password resets via this primitive to computer or user accounts - they are just regular `Modify(Replace)` operations on the corresponding `unicodePwd` attribute. Of course, as usual, the principal that will perform the action (either NETWORK SERVICE when `target==targetDC` or `TARGET$` otherwise) has to have the necessary rights on the object whose password is going to be reset:

```bash
$ ./changepwd dfsrh [auth_flags] \
  -a DN_FOR_TARGETOBJECT -w NewPass@123 \
  --target-dc DCHOSTNAME

# Alternative
$ ./bin/repldap [auth_flags] modify DN_FOR_TARGETOBJECT --replace unicodePwd=Banana@1338 --target-dc DCHOSTNAME
```

<figure><img src="../.gitbook/assets/615908939-d0164dac-1707-4b83-a18f-93b66112308e.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Since password operations in LDAP can only be performed via LDAPS on 636, you must always use the proper DC hostname instead of its IP in `--target-dc` to avoid certificate validation issues between the `target` and the `targetDC`.
{% endhint %}

### Self password changes

Not sure if this is possible yet :)

## Internals

All of this logic is implemented in `DFSRHelper.dll`, and can be called from any admin of the target host. ELABORATE

## Limitations

{% hint style="info" %}
This primitive doesn't seem to cross any security boundaries, as admin privileges are required from the start and with privileges there are other ways of taking over the machine account, but it's definitely an esoteric approach to the problem 🙂
{% endhint %}

{% hint style="warning" %}
The `_AdAttributeData` structure, used to pass a list of arguments to the ADProxy methods, carries exactly **one value field** (not a **list of values** as is usual behavior), and the `DfsrHelper.dll` only forwards that value field through the LDAP operation for `Modify/add` and `Modify/replace` calls (not for `Modify/delete`). The practical consequences:

1) For attribute modifications (`repldap modify`), **replacements** (`--replace`) clear all existing values of the attribute and set the single supplied value - there is no way to replace a multi-valued attribute with multiple new values in one call;
2) For attribute modifications (`repldap modify`), **deletes** (`--delete`) always remove all values of the attribute regardless of what value is supplied - value-specific deletes are not supported.
3) For object creation (`repldap create`), **multi-valued attributes cannot be set** - passing the same attribute name twice issues two separate LDAP Add operations on the same attribute, which AD rejects sometimes (e.g. `objectClass` may return an Object Class Violation). The typed `repldap create [XXX]` subcommands already handle these constraints. For **custom creations** (`repldap create custom`) more testing is needed to verify the scope of this limitation.
{% endhint %}
