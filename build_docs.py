import os
import re

source_readme = r"C:\Users\artur\Downloads\dcsync-weiwei\README.md"
dest_dir = r"C:\Users\artur\Downloads\ginpacket-wiki"
tools_dir = os.path.join(dest_dir, "tools")

if not os.path.exists(tools_dir):
    os.makedirs(tools_dir)

with open(source_readme, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Split top-level sections
usage_idx = content.find("## Usage")
if usage_idx == -1:
    print("Could not find '## Usage' in README.md")
    exit(1)

def convert_github_alerts(text):
    lines = text.split('\n')
    out = []
    in_alert = False
    for line in lines:
        if line.startswith('> [!NOTE]'):
            out.append('{% hint style="info" %}')
            in_alert = True
        elif line.startswith('> [!IMPORTANT]'):
            out.append('{% hint style="warning" %}')
            in_alert = True
        elif line.startswith('> [!WARNING]'):
            out.append('{% hint style="danger" %}')
            in_alert = True
        elif line.startswith('> [!TIP]'):
            out.append('{% hint style="success" %}')
            in_alert = True
        elif in_alert and line.startswith('>'):
            content = line[1:]
            if content.startswith(' '):
                content = content[1:]
            out.append(content)
        elif in_alert and not line.startswith('>'):
            out.append('{% endhint %}')
            out.append(line)
            in_alert = False
        else:
            out.append(line)
    if in_alert:
        out.append('{% endhint %}')
    return '\n'.join(out)

top_part = content[:usage_idx].strip()
install_idx = top_part.find("## Installation")
auth_idx = top_part.find("## Authentication")

intro = top_part[:install_idx].strip()
authentication = top_part[auth_idx:].strip()

# Cleanup Intro
intro = re.sub(r'<p align="center">.*?</p>\s*</p>\s*', '', intro, flags=re.DOTALL)
intro = "# Ginpacket\n\n" + intro
intro = convert_github_alerts(intro)

# Fix order of RAA and Endpoint mapper
intro = intro.replace(
    "* Endpoint mapper\n* Directory Replication Service ([MS-DRSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DRSR/%5bMS-DRSR%5d.pdf))\n* Remote Authorization API ([MS-RAA](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-raa/))",
    "* Endpoint mapper\n* Remote Authorization API ([MS-RAA](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-raa/))\n* Directory Replication Service ([MS-DRSR](https://winprotocoldocs-bhdugrdyduf5h2e4.b02.azurefd.net/MS-DRSR/%5bMS-DRSR%5d.pdf))"
)

with open(os.path.join(dest_dir, "README.md"), 'w', encoding='utf-8') as f:
    f.write(intro)

# Write Authentication
auth_md = "# Authentication\n\n" + convert_github_alerts(authentication[len("## Authentication"):].strip())
with open(os.path.join(dest_dir, "AUTHENTICATION.md"), 'w', encoding='utf-8') as f:
    f.write(auth_md)

# Write Installation (Expanded)
install_md = """# Installation

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
.\\build.ps1 -All
```

### Building Specific Tools
Just like on Linux, you can run the script interactively to choose what to build from a TUI menu:
```powershell
.\\build.ps1
```

Or you can specify the tools you want to build via command-line arguments:
```powershell
.\\build.ps1 ldap dns cert
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
.\\build.ps1 -All
```
"""
with open(os.path.join(dest_dir, "INSTALLATION.md"), 'w', encoding='utf-8') as f:
    f.write(install_md)

# 2. Extract tools and build SUMMARY.md
summary_lines = [
    "# Table of contents",
    "",
    "* [Introduction](README.md)",
    "* [Installation](INSTALLATION.md)",
    "* [Authentication](AUTHENTICATION.md)",
    "* [Tools](tools/README.md)"
]

tools_readme_lines = [
    "# Tools",
    ""
]
# Find all details blocks
blocks = re.findall(r'<details>\s*<summary><strong>(.*?)</strong></summary>(.*?)</details>', content, re.DOTALL)

def parse_bash_block(bash_text):
    out = []
    current_desc = []
    lines = bash_text.strip().split('\n')
    
    # Merge lines ending with '\'
    merged_lines = []
    accum = ""
    for line in lines:
        if line.endswith('\\'):
            accum += line[:-1] + " \\\n"
        else:
            merged_lines.append(accum + line)
            accum = ""
            
    # We want to identify syntax vs examples
    for line in merged_lines:
        if line.startswith('#'):
            desc = line.lstrip('#').strip()
            current_desc.append(desc)
        elif line.strip() == '':
            if current_desc:
                # If we hit an empty line and we have accumulated comments,
                # they might be a standalone text block.
                # But if it looks like syntax, render it as a bash block.
                syntax_lines = []
                desc_lines = []
                for d in current_desc:
                    words = d.split()
                    if not words:
                        continue
                    first_word = words[0]
                    if ('[auth_flags]' in d) or (first_word == short_name and '<' in d):
                         syntax_lines.append(d)
                    else:
                         desc_lines.append(d)
                
                if syntax_lines:
                    fixed_syntax = []
                    subcmd_header = "General Usage"
                    for s in syntax_lines:
                        if not s.startswith('./') and short_name in s:
                            fixed_syntax.append(s.replace(short_name, f'./{short_name}', 1))
                        else:
                            fixed_syntax.append(s)
                            
                        # Extract subcommand for header
                        tokens = s.split()
                        for token in tokens[1:]:
                            if token == '[auth_flags]':
                                continue
                            if token.startswith('-') or token.startswith('<') or token.startswith('[') or token.startswith('('):
                                continue
                            if token in ('ldaps|ldap',):
                                continue
                            if re.match(r'^[a-zA-Z0-9_]+([-|][a-zA-Z0-9_]+)*$', token):
                                subcmd_header = token
                                # Grab an optional second subcommand part (e.g. 'query users', 'create group')
                                next_idx = tokens.index(token) + 1
                                if next_idx < len(tokens):
                                    next_tok = tokens[next_idx]
                                    if re.match(r'^[a-zA-Z0-9_]+([-|][a-zA-Z0-9_]+)*$', next_tok) and next_tok not in ('ldaps|ldap',):
                                        subcmd_header += " " + next_tok
                                break

                    out.append(f"### {subcmd_header}\n\n**Syntax:**\n```bash\n{chr(10).join(fixed_syntax)}\n```\n")
                if desc_lines:
                    out.append("\n" + "  \n".join(desc_lines) + "  \n")
                
                current_desc = []
            continue
        else:
            # Code line
            if current_desc:
                # Separate syntax from description if needed
                syntax_lines = []
                desc_lines = []
                for d in current_desc:
                    if ('[auth_flags]' in d or '<' in d or ']' in d) and (line.startswith('./' + d.split()[0]) or line.startswith(d.split()[0])):
                        syntax_lines.append(d)
                    else:
                        if ('[auth_flags]' in d and len(d.split()) > 1 and d.split()[1] == '[auth_flags]'):
                             syntax_lines.append(d)
                        else:
                             desc_lines.append(d)
                
                if syntax_lines:
                    fixed_syntax = []
                    subcmd_header = "General Usage"
                    for s in syntax_lines:
                        if not s.startswith('./') and short_name in s:
                            fixed_syntax.append(s.replace(short_name, f'./{short_name}', 1))
                        else:
                            fixed_syntax.append(s)
                            
                        # Extract subcommand for header
                        tokens = s.split()
                        for token in tokens[1:]:
                            if token == '[auth_flags]':
                                continue
                            if token.startswith('-') or token.startswith('<') or token.startswith('[') or token.startswith('('):
                                continue
                            if token in ('ldaps|ldap',):
                                continue
                            if re.match(r'^[a-zA-Z0-9_]+([-|][a-zA-Z0-9_]+)*$', token):
                                subcmd_header = token
                                # Grab an optional second subcommand part (e.g. 'query users', 'create group')
                                next_idx = tokens.index(token) + 1
                                if next_idx < len(tokens):
                                    next_tok = tokens[next_idx]
                                    if re.match(r'^[a-zA-Z0-9_]+([-|][a-zA-Z0-9_]+)*$', next_tok) and next_tok not in ('ldaps|ldap',):
                                        subcmd_header += " " + next_tok
                                break
                                
                    out.append(f"### {subcmd_header}\n\n**Syntax:**\n```bash\n{chr(10).join(fixed_syntax)}\n```\n")
                if desc_lines:
                    # Render as bold description instead of ### heading
                    out.append(f"**{' '.join(desc_lines)}:**\n")
                    out.append(f"```bash\n{line}\n```\n")
                elif not desc_lines and not syntax_lines:
                    out.append(f"```bash\n{line}\n```\n")
                current_desc = []
            else:
                out.append(f"```bash\n{line}\n```\n")
    
    # In case there are trailing comments without code
    if current_desc:
        out.append(f"{' '.join(current_desc)}\n")
        
    return "\n".join(out)

for title, body in blocks:
    # Example title: 🎫 Kerberos TGT (gettgt)
    # Extract short name
    match = re.search(r'\((.*?)\)', title)
    if not match:
        continue
    short_name = match.group(1).lower()
    
    md_filename = f"{short_name}.md"
    
    summary_lines.append(f"  * [{title}](tools/{md_filename})")
    tools_readme_lines.append(f"* [{title}]({md_filename})")
    
    # Parse body
    # Extract protocols
    proto_match = re.search(r'\*\*Protocols\*\*:.*?(?=\n\n|$)', body, re.DOTALL)
    protocols = proto_match.group(0) if proto_match else ""
    
    # Extract bash blocks
    bash_blocks = re.findall(r'```bash\n(.*?)\n```', body, re.DOTALL)
    
    # Extract notes (anything outside bash blocks and protocols)
    notes = body.replace(protocols, '')
    for b in bash_blocks:
        notes = notes.replace(f'```bash\n{b}\n```', '')
    notes = notes.strip()
    notes = convert_github_alerts(notes)
    
    # Build tool markdown
    tool_md = [
        f"# {title}",
        "",
        protocols,
        "",
        "## Subcommands / Usage",
        ""
    ]
    
    for b in bash_blocks:
        parsed = parse_bash_block(b)
        tool_md.append(parsed)
        
    if notes:
        tool_md.append("## Notes")
        tool_md.append(notes)
        
    with open(os.path.join(tools_dir, md_filename), 'w', encoding='utf-8') as f:
        f.write("\n".join(tool_md))

with open(os.path.join(dest_dir, "SUMMARY.md"), 'w', encoding='utf-8') as f:
    f.write("\n".join(summary_lines))
    
with open(os.path.join(tools_dir, "README.md"), 'w', encoding='utf-8') as f:
    f.write("\n".join(tools_readme_lines))

print("Done generating docs!")

