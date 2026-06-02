# 🖨️ Printer (printer)

**Protocols**: [MS-RPRN](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-RPRN/%5bMS-RPRN%5d.pdf) (`\pipe\spoolss` or TCP via `--use-tcp`).

## Subcommands / Usage

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] printers
```
{% endhint %}

### List all locally installed printers (name, share, port, driver, status)

```bash
./printer [auth_flags] printers
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] dump [--ports] [--monitors] [--forms] [--strict]
```
{% endhint %}

### Collect core printer inventory (server, printers, drivers, processors)

```bash
./printer [auth_flags] dump
```

### Include additional optional sections

```bash
./printer [auth_flags] dump --ports --monitors --forms
```

### Stop immediately on the first failing section

```bash
./printer [auth_flags] dump --strict
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] drivers [-e <environment>]
```
{% endhint %}

### List installed driver names, environments, and spool-store paths

```bash
./printer [auth_flags] drivers
```

### List installed drivers filtered by environment

```bash
./printer [auth_flags] drivers -e 'Windows x86'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] ports
```
{% endhint %}

### List configured ports (TCP/IP ports reveal the physical printer IP)

```bash
./printer [auth_flags] ports
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] monitors
```
{% endhint %}

### List port monitor DLLs (third-party monitors reveal loaded code paths)

```bash
./printer [auth_flags] monitors
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] server
```
{% endhint %}

### Read PrintNightmare mitigation registry flags and server version

```bash
./printer [auth_flags] server
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] processors [-e <environment>]
```
{% endhint %}

### List all print processors registered for an environment

```bash
./printer [auth_flags] processors
```

### List print processors for a specific environment

```bash
./printer [auth_flags] processors -e 'Windows x64'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] datatypes [-c <print-processor>] [-e <environment>]
```
{% endhint %}

### List data types supported by the default print processor

```bash
./printer [auth_flags] datatypes
```

### List data types for a specific print processor and environment

```bash
./printer [auth_flags] datatypes -c WinPrint -e 'Windows x64'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] info <printer>
```
{% endhint %}

### Show full PRINTER_INFO_2 for one printer (config, status, attributes bitmask)

```bash
./printer [auth_flags] info '\\TARGET\HP LaserJet'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] driver <printer> [-e <environment>]
```
{% endhint %}

### Show DRIVER_INFO_3 for the driver attached to a printer

```bash
./printer [auth_flags] driver '\\TARGET\HP LaserJet'
```

### Show driver info for a printer in a specific environment

```bash
./printer [auth_flags] driver '\\TARGET\HP LaserJet' -e 'Windows x64'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] jobs <printer>
```
{% endhint %}

### List queued (and retained) jobs on a printer

```bash
./printer [auth_flags] jobs '\\TARGET\HP LaserJet'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] job <printer> -j <job-id>
```
{% endhint %}

### Show detailed JOB_INFO_2 for a single print job

```bash
./printer [auth_flags] job '\\TARGET\HP LaserJet' -j 3
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] set-job <printer> -j <job-id> -a <pause|resume|cancel|restart|delete|retain|release>
```
{% endhint %}

### Cancel a print job

```bash
./printer [auth_flags] set-job '\\TARGET\HP LaserJet' -j 3 -a cancel
```

### Retain a completed job in the queue for inspection

```bash
./printer [auth_flags] set-job '\\TARGET\HP LaserJet' -j 3 -a retain
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] set-attrs <printer> [-A <add-mask>] [-R <remove-mask>]
```
{% endhint %}

### Enable KEEPPRINTEDJOBS (0x100) so completed jobs stay visible in the queue

```bash
./printer [auth_flags] set-attrs '\\TARGET\TestRAW1' -A 0x100
```

### Disable KEEPPRINTEDJOBS

```bash
./printer [auth_flags] set-attrs '\\TARGET\TestRAW1' -R 0x100
```

### Enable sharing (0x8) and keep-printed-jobs simultaneously

```bash
./printer [auth_flags] set-attrs '\\TARGET\TestRAW1' -A 0x108
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] notify <listener-host>
```
{% endhint %}

### Trigger a change notification to a remote listener (authentication as TARGET$)

```bash
./printer [auth_flags] notify 10.10.14.1
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] add-printer -n <name> -d <driver> -q <port> [-s <share>] [-C <comment>] [-D <datatype>] [-c <processor>]
```
{% endhint %}

### Add a printer using an already-installed driver

```bash
./printer [auth_flags] add-printer  \
    -n 'TestPrinter'  \
    -d 'Microsoft Print To PDF'  \
    -q 'PORTPROMPT:'
