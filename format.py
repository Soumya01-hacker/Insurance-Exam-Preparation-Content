import json
import re

with open('temp_claude.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

formatted_data = []
short_notes_sections = [
    {
        "type": "chapter_header",
        "title": "Complete IC-38 Syllabus - All In One"
    }
]

for i, chapter in enumerate(data):
    desc = chapter['description']
    
    # Split into concepts and Q&A
    if "🎯 HIGHLY REPEATED EXAM Q&A:" in desc:
        parts = desc.split("🎯 HIGHLY REPEATED EXAM Q&A:")
        concepts = parts[0].strip()
        qa_raw = parts[1].strip()
    else:
        concepts = desc.strip()
        qa_raw = ""
    
    # Format concepts
    formatted_concepts = re.sub(r'•\s*(.*?):', r'🔹 **\1:**', concepts)
    
    # Format Q&A
    if qa_raw:
        qa_formatted = "🎯 **HIGHLY REPEATED EXAM Q&A:**\n\n" + qa_raw
        qa_formatted = re.sub(r'(?m)^Q:\s*', r'❓ **Q:** ', qa_formatted)
        qa_formatted = re.sub(r'(?m)^A:\s*', r'💡 **A:** ', qa_formatted)
    else:
        qa_formatted = ""
    
    # Combined for all_in_one
    combined_desc = formatted_concepts + "\n\n" + qa_formatted if qa_formatted else formatted_concepts
    
    formatted_data.append({
        "title": chapter["title"],
        "description": combined_desc.strip()
    })
    
    # Create cards for short_notes
    cards = []
    cards.append({
        "title": "Key Concepts 🧠",
        "content": formatted_concepts,
        "color": "blue"
    })
    if qa_formatted:
        cards.append({
            "title": "Exam Q&A 🎯",
            "content": qa_formatted,
            "color": "green"
        })
        
    title = chapter["title"]
    if title.startswith("Chapter "):
        title = title # leave as is
    else:
        title = f"Chapter {i+1}: {title}"
        
    short_notes_sections.append({
        "type": "note_card",
        "title": title,
        "cards": cards
    })

short_notes_full = {"sections": short_notes_sections}

with open('short_and_simple/ic38_life/all_in_one.json', 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, indent=2)

with open('short_notes/ic38_life_full_notes.json', 'w', encoding='utf-8') as f:
    json.dump(short_notes_full, f, indent=2)
