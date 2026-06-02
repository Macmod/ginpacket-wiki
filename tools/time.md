# 🕒 Time (time)

**Protocols**: [MS-W32T](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-W32T/%5bMS-W32T%5d.pdf).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./time [auth_flags] sync [--wait <sec>] [--sync-flags <n>]
```
{% endhint %}

### Trigger a manual time synchronization

```bash
./time [auth_flags] sync --wait 1 --sync-flags 3
```

{% hint style="info" %}
**Syntax**

```bash
./time [auth_flags] bits
```
{% endhint %}

### Query the W32TM capability bits advertised by the service

```bash
./time [auth_flags] bits
```

{% hint style="info" %}
**Syntax**

```bash
./time [auth_flags] source
```
{% endhint %}

### Query the current time source (NTP server) in use

```bash
./time [auth_flags] source
```

{% hint style="info" %}
**Syntax**

```bash
./time [auth_flags] config
```
{% endhint %}

### Query the global W32TM service configuration

```bash
./time [auth_flags] config
```

{% hint style="info" %}
**Syntax**

```bash
./time [auth_flags] status
```
{% endhint %}

### Query the current time synchronization status

```bash
./time [auth_flags] status
```

{% hint style="info" %}
**Syntax**

```bash
./time [auth_flags] log
```
{% endhint %}

### Query the W32TM event log entries

```bash
./time [auth_flags] log
```

{% hint style="info" %}
**Syntax**

```bash
./time [auth_flags] provider-status <provider-name> [--provider-flags <n>]
```
{% endhint %}

### Query the status of a named time provider

```bash
./time [auth_flags] provider-status NtpClient
```

{% hint style="info" %}
**Syntax**

```bash
./time [auth_flags] provider-config <provider-name> [--provider-flags <n>]
```
{% endhint %}

### Query the configuration of a named time provider

```bash
./time [auth_flags] provider-config NtpClient
```
