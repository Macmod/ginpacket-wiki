# 🖥️ Terminal Services (tsts)

**Protocols**: [MS-TSTS](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-TSTS/%5bMS-TSTS%5d.pdf).

The Terminal Services Terminal Server Runtime Interface (MS-TSTS) exposes RDP session management on a Windows Terminal Server or any Windows host with Remote Desktop enabled. It allows enumerating active and disconnected sessions, sending messages, connecting or disconnecting sessions, and watching session state changes in real time.

## Usage

### sessions

**Syntax:**
```bash
./tsts [auth_flags] sessions [-s <state>] [-f <username>] [--check-lock] [--own]
```

**Enumerate Terminal Services sessions, optionally filtering by state or user:**

```bash
./tsts [auth_flags] sessions
```

```bash
./tsts [auth_flags] sessions -s active
```

```bash
./tsts [auth_flags] sessions -f administrator
```

**Include desktop lock state per session (extra RPC round-trip):**

```bash
./tsts [auth_flags] sessions --check-lock
```

**Restrict to sessions owned by the authenticated caller:**

```bash
./tsts [auth_flags] sessions --own
```

### processes

**Syntax:**
```bash
./tsts [auth_flags] processes [-s <session-id>]
```

**List running processes across Terminal Services sessions:**

```bash
./tsts [auth_flags] processes
```

```bash
./tsts [auth_flags] processes -s 1
```

### policy

**Syntax:**
```bash
./tsts [auth_flags] policy
```

**Retrieve the Terminal Services machine policy buffer:**

```bash
./tsts [auth_flags] policy
```

### session

**Syntax:**
```bash
./tsts [auth_flags] session <id> [-c] [-g]
```

**Show session details with optional raw client/config blobs:**

```bash
./tsts [auth_flags] session 1
```

```bash
./tsts [auth_flags] session 1 -c -g
```

### connect

**Syntax:**
```bash
./tsts [auth_flags] connect <src-session> <dst-session> [-P <target-password>]
```

**Connect a source session into a destination session:**

```bash
./tsts [auth_flags] connect 2 1
```

{% hint style="info" %}
Moves all processes from the source session into the destination session and disconnects the source. If `-P` is not provided, the target session will be locked before the change.
{% endhint %}

### watch

**Syntax:**
```bash
./tsts [auth_flags] watch [-e <event-list>] [-m <method>] [--wait-timeout <duration>]
```

**Watch Terminal Services events synchronously until Ctrl+C:**

```bash
./tsts [auth_flags] watch
```

```bash
./tsts [auth_flags] watch -e logon,logoff,connect,disconnect
```

```bash
./tsts [auth_flags] watch -m polling
```

```bash
./tsts [auth_flags] watch -m waitsysevent --wait-timeout 30s
```

### kill-session

**Syntax:**
```bash
./tsts [auth_flags] kill-session <id> [-w]
```

**Reset a session forcibly:**

```bash
./tsts [auth_flags] kill-session 3
```

### logoff

**Syntax:**
```bash
./tsts [auth_flags] logoff <session-id>
```

**Log off a session via LSM session control:**

```bash
./tsts [auth_flags] logoff 3
```

### disconnect

**Syntax:**
```bash
./tsts [auth_flags] disconnect <session-id> [-w]
```

**Disconnect a session without logging it off:**

```bash
./tsts [auth_flags] disconnect 3
```

### kill-process

**Syntax:**
```bash
./tsts [auth_flags] kill-process <pid> [-e <exit-code>]
```

**Terminate a process by PID:**

```bash
./tsts [auth_flags] kill-process 4242 -e 1
```

### message

**Syntax:**
```bash
./tsts [auth_flags] message <session-id> -T <title> -m <text> [-s <style>] [-o <seconds>] [-a]
```

**Show a message box and optionally wait for the user response:**

```bash
./tsts [auth_flags] message 1 -T 'Maintenance' -m 'Please save your work.' -s 1 -o 120
```

```bash
./tsts [auth_flags] message 1 -T 'Notice' -m 'This is async.' -a
```

### listeners

**Syntax:**
```bash
./tsts [auth_flags] listeners
```

**List available Terminal Services listeners:**

```bash
./tsts [auth_flags] listeners
```

### stop-listener

**Syntax:**
```bash
./tsts [auth_flags] stop-listener <name>
```

**Stop a listener such as RDP-Tcp:**

```bash
./tsts [auth_flags] stop-listener RDP-Tcp
```

### start-listener

**Syntax:**
```bash
./tsts [auth_flags] start-listener <name>
```

**Start a listener such as RDP-Tcp:**

```bash
./tsts [auth_flags] start-listener RDP-Tcp
```

### shutdown

**Syntax:**
```bash
./tsts [auth_flags] shutdown [-r] [-P] [-l]
```

**Shut down, reboot, power off, or log off all sessions via WinStationShutdownSystem:**

```bash
./tsts [auth_flags] shutdown -r
```

```bash
./tsts [auth_flags] shutdown -l
```

## Notes
{% hint style="info" %}
`tsts watch` supports two methods: `waitsysevent` (default) uses `RpcWinStationWaitSystemEvent` to block until the server signals a change, then diffs session snapshots for per-session detail; `polling` snapshots session state every 2 seconds and diffs directly. Both report create/delete/rename/connect/disconnect/logon/logoff/state-change events and print a summary count on Ctrl-C. With `--wait-timeout 0` (default) the event call blocks indefinitely; pass a duration such as `30s` to have it return an error if no event fires within that window. If an event fires but the snapshot diff produces no recognisable change, an `[Unknown]` line with the raw event mask is shown.
{% endhint %}

{% hint style="info" %}
`tsts policy` calls `RpcWinStationGetMachinePolicy`, which the MS-TSTS spec marks as legacy and tied to `POLICY_TS_MACHINE`. On newer Windows versions this commonly returns failure without a detailed status code.
{% endhint %}