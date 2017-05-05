from flask import Flask, render_template
import yaml
from jinja2 import Environment, FileSystemLoader, Template

app = Flask(__name__)

ENV = Environment(loader=FileSystemLoader('./'))

with open('data.yaml') as data:
    data =  yaml.load(data)

app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)

# data = ['anna', 'maria', 'bialas']

@app.route('/')
def index():
    return render_template('index.html', title = 'index', items = data)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about')

if __name__ == "__main__":
    app.run()