CrewOnTheBeats-AI/
│
├── 

import os
import discord
from discord.ext import commands

# =========================
# CONFIGURACIÓN
# =========================

TOKEN = os.getenv("DISCORD_TOKEN")

STREAM_URL = os.getenv(
    "STREAM_URL",
    "https://kick.com/crewonthebeats"
)

PREFIX = "!"

# Palabras que el bot puede detectar
PALABRAS_PROHIBIDAS = {
    "spamword1",
    "spamword2",
}

# =========================
# INTENTS
# =========================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents
)

# =========================
# EVENTO: BOT ENCENDIDO
# =========================

@bot.event
async def on_ready():
    print(f"✅ Moderador conectado como {bot.user}")
    print(f"🌐 Stream: {STREAM_URL}")

# =========================
# MODERACIÓN AUTOMÁTICA
# =========================

@bot.event
async def on_message(message):

    # Ignorar mensajes del propio bot
    if message.author.bot:
        return

    contenido = message.content.lower()

    # Detectar palabras prohibidas
    palabras_detectadas = [
        palabra
        for palabra in PALABRAS_PROHIBIDAS
        if palabra in contenido
    ]

    if palabras_detectadas:

        try:
            await message.delete()

            aviso = await message.channel.send(
                f"⚠️ {message.author.mention}, "
                "ese mensaje no está permitido aquí."
            )

            # Borrar el aviso después de unos segundos
            await aviso.delete(delay=5)

        except discord.Forbidden:
            print("❌ No tengo permisos para eliminar mensajes.")

        return

    # Procesar comandos
    await bot.process_commands(message)

# =========================
# COMANDO: STREAM
# =========================

@bot.command()
async def stream(ctx):

    mensaje = (
        "🔴 **ESTAMOS EN DIRECTO**\n\n"
        "🎮 Pásate por el stream y acompáñanos.\n"
        f"👉 {STREAM_URL}"
    )

    await ctx.send(mensaje)

# =========================
# COMANDO: PROMOCIÓN
# =========================

@bot.command()
async def promo(ctx):

    mensaje = (
        "🔥 **CREWONTHEBEATS** 🔥\n\n"
        "¿Te gusta GTA V, gaming y contenido en directo?\n"
        "Únete a la comunidad y acompáñanos en el próximo directo.\n\n"
        f"🎥 Stream: {STREAM_URL}"
    )

    await ctx.send(mensaje)

# =========================
# COMANDO: AYUDA
# =========================

@bot.command()
async def ayuda(ctx):

    await ctx.send(
        "🤖 **CrewOnTheBeats AI**\n\n"
        "`!stream` → Ver el stream\n"
        "`!promo` → Mensaje promocional\n"
        "`!ayuda` → Mostrar comandos"
    )

# =========================
# INICIAR BOT
# =========================

if not TOKEN:
    raise RuntimeError(
        "❌ Falta configurar la variable DISCORD_TOKEN."
    )

bot.run(TOKEN)