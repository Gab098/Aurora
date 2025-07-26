#!/usr/bin/env python3

# Read the original file
with open('main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of the first class (before the second class MiniAI:)
first_class_end = content.find('class MiniAI:', content.find('class MiniAI:') + 1)

if first_class_end != -1:
    # Keep everything up to the second class
    first_part = content[:first_class_end]
    
    # Find the run_cli function and everything after it from the second class
    run_cli_start = content.find('async def run_cli(self):', first_class_end)
    if run_cli_start != -1:
        # Find the end of the file (before the main function if it exists)
        main_start = content.find('async def main():', run_cli_start)
        if main_start != -1:
            second_part = content[run_cli_start:main_start]
        else:
            second_part = content[run_cli_start:]
        
        # Combine the parts
        fixed_content = first_part + second_part + content[main_start:]
        
        # Write the fixed content
        with open('main_fixed.py', 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print("Fixed duplicate class issue")
    else:
        print("Could not find run_cli function")
else:
    print("Could not find duplicate class") 