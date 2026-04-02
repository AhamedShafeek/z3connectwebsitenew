import os

pages_to_delete = [
    'Home.jsx',
    'About.jsx',
    'Founder.jsx',
    'Philosophy.jsx',
    'Team.jsx',
    'WhyWeExist.jsx',
    'Work.jsx',
    'Products.jsx',
    'SolutionsDetailed.jsx',
    'CaseStudies.jsx',
    'CaseStudyDetail.jsx',
    'Clients.jsx',
    'GetQuote.jsx',
    'Privacy.jsx',
    'Terms.jsx'
]

base_path = r'd:\z3connectwebsite-main\z3connectwebsite-main\z3connect-react\src\pages'

for page in pages_to_delete:
    file_path = os.path.join(base_path, page)
    if os.path.exists(file_path):
        print(f"Deleting {file_path}")
        os.remove(file_path)
    else:
        print(f"Skip (not found): {file_path}")
