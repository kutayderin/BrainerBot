import os
import discord
from discord.ext import commands
import random
import youtube_dl

token = "NzMxNDY4OTE0OTU3MjIxOTE5.Xwmfgw.IT8Jjkes6xjmgSU8zCrD99_CJOM"
client = commands.Bot(command_prefix='.')
#client = discord.Client()


@client.event
async def on_message(message):
    if message.content.find(".clear") != -1:
        list = message.content.split(" ")
        amount = int(list[1])
        await message.channel.purge(limit=(amount + 1))
    if message.content.find(".help") != -1:
        user = message.author
        await user.send(".clear to clear messages")
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)
    if message.content.find(".guess") != -1:
        await message.channel.send("Guess a number between 1 to 100.")

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.randint(1, 100)
    if message.content.find(".join2") != -1:
        channel = message.author.voice.channel
        await channel.connect()



@client.event
async def on_member_join(self):
    log = client.get_channel(743866188718932109)
    await log.send('{} has joined to server.'.format(self.mention))


@client.event
async def on_message_edit(before, after):
    log = client.get_channel(743866188718932109)
    await log.send(
        '{} edited their message on #{}: {} to {}'.format(before.author, before.channel, before.content, after.content))


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    log = client.get_channel(743866188718932109)
    await log.send('{} deleted in #{} : {}'.format(author, channel, content))
    print('{} deleted in #{} : {}'.format(author, channel, content))


@client.command(pass_context=True, aliases=['j'])
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await channel.connect()


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    player.start()


client.run(token)
