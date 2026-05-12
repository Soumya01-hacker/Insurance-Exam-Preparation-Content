import json
import os

chapter_files = [
    "introduction_to_insurance.json",
    "customer_service.json",
    "grievance_redressal_mechanism.json",
    "regulatory_aspects_of_insurance_agents.json",
    "legal_principles_of_insurance.json",
    "what_life_insurance_involves.json",
    "financial_planning.json",
    "life_insurance_products_1.json",
    "life_insurance_products_2.json",
    "applications_of_life_insurance.json",
    "pricing_and_valuation.json",
    "documentation_proposal_stage.json",
    "documentation_policy_condition_1.json",
    "documentation_policy_condition_2.json",
    "underwriting.json",
    "payments_under_life_policy.json",
    "introduction_to_health_insurance.json",
    "health_insurance_documentation.json",
    "health_insurance_products.json",
    "health_insurance_underwriting.json",
    "health_insurance_claims.json"
]

base_dir = r"I:\Playstore_apps\Insurance_exam_preparation_app\content_repo\short_notes"

combined_sections = []

for file in chapter_files:
    file_path = os.path.join(base_dir, file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Add a chapter header section
            combined_sections.append({
                "type": "chapter_header",
                "title": data.get("title", file)
            })
            
            # Add all sections from the chapter
            sections = data.get("sections", [])
            combined_sections.extend(sections)
    else:
        print(f"File not found: {file}")

combined_json = {
    "chapterId": "ic38_life_full_notes",
    "title": "IC-38 Life Full Syllabus Notes",
    "theme": "Premium Blue-Gold",
    "sections": combined_sections
}

output_path = os.path.join(base_dir, "ic38_life_full_notes.json")
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(combined_json, f, indent=2, ensure_ascii=False)

print(f"Successfully created {output_path}")
