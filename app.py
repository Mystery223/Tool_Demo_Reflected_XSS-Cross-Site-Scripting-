from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)


VULNERABLE_TEMPLATE = """
{% extends "index.html" %}
{% block content %}
    {{ query|safe }}
{% endblock %}
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    nama = request.args.get('nama', '')
    return render_template('index.html', mode='vulnerable', query=nama)

@app.route('/secure', methods=['GET'])
def secure():
    nama = request.args.get('nama', '')
    return render_template('index.html', mode='secure', query=nama)

if __name__ == '__main__':
    print("XSS Lab berjalan di http://127.0.0.1:5000")
    app.run(debug=True)
