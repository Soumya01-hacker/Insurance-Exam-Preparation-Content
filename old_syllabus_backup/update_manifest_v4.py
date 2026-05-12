import json
import os

old_file = 'old_manifest.json'
new_file_repo = 'manifest.json'
new_file_app = '../app/assets/manifest.json'
new_file_app_content = '../app/assets/content/manifest.json'

with open(old_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_common = [
    {'title': 'Introduction to Insurance', 'id': 'introduction_to_insurance'},
    {'title': 'Core Elements of Insurance', 'id': 'core_elements_of_insurance'},
    {'title': 'Principles of Insurance', 'id': 'principles_of_insurance'},
    {'title': 'Features of Insurance Contracts', 'id': 'features_of_insurance_contracts'},
    {'title': 'Underwriting and Rating', 'id': 'underwriting_and_rating'},
    {'title': 'Claims Processing', 'id': 'claims_processing'},
    {'title': 'Documentation', 'id': 'documentation'},
    {'title': 'Customer Service', 'id': 'customer_service'},
    {'title': 'Grievance Redressal Mechanism', 'id': 'grievance_redressal_mechanism'},
    {'title': 'Regulatory Aspects for Insurance Agents', 'id': 'regulatory_aspects_for_insurance_agents'}
]

new_life = [
    {'title': 'What Life Insurance Involves', 'id': 'what_life_insurance_involves'},
    {'title': 'Financial Planning', 'id': 'financial_planning'},
    {'title': 'Life Insurance Products: Traditional', 'id': 'life_insurance_products_traditional'},
    {'title': 'Life insurance products: Non-Traditional', 'id': 'life_insurance_products_non_traditional'},
    {'title': 'Applications of Life Insurance', 'id': 'applications_of_life_insurance'},
    {'title': 'Pricing and Valuation in Life Insurance', 'id': 'pricing_and_valuation_in_life_insurance'},
    {'title': 'Life Insurance Documentation', 'id': 'life_insurance_documentation'},
    {'title': 'Life Insurance Underwriting', 'id': 'life_insurance_underwriting'},
    {'title': 'Life Insurance Claims', 'id': 'life_insurance_claims'}
]

new_health = [
    {'title': 'Introduction to Health Insurance', 'id': 'introduction_to_health_insurance'},
    {'title': 'Health Insurance Documentation', 'id': 'health_insurance_documentation'},
    {'title': 'Health Insurance Products', 'id': 'health_insurance_products'},
    {'title': 'Health Insurance Underwriting', 'id': 'health_insurance_underwriting'},
    {'title': 'Health Insurance Claims', 'id': 'health_insurance_claims'}
]

new_general = [
    {'title': 'General Insurance Documentation', 'id': 'general_insurance_documentation'},
    {'title': 'Underwriting and Rate Making', 'id': 'underwriting_and_rate_making'},
    {'title': 'Personal and Retail Insurance', 'id': 'personal_and_retail_insurance'},
    {'title': 'Commercial Insurance', 'id': 'commercial_insurance'},
    {'title': 'General Insurance Claims', 'id': 'general_insurance_claims'},
    {'title': 'Annexures - Specimen Proposal forms and Claims Forms for filling up', 'id': 'annexures_specimen'}
]

def make_ch(ch):
    return {
        'id': ch['id'],
        'title': ch['title'],
        'topics': [],
        'detailed_topics': [],
        'book_url': f"https://soumya01-hacker.github.io/Insurance-Exam-Preparation-Content/textbooks/{ch['id']}.pdf",
        'test_url': f"https://soumya01-hacker.github.io/Insurance-Exam-Preparation-Content/tests/{ch['id']}.json"
    }

common_chapters_list = [make_ch(c) for c in new_common]
life_chapters_list = [make_ch(c) for c in new_life]
health_chapters_list = [make_ch(c) for c in new_health]
general_chapters_list = [make_ch(c) for c in new_general]

for course in data['courses']:
    # Instead of relying on old_sections order, we build explicitly based on course ID
    new_sections = []
    
    # Common for all
    new_sections.append({
        'name': 'SECTION 1: COMMON CHAPTERS (1-10)',
        'chapters': common_chapters_list
    })
    
    if course['id'] == 'ic38_life':
        new_sections.append({
            'name': 'SECTION 2: LIFE INSURANCE (11-19)',
            'chapters': life_chapters_list
        })
        new_sections.append({
            'name': 'SECTION 3: HEALTH INSURANCE (20-24)',
            'chapters': health_chapters_list
        })
    elif course['id'] == 'ic38_general':
        new_sections.append({
            'name': 'SECTION 2: HEALTH INSURANCE (11-15)',
            'chapters': health_chapters_list
        })
        new_sections.append({
            'name': 'SECTION 3: GENERAL INSURANCE (16-21)',
            'chapters': general_chapters_list
        })
    elif course['id'] == 'ic38_health':
        new_sections.append({
            'name': 'SECTION 2: HEALTH INSURANCE (11-15)',
            'chapters': health_chapters_list
        })

    course['sections'] = new_sections
    course['total_chapters'] = sum(len(s['chapters']) for s in new_sections)

# version bump for forced update
data['version'] = '12.0.0'

for out_file in [new_file_repo, new_file_app, new_file_app_content]:
    dir_name = os.path.dirname(out_file)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f'Wrote {out_file}')
