import json
import os
import markdown
from jinja2 import Environment, FileSystemLoader

CONTENT_DIR = 'content'
TEMPLATE_DIR = 'templates'
OUTPUT_DIR = 'public'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template('index.html')

projects = []
for filename in os.listdir(CONTENT_DIR):
    if filename.endswith('.json'):
        with open(os.path.join(CONTENT_DIR, filename), 'r') as f:
            project = json.load(f)
            if 'description' in project:
                project['description_html'] = markdown.markdown(project['description'])
            projects.append(project)

projects.sort(key=lambda x: x.get('order', 999))

html = template.render(projects=projects)

with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w') as f:
    f.write(html)

print("Site built successfully.")