```

### Add a shared printer with a comment

```bash
./printer [auth_flags] add-printer  \
    -n 'SharedPrinter'  \
    -d 'Microsoft Print To PDF'  \
    -q 'PORTPROMPT:'  \
    -s 'SharedPrinter'  \
    -C 'added remotely'
```

### Add a v3 RAW printer suitable for direct RPRN print jobs

```bash
./printer [auth_flags] add-printer  \
    -n 'TestRAW1'  \
    -d 'Microsoft Shared Fax Driver'  \
    -q 'LPT1:'  \
    -D RAW -c WinPrint
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] set-printer <printer> -a <pause|resume|purge>
```
{% endhint %}

### Pause a printer (new jobs are held)

```bash
./printer [auth_flags] set-printer '\\TARGET\TestPrinter' -a pause
```

### Resume a paused printer

```bash
./printer [auth_flags] set-printer '\\TARGET\TestPrinter' -a resume
```

### Purge all queued jobs from a printer

```bash
./printer [auth_flags] set-printer '\\TARGET\TestPrinter' -a purge
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] reset-printer <printer> [-D <datatype>]
```
{% endhint %}

### Reset a printer's data type and device-mode to defaults

```bash
./printer [auth_flags] reset-printer '\\TARGET\TestPrinter'
```

### Reset a printer with an explicit data type

```bash
./printer [auth_flags] reset-printer '\\TARGET\TestPrinter' -D RAW
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] del-printer <printer>
```
{% endhint %}

### Delete a printer

```bash
./printer [auth_flags] del-printer '\\TARGET\TestPrinter'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] driver-dir [-e <environment>]
```
{% endhint %}

### Get the server-side driver staging directory

```bash
./printer [auth_flags] driver-dir
```

### Get the driver staging directory for a specific environment

```bash
./printer [auth_flags] driver-dir -e 'Windows x64'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] add-driver <driver-name> --driver-path <path> --data-file <path> --config-file <path> [-e <env>]
```
{% endhint %}

### Install a driver from UNC paths accessible to the print server

```bash
./printer [auth_flags] add-driver  \
    'CustomDriver'  \
    --driver-path '\\FILESERVER\share\driver.dll'  \
    --data-file   '\\FILESERVER\share\driver.dll'  \
    --config-file '\\FILESERVER\share\driver.dll'
```

### Install a driver using files already in the server's driver store

```bash
./printer [auth_flags] add-driver  \
    'Cloned Driver'  \
    --driver-path 'C:\Windows\System32\spool\DRIVERS\x64\3\mxdwdrv.dll'  \
    --data-file   'C:\Windows\System32\spool\DRIVERS\x64\3\mxdwdrv.dll'  \
    --config-file 'C:\Windows\System32\spool\DRIVERS\x64\3\mxdwdrv.dll'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] del-driver <driver-name> [-e <environment>]
