import json
import os

with open('temp_claude.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# The wrapped data for dynamic content
items_data = {"items": data}

# 1. Update Red Card (All in One) in the CORRECT directory
path_all_in_one = 'dynamic_content/short_and_simple/ic38_life/all_in_one.json'
os.makedirs(os.path.dirname(path_all_in_one), exist_ok=True)
with open(path_all_in_one, 'w', encoding='utf-8') as f:
    json.dump(items_data, f, indent=2)

# 2. Update Pink Card (One Liner Notes) in the CORRECT directory
path_one_liner = 'dynamic_content/one_liner_notes/ic38_life/one_liner_notes.json'
os.makedirs(os.path.dirname(path_one_liner), exist_ok=True)
with open(path_one_liner, 'w', encoding='utf-8') as f:
    json.dump(items_data, f, indent=2)

print("Correct files updated successfully.")
