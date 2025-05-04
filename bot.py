import requests
import time

BOT_TOKEN = ' 7893795650:AAGNMWS51L5PwCTrulgT7LH3Ghp80YMbdtM'
CHAT_ID = ' 7893927170'

BACKEND_URL = 'https://winalertbot-backend.onrender.com/predictions'

def envoyer_prediction(resultat):
    try:
        response = requests.post(BACKEND_URL, json={'result': resultat})
        if response.status_code == 200:
            print("✅ Prédiction envoyée avec succès")
        else:
            print(f"❌ Erreur d'envoi : {response.status_code}")
    except Exception as e:
        print(f"❌ Exception : {e}")

def boucle_predictions():
    while True:
        
        resultat = "WIN"  # ou "LOSE", ou toute autre logique IA ici
        envoyer_prediction(resultat)
        time.sleep(300)  # Toutes les 5 minutes

if __name__ == "__main__":
    boucle_predictions()
