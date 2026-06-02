# Installation

{% hint style="success" %}
**Looking for pre-built binaries?**
You can download ready-to-use releases for Windows, Linux, and macOS directly from the [Releases page](https://github.com/Macmod/ginpacket/releases).
{% endhint %}

## Clone the repository
```bash
git clone https://github.com/Macmod/ginpacket
cd ginpacket
```

## Linux / MacOS
To build all commands into `./bin` on Linux or MacOS, use the `build.sh` script:
```bash
chmod +x build.sh
./build.sh --all
```

### Building Specific Tools
If you only want to build specific tools, you can run the script interactively. This will open a terminal UI (TUI) menu allowing you to select the desired tools with the spacebar:
```bash
./build.sh
```

Alternatively, you can pass the tool names directly as arguments to skip the menu:
```bash
./build.sh ldap dns cert
```

## Windows
To build all commands on Windows, use the provided `build.ps1` PowerShell script:
```powershell
.uild.ps1 -All
```

### Building Specific Tools
Just like on Linux, you can run the script interactively to choose what to build from a TUI menu:
```powershell
.uild.ps1
```

Or you can specify the tools you want to build via command-line arguments:
```powershell
.uild.ps1 ldap dns cert
```

## Static Build (Disable CGO)
If you want to build the binaries statically without relying on CGO (which is useful for portability), you can disable it by setting the `CGO_ENABLED` environment variable to `0` before building.

**On Linux / MacOS:**
```bash
CGO_ENABLED=0 ./build.sh --all
```

**On Windows (PowerShell):**
```powershell
$env:CGO_ENABLED="0"
.uild.ps1 -All
```
