import discord
import config
import getStockData

client = discord.Client()
stockData = getStockData.getStockList()
topFiveStockList = stockData.mostGainerStock()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!stock"):
        await message.channel.send("Top 5 Gainer Stocks Today: \n" + "\n".join(topFiveStockList))

client.run(config.BOT_TOKEN)
