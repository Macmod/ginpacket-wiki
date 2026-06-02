import os
import re

source_readme = r"C:\Users\artur\Downloads\dcsync-weiwei\README.md"
dest_dir = r"C:\Users\artur\Downloads\ginpacket-wiki"
tools_dir = os.path.join(dest_dir, "tools")

if not os.path.exists(tools_dir):
    os.makedirs(tools_dir)

with open(source_readme, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Create main README.md
usage_idx = content.find("## Usage")
if usage_idx == -1:
    print("Could not find '## Usage' in README.md")
    exit(1)

main_readme = content[:usage_idx].strip()
# Remove the HTML badges section at the top of main readme to make it cleaner for GitBook
main_readme = re.sub(r'<p align="center">.*?</p>\s*</p>\s*', '', main_readme, flags=re.DOTALL)
# Alternatively just leave it. GitBook can render basic HTML. But let's replace with a simple markdown header.
main_readme = "# Ginpacket\n\n" + main_readme

# Also append the Authentication section which is before Usage
auth_start = main_readme.find("## Authentication")

with open(os.path.join(dest_dir, "README.md"), 'w', encoding='utf-8') as f:
    f.write(main_readme)

# 2. Extract tools and build SUMMARY.md
summary_lines = [
    "# Table of contents",
    "",
    "* [Introduction](README.md)",
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
                # Let's flush them as markdown text.
                out.append("\n" + "\n".join(current_desc) + "\n")
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
                    out.append(f"### Syntax\n\n```bash\n{chr(10).join(syntax_lines)}\n```\n")
                if desc_lines:
                    # Treat the first line as heading if short, rest as text
                    if len(desc_lines[0]) < 80 and not desc_lines[0].startswith('-') and not desc_lines[0].startswith(' '):
                        out.append(f"### {desc_lines[0]}")
                        if len(desc_lines) > 1:
                            out.append("\n" + "\n".join(desc_lines[1:]) + "\n")
                    else:
                        out.append("\n" + "\n".join(desc_lines) + "\n")
                    out.append(f"\n```bash\n{line}\n```\n")
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
