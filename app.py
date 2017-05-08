from flask import Flask, render_template
import yaml
from jinja2 import Environment, FileSystemLoader, Template
from slugify import slugify
import os

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
	# if os.environ.get('APP_LOCATION') == 'heroku':
	# 	app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
	# else:
	# 	app.run(host='localhost', port=5000, debug=True)
	app.run(host="0.0.0.0", port=os.environ.get("PORT"))