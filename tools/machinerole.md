# 🧭 Machine Role (machinerole)

**Protocols**: [MS-DSSP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DSSP/%5bMS-DSSP%5d.pdf).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./machinerole [auth_flags] [--use-named-pipe]
```
{% endhint %}

### Query the machine's domain role and DS state via TCP

```bash
./machinerole [auth_flags]
```

### Query using the named pipe transport instead of TCP

```bash
./machinerole [auth_flags] --use-named-pipe
```
