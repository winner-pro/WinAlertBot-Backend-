import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from prédicteur import faire_prediction
from config import BOT_TOKEN, MENU_OPTIONS

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

etat_utilisateur = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    clavier = ReplyKeyboardMarkup(MENU_OPTIONS, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Bienvenue sur WinAlert Bot ! Choisissez une option :", reply_markup=clavier)

async def message_recu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texte = update.message.text
    chat_id = update.message.chat_id

    if texte == "Prédiction":
        prediction = faire_prediction()
        await update.message.reply_text(f"Voici la prédiction actuelle :\n\n{prediction}")
    else:
        await update.message.reply_text("Option non reconnue. Tapez /start pour revenir au menu.")

# Fonction principale
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_recu))

    application.run_polling()

if __name__ == "__main__":
    main()
