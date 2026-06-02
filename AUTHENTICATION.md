# Authentication

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

{% hint style="warning" %}
If using a Kerberos-based auth method, such as any method with `-k`, `--ccache`, or certificates (which use PKINIT to implicitly exchange certificates for Kerberos tickets to use in the RPC auth flow), you must either set `--dc` to your KDC or let it be resolved by your DNS (in which case you may provide `--dns` to specify a custom DNS server).
{% endhint %}

{% hint style="warning" %}
When using cross-domain authentication, proper DNS resolution is needed for the names of all domains in the referral chain (except the first, which can be provided explicitly with `--dc`).
{% endhint %}

In the usage examples below, `[auth_flags]` is a shorthand for any combination of the flags above (e.g. `-t <TARGET> -u 'DOMAIN\user' -p <password>` or `-t <TARGET> --ccache <file>`).

`-t` / `--target` is either an IP or hostname of the target system - it's always part of `[auth_flags]` and is required for all tools except `gettgt` and `getst` (which use only `--dc` instead).