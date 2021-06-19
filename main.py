import discord
from discord.ext import commands, tasks
from itertools import cycle
import config
import getStockData

client = commands.Bot(command_prefix=config.PREFIX)
stockData = getStockData.getStockList()
status = cycle(['with itself', 'God'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is online.')


@tasks.loop(seconds=300)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))


@client.command()
async def stock(context):
    channel = context.message.channel
    embeddedMessage = discord.Embed(
        title='Top 5 Gainer Stocks Today: \n',
        description="\n".join(stockData.mostGainerStock()),
        colour=discord.Colour.blue()
    )
    await context.send(embed=embeddedMessage)


@client.command()
async def clear(message, amount=1):  # Clear messages amount default 1
    await message.channel.purge(limit=amount)


@client.command()
async def stockgraph(context):
    channel = context.message.channel
    embeddedMessage = discord.Embed(
        title='Title',  # Ticker
        description='Description here',  # Price and % change
        colour=discord.Colour.green()
    )
    embeddedMessage.set_image(
        url='http://theconcordian.com/wp-content/uploads/2021/03/dogecoin-taylor.png')

    await context.send(embed=embeddedMessage)

client.run(config.BOT_TOKEN)
