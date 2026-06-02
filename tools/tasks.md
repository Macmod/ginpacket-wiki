# 🗓️ Tasks (tasks)

**Protocols**: [MS-TSCH](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-TSCH/%5bMS-TSCH%5d.pdf), ATSvc.

## Subcommands / Usage

### Syntax

```bash
tasks [auth_flags] dump
```

### Dump the full task scheduler folder tree (v2 only)

```bash
./tasks [auth_flags] dump
```

### Syntax

```bash
tasks [auth_flags] query [--include-hidden]
```

### List all task paths, optionally including hidden tasks

```bash
./tasks [auth_flags] query --include-hidden
```

### Syntax

```bash
tasks [auth_flags] task <path> [--format xml]
```

### Show full task details (info + embedded XML) for a v2 task

```bash
./tasks [auth_flags] task '\Microsoft\Windows\UpdateOrchestrator\Schedule Scan'
```

### Show only the raw XML definition of a task

```bash
./tasks [auth_flags] task '\MyTask' --format xml
```

### Syntax

```bash
tasks [auth_flags] folders [path]
```

### List immediate subfolders of a task scheduler folder path (v2 only)

```bash
./tasks [auth_flags] folders
```

```bash
./tasks [auth_flags] folders '\Microsoft\Windows'
```

### Syntax

```bash
tasks [auth_flags] xml <path>
```

### Export a task's raw XML definition

```bash
./tasks [auth_flags] xml '\MyTask'
```

### Syntax

```bash
tasks [auth_flags] add (-P <path> -X <xml> | --use-v1 -c <cmd> --time <HH:MM> [schedule flags])
```

### Register a v2 task from an XML file

```bash
./tasks [auth_flags] add -P '\MyTask' -X "$(Get-Content task.xml -Raw)"
```

### Register a v1 ATSvc job with a schedule

```bash
./tasks [auth_flags] add --use-v1 -c 'cmd.exe /c whoami > C:\temp\t.txt' --time 09:30 --days-of-week mon,wed,fri --periodic
```

### Syntax

```bash
tasks [auth_flags] enable|disable <path>
```

### Enable a disabled task

```bash
./tasks [auth_flags] enable '\MyTask'
```

### Disable an enabled task

```bash
./tasks [auth_flags] disable '\MyTask'
```

### Syntax

```bash
tasks [auth_flags] run <path>
```

### Run a task immediately

```bash
./tasks [auth_flags] run '\MyTask'
```

### Syntax

```bash
tasks [auth_flags] stop ([path] | -G <instance-guid>)
```

### Stop all running instances of a task by path

```bash
./tasks [auth_flags] stop '\MyTask'
```

### Stop a single running instance by GUID

```bash
./tasks [auth_flags] stop -G '{guid}'
```

### Syntax

```bash
tasks [auth_flags] rename <current-path> <new-path>
```

### Rename a task to a new path

```bash
./tasks [auth_flags] rename '\MyTask' '\MyRenamedTask'
```

### Syntax

```bash
tasks [auth_flags] add-folder <path> [-D <sddl>]
```

### Create a task scheduler folder

```bash
./tasks [auth_flags] add-folder '\MyFolder'
```

### Syntax

```bash
tasks [auth_flags] instances <path>
```

### List currently running instances of a task

```bash
./tasks [auth_flags] instances '\MyTask'
```

### Syntax

```bash
tasks [auth_flags] get-sddl <path> [--parse-dacl]
```

### Read the security descriptor of a task

```bash
./tasks [auth_flags] get-sddl '\MyTask'
```

### Read and parse the DACL of a task's security descriptor

```bash
./tasks [auth_flags] get-sddl '\MyTask' --parse-dacl
```

### Syntax

```bash
tasks [auth_flags] set-sddl <path> -D <sddl>
```

### Write a security descriptor to a task

```bash
./tasks [auth_flags] set-sddl '\MyTask' -D 'D:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SY)'
```

### Syntax

```bash
tasks [auth_flags] missed-runs <path>
```

### List missed runs for a task

```bash
./tasks [auth_flags] missed-runs '\MyTask'
```

### Syntax

```bash
tasks [auth_flags] del ([path] | --use-v1 (--job-id | --min-job-id/--max-job-id))
```

### Delete a v2 task by path

```bash
./tasks [auth_flags] del '\MyTask'
```

### Delete a single v1 ATSvc job by ID

```bash
./tasks [auth_flags] del --use-v1 --job-id 1
```

### Delete a range of v1 ATSvc jobs by ID range

```bash
./tasks [auth_flags] del --use-v1 --min-job-id 2 --max-job-id 5
```

### Syntax

```bash
tasks [auth_flags] del-folder <path>
```

### Delete a task scheduler folder

```bash
./tasks [auth_flags] del-folder '\MyFolder'
```
