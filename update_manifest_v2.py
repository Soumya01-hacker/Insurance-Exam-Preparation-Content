import json

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

common_chapters_list = []
for ch in new_common:
    common_chapters_list.append({
        'id': ch['id'],
        'title': ch['title'],
        'topics': [],
        'detailed_topics': [],
        'book_url': f"https://soumya01-hacker.github.io/Insurance-Exam-Preparation-Content/textbooks/{ch['id']}.pdf",
        'test_url': f"https://soumya01-hacker.github.io/Insurance-Exam-Preparation-Content/tests/{ch['id']}.json"
    })

for course in data['courses']:
    # Get the old sections
    old_sections = course.get('sections', [])
    new_sections = []
    
    # 1. Add Common Chapters
    new_sections.append({
        'name': 'SECTION 1: COMMON CHAPTERS (1-10)',
        'chapters': common_chapters_list
    })
    
    # 2. Add specific chapters
    for sec in old_sections:
        if 'COMMON' in sec['name'].upper():
            continue
        
        # update section names
        if 'LIFE' in sec['name'].upper():
            sec['name'] = 'SECTION 2: LIFE INSURANCE (11-21)'
        elif 'HEALTH' in sec['name'].upper():
            if course['id'] == 'ic38_life':
                sec['name'] = 'SECTION 3: HEALTH INSURANCE (22-26)' 
            elif course['id'] == 'ic38_general':
                sec['name'] = 'SECTION 2: HEALTH INSURANCE (11-15)'
            elif course['id'] == 'ic38_health':
                sec['name'] = 'SECTION 2: HEALTH INSURANCE (11-15)'
        elif 'GENERAL' in sec['name'].upper():
            sec['name'] = 'SECTION 3: GENERAL INSURANCE (16-21)'

        new_sections.append(sec)

    course['sections'] = new_sections
    
    # update total_chapters
    total = sum(len(s['chapters']) for s in new_sections)
    course['total_chapters'] = total
    
    new_mocks = [m for m in course.get('mock_tests', []) if 'mock' in m.get('id', '').lower()]
    course['mock_tests'] = new_mocks

data['version'] = '10.0.0'

for out_file in [new_file_repo, new_file_app, new_file_app_content]:
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f'Wrote to {out_file}')
