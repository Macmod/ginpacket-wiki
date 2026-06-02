# 📊 Performance Counter (perf)

**Protocols**: [MS-PCQ](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-PCQ/%5bMS-PCQ%5d.pdf).

## Subcommands / Usage

### Syntax

```bash
./perf [auth_flags] csets
```

### List all performance counter sets (GUIDs and names)

```bash
./perf [auth_flags] csets
```

### Syntax

```bash
./perf [auth_flags] cset <guid>
```

### Show metadata for a specific counter set by GUID

```bash
./perf [auth_flags] cset '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}'
```

### Syntax

```bash
./perf [auth_flags] instances <guid>
```

### List all instances of a counter set

```bash
./perf [auth_flags] instances '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}'
```

### Syntax

```bash
./perf [auth_flags] query <guid> [-c <counter-id>] [--instance <id>]
```

### Query all counters for a counter set

```bash
./perf [auth_flags] query '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}'
```

### Query specific counters within a counter set

```bash
./perf [auth_flags] query '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --counter 1 --counter 2
```

### Query a specific counter for a specific instance

```bash
./perf [auth_flags] query '{6BFFD098-A112-610E-9FBF-00A0C90D67DA}' --counter 1 --instance 0
```

### Syntax

```bash
./perf [auth_flags] dump
```

### Dump all available counter data from all counter sets

```bash
./perf [auth_flags] dump
```
