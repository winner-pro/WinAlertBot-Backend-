from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
predictions = []

@app.route('/')
def index():
    return "WinAlertBot est en ligne !"

@app.route('/predictions', methods=['GET'])
def get_predictions():
    return jsonify(predictions[-20:])

@app.route('/predictions', methods=['POST'])
def add_prediction():
    data = request.json
    if not data or 'result' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    prediction = {
        'time': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'result': data['result']
    }
    predictions.append(prediction)
    return jsonify({'message': 'Prediction added'}), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
