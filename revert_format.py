import json

with open('temp_claude.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. For All In One (Red Card) -> Needs {"items": [...]}
with open('short_and_simple/ic38_life/all_in_one.json', 'w', encoding='utf-8') as f:
    json.dump({"items": data}, f, indent=2)

# 2. For E-Notes (Blue Card) -> Needs sections -> note_card -> cards
short_notes_sections = [
    {
        "type": "chapter_header",
        "title": "Complete IC-38 Syllabus"
    }
]

for i, chapter in enumerate(data):
    title = chapter["title"]
    if not title.startswith("Chapter"):
        title = f"Chapter {i+1}: {title}"
        
    short_notes_sections.append({
        "type": "note_card",
        "title": title,
        "cards": [
            {
                "title": "Notes & Important Q&A",
                "content": chapter["description"],
                "color": "blue"
            }
        ]
    })

short_notes_full = {"sections": short_notes_sections}

with open('short_notes/ic38_life_full_notes.json', 'w', encoding='utf-8') as f:
    json.dump(short_notes_full, f, indent=2)
