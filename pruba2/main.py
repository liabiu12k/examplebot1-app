from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Función para manejar el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola Mundo! 👋")

# Configuración del bot
if __name__ == "__main__":
    application = ApplicationBuilder().token("7721418131:AAGRzdKFFHRfHjdtfAdZCc7l4N8HH1jKzjE").build()

    # Añadir el manejador para el comando /start
    application.add_handler(CommandHandler("start", start))

    # Ejecutar el bot
    application.run_polling()
