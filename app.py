from flask import Flask, jsonify, send_from_directory
from rbi_quiz import generate_quiz

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/quiz')
def quiz():
    questions = [q.__dict__ for q in generate_quiz()]
    return jsonify(questions)


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
