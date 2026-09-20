 import os
import asyncio
import pyttsx3

from twitchio.ext import commands

# =========================
# CONFIGURACIÓN
# =========================

TWITCH_TOKEN = os.getenv("live_1227266554_zKk7XvRC04M4SUZjlbGcr3z5RzSBOU")
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
            token=TWITCH_TOKEN,
            prefix="!",
            initial_channels=[TWITCH_CHANNEL]
        )

    async def event_ready(self):

        print("✅ Moderador de Twitch conectado")
        print(f"🎮 Canal: {TWITCH_CHANNEL}")

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
        "live_1227266554_zKk7XvRC04M4SUZjlbGcr3z5RzSBOU"
    )

bot = TwitchModerador()

bot.run()
