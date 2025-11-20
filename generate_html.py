import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os

# Load YAML data
with open('data.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Load HTML template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render HTML
output = template.render(data=data)

# Generate timestamped filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_filename = f'output_{timestamp}.html'

# Save HTML
with open(output_filename, 'w') as f:
    f.write(output)

print(f"Generated HTML file: {output_filename}")
