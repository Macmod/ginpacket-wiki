import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title and protocols
    lines = content.split('\n')
    title = lines[0] if len(lines) > 0 else ''
    protocols = lines[2] if len(lines) > 2 and 'Protocols' in lines[2] else ''

    # Find the bash block
    bash_block_match = re.search(r'```bash\n(.*?)\n```', content, re.DOTALL)
    
    notes_match = re.search(r'```\n\n(.*)', content, re.DOTALL)
    notes = notes_match.group(1).strip() if notes_match else ''

    if not bash_block_match:
        print(f"Skipping {filepath} - no bash block found.")
        return

    bash_block = bash_block_match.group(1)

    out_md = []
    out_md.append(title)
    out_md.append("\n" + protocols + "\n")
    
    tool_name = re.search(r'\((.*?)\)', title)
    tool_name = tool_name.group(1) if tool_name else 'this tool'

    out_md.append("## Introduction")
    out_md.append(f"The `{tool_name}` tool is used to interact with {tool_name}-related features via the specified protocols. It provides a variety of subcommands to perform administrative, auditing, and operational tasks against the target system.")
    out_md.append("\n## Subcommands\n")

    # Parse bash block
    # A block typically looks like:
    # # command usage syntax
    # # description
    # example
    
    # We will split by empty lines to get command groups
    blocks = bash_block.split('\n\n')
    
    for block in blocks:
        block = block.strip()
        if not block: continue
        
        block_lines = block.split('\n')
        syntax = ""
        description = ""
        examples = []
        
        # Parse lines in the block
        # Sometimes there's syntax `# tool [auth_flags] cmd ...`
        # Then multiple `# description` followed by `example`
        current_desc = ""
        
        for line in block_lines:
            line = line.strip()
            if not line: continue
            
            if line.startswith(f"# {tool_name} [auth_flags]") or line.startswith(f"# {tool_name} ("):
                syntax = line[1:].strip()
            elif line.startswith("#"):
                current_desc = line[1:].strip()
            else:
                examples.append((current_desc, line))
                current_desc = ""

        if syntax:
            # Try to extract the subcommand name
            parts = syntax.split(' ')
            subcmd = parts[2] if len(parts) > 2 else "command"
            if subcmd.startswith('[') or subcmd.startswith('(') or subcmd.startswith('-'):
                subcmd = "General Usage"
            out_md.append(f"### `{subcmd}`")
            out_md.append(f"**Syntax**:\n```bash\n{syntax}\n```\n")
            
            if examples:
                out_md.append("#### Examples")
        else:
            out_md.append(f"### Examples")

        for desc, cmd in examples:
            if desc:
                out_md.append(f"{desc}:")
            out_md.append(f"```bash\n{cmd}\n```\n")

    if notes:
        out_md.append("## Notes\n")
        out_md.append(notes)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_md))

if __name__ == "__main__":
    for f in glob.glob("*.md"):
        if f == "README.md": continue
        process_file(f)
