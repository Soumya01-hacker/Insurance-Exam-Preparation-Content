import re

file_path = r'i:\Playstore_apps\Insurance_exam_preparation_app\app\lib\features\auth\presentation\pages\exam_selection_screen.dart'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

life_chapters = """totalChapters: 24, totalTests: 20,
    chapters: [
      '1. Introduction to Insurance',
      '2. Core Elements of Insurance',
      '3. Principles of Insurance',
      '4. Features of Insurance Contracts',
      '5. Underwriting and Rating',
      '6. Claims Processing',
      '7. Documentation',
      '8. Customer Service',
      '9. Grievance Redressal Mechanism',
      '10. Regulatory Aspects for Insurance Agents',
      '11. What Life Insurance Involves',
      '12. Financial Planning',
      '13. Life Insurance Products: Traditional',
      '14. Life insurance products: Non-Traditional',
      '15. Applications of Life Insurance',
      '16. Pricing and Valuation in Life Insurance',
      '17. Life Insurance Documentation',
      '18. Life Insurance Underwriting',
      '19. Life Insurance Claims',
      '20. Introduction to Health Insurance',
      '21. Health Insurance Documentation',
      '22. Health Insurance Products',
      '23. Health Insurance Underwriting',
      '24. Health Insurance Claims',
    ],"""

general_chapters = """totalChapters: 21, totalTests: 15,
    chapters: [
      '1. Introduction to Insurance',
      '2. Core Elements of Insurance',
      '3. Principles of Insurance',
      '4. Features of Insurance Contracts',
      '5. Underwriting and Rating',
      '6. Claims Processing',
      '7. Documentation',
      '8. Customer Service',
      '9. Grievance Redressal Mechanism',
      '10. Regulatory Aspects for Insurance Agents',
      '11. Introduction to Health Insurance',
      '12. Health Insurance Documentation',
      '13. Health Insurance Products',
      '14. Health Insurance Underwriting',
      '15. Health Insurance Claims',
      '16. General Insurance Documentation',
      '17. Underwriting and Rate Making',
      '18. Personal and Retail Insurance',
      '19. Commercial Insurance',
      '20. General Insurance Claims',
      '21. Annexures - Specimen Proposal forms and Claims Forms for filling up',
    ],"""

health_chapters = """totalChapters: 15, totalTests: 10,
    chapters: [
      '1. Introduction to Insurance',
      '2. Core Elements of Insurance',
      '3. Principles of Insurance',
      '4. Features of Insurance Contracts',
      '5. Underwriting and Rating',
      '6. Claims Processing',
      '7. Documentation',
      '8. Customer Service',
      '9. Grievance Redressal Mechanism',
      '10. Regulatory Aspects for Insurance Agents',
      '11. Introduction to Health Insurance',
      '12. Health Insurance Documentation',
      '13. Health Insurance Products',
      '14. Health Insurance Underwriting',
      '15. Health Insurance Claims',
    ],"""

# Regex to find ExamInfo block and replace totalChapters ... chapters: [...]
def replace_chapters(text, exam_id, new_content):
    pattern = r"(id:\s*'" + exam_id + r"'.*?totalChapters:\s*\d+,\s*totalTests:\s*\d+,\s*\n\s*chapters:\s*\[.*?\]\,)"
    def repl(m):
        m_str = m.group(1)
        # replace the totalChapters and chapters part inside m_str
        sub_pattern = r"totalChapters:\s*\d+,\s*totalTests:\s*\d+,\s*\n\s*chapters:\s*\[.*?\]\,"
        return re.sub(sub_pattern, new_content, m_str, flags=re.DOTALL)
    
    return re.sub(pattern, repl, text, flags=re.DOTALL)

content = replace_chapters(content, 'ic38_life', life_chapters)
content = replace_chapters(content, 'ic38_general', general_chapters)
content = replace_chapters(content, 'ic38_health', health_chapters)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done replacing chapters in exam_selection_screen.dart')