```
{% endhint %}

### Delete an installed driver

```bash
./printer [auth_flags] del-driver 'Evil Driver'
```

### Delete a driver for a specific environment

```bash
./printer [auth_flags] del-driver 'Evil Driver' -e 'Windows x64'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] add-processor <processor-name> --path <dll> [-e <environment>]
```
{% endhint %}

### Register a print processor DLL (must be in the driver store on the server)

```bash
./printer [auth_flags] add-processor 'EvilProc' --path 'evilproc.dll'
```

### Register a print processor for a specific environment

```bash
./printer [auth_flags] add-processor 'EvilProc' --path 'evilproc.dll' -e 'Windows x64'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] del-processor <processor-name> [-e <environment>]
```
{% endhint %}

### Remove a print processor

```bash
./printer [auth_flags] del-processor 'EvilProc'
```

### Remove a print processor for a specific environment

```bash
./printer [auth_flags] del-processor 'EvilProc' -e 'Windows x64'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] processor-dir [-e <environment>]
```
{% endhint %}

### Get the server-side print processor staging directory

```bash
./printer [auth_flags] processor-dir
```

```bash
./printer [auth_flags] processor-dir -e 'Windows x64'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] forms
```
{% endhint %}


List all form definitions registered on the print server (built-in and user-defined)  


```bash
./printer [auth_flags] forms
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] form <form>
```
{% endhint %}

### Show details for a specific form by name

```bash
./printer [auth_flags] form 'Letter'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] add-form <form> --width <mm> --height <mm> [--x-off <n>] [--y-off <n>]
```
{% endhint %}

### Add a new user-defined form to the print server

```bash
./printer [auth_flags] add-form 'MyForm' --width 210 --height 297
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] set-form <form> --width <mm> --height <mm>
```
{% endhint %}

### Update dimensions of an existing user-defined form

```bash
./printer [auth_flags] set-form 'MyForm' --width 215 --height 279
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] del-form <form>
```
{% endhint %}

### Delete a user-defined form from the print server

```bash
./printer [auth_flags] del-form 'MyForm'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] add-port <port> [--monitor <name>]
```
{% endhint %}

### Register a new printer port on the print server

```bash
./printer [auth_flags] add-port 'LPT2:'
```

```bash
./printer [auth_flags] add-port '192.168.88.20_Port' --monitor 'Standard TCP/IP Port'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] del-port <port>
```
{% endhint %}

### Delete a printer port from the print server

```bash
./printer [auth_flags] del-port 'LPT2:'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] add-monitor <name> --path <dll> [-e <environment>]
```
{% endhint %}

### Register a port monitor DLL on the print server

```bash
./printer [auth_flags] add-monitor 'MyMon' --path 'mymon.dll'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] del-monitor <name> [-e <environment>]
```
{% endhint %}

### Remove a port monitor from the print server

```bash
./printer [auth_flags] del-monitor 'MyMon'
```

{% hint style="info" %}
**Syntax**

```bash
./printer [auth_flags] print <printer> -f <file> [-d <doc-name>] [-D <datatype>] [-o <output-path>]
```
{% endhint %}

### Send a raw PRN/PCL/PostScript file to a v3-driver printer

```bash
./printer [auth_flags] print '\\TARGET\TestRAW1' -f document.prn
```

### Send a print job with a custom document name

```bash
./printer [auth_flags] print '\\TARGET\TestRAW1' -f payload.prn -d 'Quarterly Report'
```

### Send a print job with an explicit data type

```bash
./printer [auth_flags] print '\\TARGET\TestRAW1' -f page.ps -D RAW
```

### Redirect server-side output to a path (for virtual/PDF printers)

```bash
./printer [auth_flags] print '\\TARGET\PDFPrinter' -f input.ps  \
    -o 'C:\Users\Public\out.pdf'
```

## Notes
> **💡 Tip — Testing workflow for the write commands** ? run the read-only commands first to find valid values before making changes:
> 1. `printers` ? records exact `\\TARGET\PrinterName` strings to use with `-P`
> 2. `drivers` ? confirms driver name/environment for `add-driver` / `del-driver`
> 3. `driver-dir` ? reveals the server-side staging path so you can pre-stage driver files via `smb put`
> 4. `server` ? checks `NoAddPrinterDrivers` and `RestrictDriverInstallationToAdministrators` flags before attempting driver operations
> 5. `info -P ...` ? shows the current `Attributes` bitmask before using `set-attrs`
>
> **Job retention** ? by default Windows discards jobs once printed. Enable `KEEPPRINTEDJOBS` (bit `0x100`) with `set-attrs -A 0x100` to keep completed jobs visible for inspection with `jobs` and `job`.
>
> **v3 vs v4 drivers** ? only v3 drivers (e.g. "Microsoft Shared Fax Driver") support the `RpcStartDocPrinter` / `RpcWritePrinter` RPRN print path. v4 drivers (Print to PDF, XPS Writer) return `ERROR_NOT_SUPPORTED`. Use `drivers` to check the driver version column.
>
> **Transport note** ? named-pipe transport (`\pipe\spoolss`, default) requires domain credentials and will silently reject operations on hardened hosts. Add `--use-tcp` to fall back to the RPC-over-TCP path registered via the endpoint mapper on port 135.