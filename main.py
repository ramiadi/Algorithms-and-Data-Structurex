from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return open('templates/index.html', encoding='utf-8').read()

@app.route('/visualize/<algorithm>')
def visualize(algorithm):
    return render_template('visualize.html', algorithm=algorithm)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
