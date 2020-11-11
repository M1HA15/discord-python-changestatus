import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '<custom_prefix>')

@bot.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Old Status'))

@bot.command()
async def changeStatus(ctx, status : str):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(status))
    await ctx.send(f'New status: {status}')

bot.runt("token")
