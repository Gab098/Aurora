#!/usr/bin/env python3

# Read the backup file to get missing functions
with open('main_backup.py', 'r', encoding='utf-8') as f:
    backup_content = f.read()

# Find the run_cli function directly
run_cli_start = backup_content.find('async def run_cli(self):')
if run_cli_start != -1:
    # Find the end of the first class (before the second class MiniAI:)
    second_class_start = backup_content.find('class MiniAI:', run_cli_start + 1)
    if second_class_start != -1:
        missing_functions = backup_content[run_cli_start:second_class_start]
    else:
        # If no second class, take everything to the end
        missing_functions = backup_content[run_cli_start:]
    
    # Append to main.py
    with open('main.py', 'a', encoding='utf-8') as f:
        f.write('\n' + missing_functions)
    
    print("Added missing functions to main.py")
else:
    print("Could not find run_cli function in backup") 