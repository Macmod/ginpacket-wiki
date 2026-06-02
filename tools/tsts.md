# 🖥️ Terminal Services (tsts)

**Protocols**: [MS-TSTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-TSTS/%5bMS-TSTS%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
tsts [auth_flags] sessions [-s <state>] [-f <username>]
```

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

### Syntax

```bash
tsts [auth_flags] processes [-s <session-id>]
```

### List running processes across Terminal Services sessions

```bash
./tsts [auth_flags] processes
```

```bash
./tsts [auth_flags] processes -s 1
```

### Syntax

```bash
tsts [auth_flags] policy
```

### Retrieve the Terminal Services machine policy buffer

```bash
./tsts [auth_flags] policy
```

### Syntax

```bash
tsts [auth_flags] session <id> [-c] [-g]
```

### Show session details with optional raw client/config blobs

```bash
./tsts [auth_flags] session 1
```

```bash
./tsts [auth_flags] session 1 -c -g
```

### Syntax

```bash
tsts [auth_flags] connect <src-session> <dst-session> [-P <target-password>]
```

### Connect a source session into a destination session

```bash
./tsts [auth_flags] connect 2 1
```

### Syntax

```bash
tsts [auth_flags] watch [-e <event-list>]
```

### Watch Terminal Services events synchronously until Ctrl+C

```bash
./tsts [auth_flags] watch
```

```bash
./tsts [auth_flags] watch -e logon,logoff,connect,disconnect
```

### Syntax

```bash
tsts [auth_flags] kill-session <id> [-w]
```

### Reset a session forcibly

```bash
./tsts [auth_flags] kill-session 3
```

### Syntax

```bash
tsts [auth_flags] logoff <session-id>
```

### Log off a session via LSM session control

```bash
./tsts [auth_flags] logoff 3
```

### Syntax

```bash
tsts [auth_flags] disconnect <session-id> [-w]
```

### Disconnect a session without logging it off

```bash
./tsts [auth_flags] disconnect 3
```

### Syntax

```bash
tsts [auth_flags] kill-process <pid> [-e <exit-code>]
```

### Terminate a process by PID

```bash
./tsts [auth_flags] kill-process 4242 -e 1
```

### Syntax

```bash
tsts [auth_flags] message <session-id> -T <title> -m <text> [-s <style>] [-o <seconds>] [-a]
```

### Show a message box and optionally wait for the user response

```bash
./tsts [auth_flags] message 1 -T 'Maintenance' -m 'Please save your work.' -s 1 -o 120
```

```bash
./tsts [auth_flags] message 1 -T 'Notice' -m 'This is async.' -a
```

### Syntax

```bash
tsts [auth_flags] listeners
```

### List available Terminal Services listeners

```bash
./tsts [auth_flags] listeners
```

### Syntax

```bash
tsts [auth_flags] stop-listener <name>
```

### Stop a listener such as RDP-Tcp

```bash
./tsts [auth_flags] stop-listener RDP-Tcp
```

### Syntax

```bash
tsts [auth_flags] start-listener <name>
```

### Start a listener such as RDP-Tcp

```bash
./tsts [auth_flags] start-listener RDP-Tcp
```

### Syntax

```bash
tsts [auth_flags] shutdown [-r] [-P] [-l]
```


Shut down, reboot, power off, or log off all sessions via WinStationShutdownSystem  


```bash
./tsts [auth_flags] shutdown -r
```

```bash
./tsts [auth_flags] shutdown -l
```

## Notes
> [!NOTE]
> `tsts watch` polls Terminal Services session state every 2 seconds and reports matching create/delete/rename/connect/disconnect/logon/logoff/state changes until you interrupt it. `tsts message` (without `-a` / `--async`) intentionally uses a no-deadline caller context so it can block synchronously until a user responds or you interrupt it.

> [!NOTE]
> `tsts policy` calls `RpcWinStationGetMachinePolicy`, which the MS-TSTS spec marks as legacy and tied to `POLICY_TS_MACHINE`. On newer Windows versions this commonly returns failure without a detailed status code.