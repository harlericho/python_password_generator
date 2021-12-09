from flask import Flask, render_template
from generator import generatorText
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', text=generatorText())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)