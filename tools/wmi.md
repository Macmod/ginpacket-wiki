# 🧠 WMI (wmi)

**Protocols**: [MS-DCOM](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DCOM/%5bMS-DCOM%5d.pdf), [MS-WMI](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-WMI/%5bMS-WMI%5d.pdf).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] [-n <namespace>] query <wql> [-f <fields>] [-L <n>]
```
{% endhint %}

### Run a WQL query against a WMI namespace

```bash
./wmi [auth_flags] -n //./root/cimv2 query 'SELECT Caption,Version,BuildNumber FROM Win32_OperatingSystem' -L 10
```

### Run a WQL query with field filtering and a row limit

```bash
./wmi [auth_flags] query 'SELECT * FROM Win32_Process' -f Name,ProcessId,CommandLine -L 20
```

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] namespaces
```
{% endhint %}

### List all WMI namespaces on the host

```bash
./wmi [auth_flags] namespaces
```

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] classes
```
{% endhint %}

### List all classes in the current namespace

```bash
./wmi [auth_flags] classes
```

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] class <class>
```
{% endhint %}

### List all properties of a WMI class

```bash
./wmi [auth_flags] class Win32_Process
```

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] methods <class>
```
{% endhint %}

### List all methods of a WMI class

```bash
./wmi [auth_flags] methods Win32_Process
```

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] instance <object-path>
```
{% endhint %}

### Retrieve a WMI object instance by path

```bash
./wmi [auth_flags] instance "Win32_Service.Name='W32Time'"
```

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] invoke <object::method> [--arg <key=value>]
```
{% endhint %}

### Invoke a method on a WMI object

```bash
./wmi [auth_flags] invoke Win32_Process::Create --arg 'CommandLine=cmd.exe /c whoami'
```

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] exec <command>
```
{% endhint %}

### Execute a command via WMI (Win32_Process.Create shorthand)

```bash
./wmi [auth_flags] exec 'cmd.exe /c hostname'
```

{% hint style="info" %}
**Syntax**

```bash
./wmi [auth_flags] del-instance <object-path>
```
{% endhint %}

### Delete a WMI object instance by path

```bash
./wmi [auth_flags] del-instance "Win32_Process.Handle='1234'"
```
