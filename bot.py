import discord 

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("hello i'am a bot")

client.run("ODQ1MjkzMTM2MDA4MDUyNzg2.YKe2lA.caecttCMeEtLk2UjZ4qRCd4gfGc")
