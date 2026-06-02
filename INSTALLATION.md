# Installation

## Clone the repository
```bash
git clone https://github.com/Macmod/ginpacket
cd ginpacket
```

## Linux / MacOS
To build all commands into `./bin` on Linux or MacOS, use the `build.sh` script:
```bash
chmod +x build.sh
./build.sh
```

## Windows
To build all commands on Windows, use the provided `build.ps1` PowerShell script:
```powershell
.\build.ps1
```

## Static Build (Disable CGO)
If you want to build the binaries statically without relying on CGO (which is useful for portability), you can disable it by setting the `CGO_ENABLED` environment variable to `0` before building.

**On Linux / MacOS:**
```bash
CGO_ENABLED=0 ./build.sh
```

**On Windows (PowerShell):**
```powershell
$env:CGO_ENABLED="0"
.\build.ps1
```
