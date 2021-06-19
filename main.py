import discord
from discord.ext import commands
import config
import getStockData

client = commands.Bot(command_prefix=config.PREFIX)
stockData = getStockData.getStockList()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('with itself.'))
    print('Bot is online.')


@client.command()
async def stock(message):
    await message.send("Top 5 Gainer Stocks Today: \n" + "\n".join(stockData.mostGainerStock()))


@client.command()
async def clear(message, amount=5):  # Clear messages amount 5
    await message.channel.purge(limit=amount)

client.run(config.BOT_TOKEN)
