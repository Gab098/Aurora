#!/usr/bin/env python3
import re

# Read the original file
with open('main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by class MiniAI: to get the first class only
parts = content.split('class MiniAI:')
if len(parts) >= 2:
    # Keep only the first class
    fixed_content = parts[0] + 'class MiniAI:' + parts[1]
    
    # Fix indentation errors
    fixed_content = fixed_content.replace(
        'if novelty_proposal:\n            print(f"AI (proattiva): {novelty_proposal}")',
        'if novelty_proposal:\n                print(f"AI (proattiva): {novelty_proposal}")'
    )
    
    fixed_content = fixed_content.replace(
        'if new_addition:\n            self.legacy_project_content += "\\n\\n" + new_addition.strip()',
        'if new_addition:\n                self.legacy_project_content += "\\n\\n" + new_addition.strip()'
    )
    
    # Write the fixed content
    with open('main_fixed.py', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("File fixed successfully!")
else:
    print("Could not find class MiniAI: in the file") 