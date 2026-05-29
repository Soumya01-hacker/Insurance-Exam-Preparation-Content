import os
import json

base_dir = r"I:\Playstore_apps\Content_Repo\short_notes"

full_notes_content = {
  "sections": [
    {
      "type": "chapter_header",
      "title": "Complete IC-38 Syllabus"
    },
    {
      "type": "timeline",
      "title": "Historical Milestones",
      "items": [
        {"year": 1938, "text": "Insurance Act passed, foundation of Indian insurance regulation."},
        {"year": 1956, "text": "LIC was formed and life insurance was nationalised."},
        {"year": 1999, "text": "IRDAI Act was passed to open up the sector."}
      ]
    },
    {
      "type": "note_card",
      "title": "Key Principles",
      "cards": [
        {"title": "Utmost Good Faith", "content": "Complete transparency between insurer and insured.", "color": "blue"},
        {"title": "Insurable Interest", "content": "You must suffer a direct financial loss if the insured event happens.", "color": "green"},
        {"title": "Indemnity", "content": "Restores the insured to the same financial position as before the loss.", "color": "orange"}
      ]
    },
    {
      "type": "tips",
      "title": "Exam Pro-Tips",
      "items": [
        "Always remember the grace period is 30 days for yearly/half-yearly premiums.",
        "Free Look period is exactly 15 days from receipt of the policy document."
      ]
    }
  ]
}

# Create full notes for each course
courses = ["ic38_life", "ic38_general", "ic38_health"]
for course in courses:
    with open(os.path.join(base_dir, f"{course}_full_notes.json"), "w") as f:
        json.dump(full_notes_content, f, indent=2)

print("Full notes generated successfully!")
