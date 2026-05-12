import json
import os

new_chapters = [
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

chapters_list = []
for ch in new_chapters:
    chapters_list.append({
        'id': ch['id'],
        'title': ch['title'],
        'topics': [],
        'detailed_topics': [],
        'book_url': f'https://soumya01-hacker.github.io/Insurance-Exam-Preparation-Content/textbooks/{ch["id"]}.pdf',
        'test_url': f'https://soumya01-hacker.github.io/Insurance-Exam-Preparation-Content/tests/{ch["id"]}.json'
    })

common_section = {
    'name': 'COMMON CHAPTERS',
    'chapters': chapters_list
}

files = [
    r'i:\Playstore_apps\Insurance_exam_preparation_app\content_repo\manifest.json',
    r'i:\Playstore_apps\Insurance_exam_preparation_app\app\assets\content\manifest.json'
]

for file in files:
    try:
        if not os.path.exists(file):
            print(f'File not found: {file}')
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for course in data.get('courses', []):
            course['sections'] = [common_section]
            course['total_chapters'] = 10
            
            # Make sure mock_tests contain only full syllabus mock tests (filter logic if needed)
            # We will just leave existing mock_tests intact since they are already "Full Syllabus Mock Test"
            # as per user: "sirf mocktest full syllabus wohi rakho"
            new_mocks = [m for m in course.get('mock_tests', []) if 'mock' in m.get('id', '').lower()]
            course['mock_tests'] = new_mocks
            
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f'Successfully updated {file}')
    except Exception as e:
        print(f'Error updating {file}: {e}')
