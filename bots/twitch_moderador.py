


pip install twitchio python-dotenv



import os
from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()

TWITCH_TOKEN = os.getenv("http://localhost:3000")
TWITCH_NICK = os.getenv("dabynhogta")
TWITCH_CHANNEL = os.getenv("https://www.twitch.tv/dabynhogta")


class BotTwitch(commands.Bot):
    def __init__(self):
        super().__init__(
            token=http://localhost:3000,
            prefix="!",
            initial_channels=[https://www.twitch.tv/dabynhogta],
        )

    async def event_ready(self):
        print(f"✅ Bot conectado como: {self.nick}")
        print(f"🎮 Canal: ("{https://www.twitch.tv/dabynhogta}")

    async def event_message(self, message):
        # Ignorar mensajes del propio bot
        if message.echo:
            return

        # Permitir que los comandos reaccionen
        await self.handle_commands(message)

    @commands.command()
    async def hola(self, ctx):
        await ctx.send(f"¡Hola {ctx.author.name}! Bienvenido/a a la stream.")

    @commands.command()
    async def ayuda(self, ctx):
        await ctx.send(
            "Comandos disponibles: "
            "!hola, !ayuda, !socials, !stream, !discord"
        )

    @commands.command()
    async def socials(self, ctx):
        await ctx.send(
            "Síguenos en redes: "
            "Instagram / TikTok / X / Discord"
        )

    @commands.command()
    async def stream(self, ctx):
        await ctx.send(
            "🎮 Estamos en directo. ¡Acompáñanos y activa la campanita!"
        )

    @commands.command()
    async def discord(self, ctx):
        await ctx.send("Únete a nuestra comunidad en Discord: https://discord.gg/tu-servidor")


bot = BotTwitch()
bot.run()


python bot.py




