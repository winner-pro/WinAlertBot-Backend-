import os
import time
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Récupère le token depuis les variables d'env (à configurer sur Render)
BOT_TOKEN = os.environ[' 7893795650:AAGNMWS51L5PwCTrulgT7LH3Ghp80YMbdtM']

BACKEND_BASE = "https://winalertbot-backend.onrender.com"

def envoyer_prediction(resultat):
    """Envoie une prédiction au backend."""
    try:
        response = requests.post(
            f"{BACKEND_BASE}/predictions",
            json={'result': resultat}
        )
        if response.status_code == 200:
            print("✅ Prédiction envoyée avec succès")
        else:
            print(f"❌ Erreur d'envoi : {response.status_code}")
    except Exception as e:
        print(f"❌ Exception : {e}")

def boucle_predictions():
    """Boucle envoyant régulièrement une prédiction."""
    while True:
        # TODO : Remplace cette ligne par ta logique de calcul de résultat
        resultat = "WIN"
        envoyer_prediction(resultat)
        time.sleep(300)  # toutes les 5 minutes

def cmd_resultats(update: Update, context: CallbackContext):
    """Handler pour la commande /résultats."""
    try:
        r = requests.get(f"{BACKEND_BASE}/predictions")
        r.raise_for_status()
        data = r.json()
        if not data:
            text = "Aucune prédiction disponible."
        else:
            dernières = data[-5:]
            lignes = [f"{p['time']} ➔ {p['result']}" for p in dernières]
            text = "\n".join(lignes)
    except Exception as e:
        text = f"Erreur en récupérant les résultats : {e}"
    update.message.reply_text(text)

def main():
    updater = Updater(token=BOT_TOKEN)
    dp = updater.dispatcher

    # Ajout du handler /résultats
    dp.add_handler(CommandHandler("résultats", cmd_resultats))

    # Démarre la boucle de prédiction en arrière-plan
    # Si tu préfères lancer manuellement, commente ces lignes
    import threading
    thread = threading.Thread(target=boucle_predictions, daemon=True)
    thread.start()

    # Lance le bot Telegram
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
