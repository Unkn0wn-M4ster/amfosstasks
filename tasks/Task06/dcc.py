import discord
from discord.ext import commands
from scraper import scrape_livescore

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot Is Online")

@bot.command()
async def Ping(ctx):
    await ctx.reply("pong")

@bot.command()
async def livescore(ctx):
    live_score = scrape_livescore()
    await ctx.send(live_score)

@bot.command()
async def generate(ctx):
    with open('livescore.csv', 'rb') as file:
        file = discord.File(file, filename='livescore.csv')
        message = "Live scores have been saved to 'livescore.csv':"
        await ctx.send(content=message, file=file)
@bot.command()
async def Help(ctx):
    await ctx.reply("""
                    1)!Ping Gives back Pong
                    2)!livescore gives u the latest ongoing match
                    3)!Generate Gives you a csv of details of matches""")
    
    
    
    
bot.run("MTE1MDAxMTQ0NDYwODM4MDk2OA.GrD5eo.QWyvmNot-dwqt4eIDIxXdBa7bZXNpXp-z_cfck")
