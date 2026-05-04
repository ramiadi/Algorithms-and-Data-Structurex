from flask import Flask, render_template, request, jsonify
from algorithms.bubble_sort import bubble_sort

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/hello")
def hello():
    return "hello_world"


@app.route("/bubble_sort")
def bubble_sort_page():
    return render_template("bubble_sort.html")

@app.route("/api/bubble_sort", methods=["POST"])
def bubble_sort_api():
    data = request.get_json()
    steps = bubble_sort(data["array"])
    return jsonify(steps)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)