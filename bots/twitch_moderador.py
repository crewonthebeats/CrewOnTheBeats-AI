 import os
import asyncio
import pyttsx3

from twitchio.ext import commands

# =========================
# CONFIGURACIÓN
# =========================

TWITCH_TOKEN = os.getenv("j3lh9eo68hhz9dwfegrktpswhbxdyo")
TWITCH_CHANNEL = os.getenv("https://www.twitch.tv/dabynhogta")
    "TWITCH_CHANNEL",
    "https://www.twitch.tv/dabynhogta"
)

# =========================
# TEXTO A VOZ
# =========================

tts = pyttsx3.init()

tts.setProperty("rate", 170)
tts.setProperty("volume", 1.0)


def hablar(texto):
    print(f"🔊 LEYENDO: {texto}")

    tts.say(texto)
    tts.runAndWait()


# =========================
# BOT DE TWITCH
# =========================

class TwitchModerador(commands.Bot):

    def __init__(self):

        super().__init__(
            token=("j3lh9eo68hhz9dwfegrktpswhbxdyo")
            prefix="!",
            initial_channels=[https://www.twitch.tv/dabynhogta]
        )

    async def event_ready(self):

        print("✅ Moderador de Twitch conectado")
        print(f"🎮 Canal: ("https://www.twitch.tv/dabynhogta")

    async def event_message(self, message):

        # Ignorar mensajes del propio bot
        if message.echo:
            return

        usuario = message.author.name
        texto = message.content.strip()

        if not texto:
            return

        print(f"💬 {usuario}: {texto}")

        # =========================
        # COMENTARIOS QUE SE LEEN
        # =========================

        frase = f"{usuario} dice: {texto}"

        # Ejecutar TTS sin bloquear el bot
        await asyncio.to_thread(hablar, frase)

        # Procesar comandos
        await self.handle_commands(message)


# =========================
# INICIAR
# =========================

if not TWITCH_TOKEN:

    raise RuntimeError(
        ""
    )

bot = TwitchModerador()

bot.run()
