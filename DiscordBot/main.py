# Bot By Dylan

import discord
from discord.ext import commands
import asyncio
import random
from itertools import cycle

TOKEN = 'CANT POST THE TOKEN ONLINE :('
bot = commands.Bot(command_prefix = ";")
bot.remove_command('help')
playing = bot.change_presence(game=discord.Game(name='Type $commands for Commands'))
status = ["Use $help", "type $help"]

async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    print("==================================")
    print("--- TestBot Version 2.0.0 Beta ---")
    print("==================================")
    print("---------- I'M ONLINE!! ----------")
    print("==================================")

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await bot.send_message(channel, "{} has added {} to the message: {}".format(user.name, reaction.emoji, reaction.message.content))

@bot.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await bot.send_message(channel, "{} has removed {} to the message: {}".format(user.name, reaction.emoji, reaction.message.content))

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.orange()
        )

    embed.set_author(name='Commands:')
    embed.add_field(name='$ping', value='return pong!', inline=False)
    embed.add_field(name='$coinflip', value='flips a coin', inline=False)
    embed.add_field(name='$echo (phrase)', value='returns phrase', inline=False)

    await bot.send_message(author, embed=embed)

@bot.command()
async def ping(): 
    await bot.say('Pong!')

@bot.command(pass_context = True)
async def kick(member):
    await bot.kick(member)
    await bot.send_message(member, "has been removed From The Server Monka-S")

@bot.command()
async def ban(member, delete_message_days):
    await bot.ban(member)
    await bot.send_message(member, "Has Been Banned #FeelsBadMan")


@bot.command()
async def echo(*args):
    output = ''
    for word in args:
        output +=word
        output += ' '
    await bot.say(output)

@bot.command()
async def coinflip():
    coin = ["Tails!!", "Heads", "Tails!!", "Heads", "Coin Broke :grimacing:"]
    randomchoice = random.choice(coin)
    await bot.say(randomchoice)

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages Deleted")

bot.loop.create_task(change_status())
bot.run(TOKEN)
