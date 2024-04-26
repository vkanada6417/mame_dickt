import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

command_info = [
    "1. random_pass - выводит рандомный пароль (можно самостоятельно указать длину пароля)",
    "2. add - сложение двух чисел",
    "3. spam - spam бот"
]

bot = commands.Bot(command_prefix='$-', intents=intents)

@bot.command()
async def info_help(ctx):
    for i in command_info:
        await ctx.send(i)

@bot.command()
async def random_pass(ctx, len_pass = 10):
    await ctx.send(ran_pass(len_pass))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def spam(ctx, spam_count=10):
    for i in range(spam_count):
        await ctx.send(f"Ха-ха-ха, заспамил {i+1}")


bot.run("token")
