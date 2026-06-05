# 🧭 Machine Role (machinerole)

**Protocols**: [MS-DSSP](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DSSP/%5bMS-DSSP%5d.pdf).

The Directory Services Setup Protocol (MS-DSSP) allows querying basic domain membership and machine role information from a remote Windows host. It reveals whether the target is a domain controller, a domain member, or a standalone machine - and which domain or workgroup it belongs to.

## Usage

### General

**Syntax:**
```bash
./machinerole [auth_flags] [--use-named-pipe]
```

**Query the machine's domain role and DS state via TCP:**

```bash
./machinerole [auth_flags]
```

**Query using the named pipe transport instead of TCP:**

```bash
./machinerole [auth_flags] --use-named-pipe
```
