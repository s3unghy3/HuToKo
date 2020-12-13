import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("available")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!Szia"):
        await message.channel.send("안녕하세요")


client.run("Nzg3NDA1MjQwNjg4NTc0NTE0.X9UeRg.4p03iZjOTA_5DDJuvsjixGqJ3CA")