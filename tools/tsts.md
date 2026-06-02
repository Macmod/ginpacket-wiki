# 🖥️ Terminal Services (tsts)

**Protocols**: [MS-TSTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-TSTS/%5bMS-TSTS%5d.pdf).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] sessions [-s <state>] [-f <username>]
```
{% endhint %}

### Enumerate Terminal Services sessions, optionally filtering by state or user

```bash
./tsts [auth_flags] sessions
```

```bash
./tsts [auth_flags] sessions -s active
```

```bash
./tsts [auth_flags] sessions -f administrator
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] processes [-s <session-id>]
```
{% endhint %}

### List running processes across Terminal Services sessions

```bash
./tsts [auth_flags] processes
```

```bash
./tsts [auth_flags] processes -s 1
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] policy
```
{% endhint %}

### Retrieve the Terminal Services machine policy buffer

```bash
./tsts [auth_flags] policy
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] session <id> [-c] [-g]
```
{% endhint %}

### Show session details with optional raw client/config blobs

```bash
./tsts [auth_flags] session 1
```

```bash
./tsts [auth_flags] session 1 -c -g
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] connect <src-session> <dst-session> [-P <target-password>]
```
{% endhint %}

### Connect a source session into a destination session

```bash
./tsts [auth_flags] connect 2 1
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] watch [-e <event-list>]
```
{% endhint %}

### Watch Terminal Services events synchronously until Ctrl+C

```bash
./tsts [auth_flags] watch
```

```bash
./tsts [auth_flags] watch -e logon,logoff,connect,disconnect
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] kill-session <id> [-w]
```
{% endhint %}

### Reset a session forcibly

```bash
./tsts [auth_flags] kill-session 3
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] logoff <session-id>
```
{% endhint %}

### Log off a session via LSM session control

```bash
./tsts [auth_flags] logoff 3
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] disconnect <session-id> [-w]
```
{% endhint %}

### Disconnect a session without logging it off

```bash
./tsts [auth_flags] disconnect 3
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] kill-process <pid> [-e <exit-code>]
```
{% endhint %}

### Terminate a process by PID

```bash
./tsts [auth_flags] kill-process 4242 -e 1
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] message <session-id> -T <title> -m <text> [-s <style>] [-o <seconds>] [-a]
```
{% endhint %}

### Show a message box and optionally wait for the user response

```bash
./tsts [auth_flags] message 1 -T 'Maintenance' -m 'Please save your work.' -s 1 -o 120
```

```bash
./tsts [auth_flags] message 1 -T 'Notice' -m 'This is async.' -a
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] listeners
```
{% endhint %}

### List available Terminal Services listeners

```bash
./tsts [auth_flags] listeners
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] stop-listener <name>
```
{% endhint %}

### Stop a listener such as RDP-Tcp

```bash
./tsts [auth_flags] stop-listener RDP-Tcp
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] start-listener <name>
```
{% endhint %}

### Start a listener such as RDP-Tcp

```bash
./tsts [auth_flags] start-listener RDP-Tcp
```

{% hint style="info" %}
**Syntax**

```bash
./tsts [auth_flags] shutdown [-r] [-P] [-l]
```
{% endhint %}


Shut down, reboot, power off, or log off all sessions via WinStationShutdownSystem  


```bash
./tsts [auth_flags] shutdown -r
```

```bash
./tsts [auth_flags] shutdown -l
```

## Notes
{% hint style="info" %}
`tsts watch` polls Terminal Services session state every 2 seconds and reports matching create/delete/rename/connect/disconnect/logon/logoff/state changes until you interrupt it. `tsts message` (without `-a` / `--async`) intentionally uses a no-deadline caller context so it can block synchronously until a user responds or you interrupt it.
{% endhint %}

{% hint style="info" %}
`tsts policy` calls `RpcWinStationGetMachinePolicy`, which the MS-TSTS spec marks as legacy and tied to `POLICY_TS_MACHINE`. On newer Windows versions this commonly returns failure without a detailed status code.
{% endhint %}