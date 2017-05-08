from flask import Flask, render_template
import yaml
from jinja2 import Environment, FileSystemLoader, Template
from slugify import slugify

app = Flask(__name__)

env = Environment(loader=FileSystemLoader('./'))

with open('data.yaml') as data:
    data =  yaml.load(data)

def slugify_string(text):
    return slugify(text)

app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)

@app.route('/')
def index():
    return render_template('index.html', title = 'index', items = data)

if __name__ == "__main__":
	app.jinja_env.filters['slugify'] = slugify_string
	app.run(host='0.0.0.0', port=3000)