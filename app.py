from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predictions', methods=['POST'])
def recevoir_prediction():
    data = request.json
    resultat = data.get('result')
    print(f"Résultat reçu : {resultat}")
    return jsonify({'message': 'Prédiction reçue'}), 200

@app.route('/')
def accueil():
    return 'Backend WinAlert est en ligne !'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
