import discord
from discord.ext import commands
import random
from ranks import *

'''description = An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='.', description='Returns Tespa team SR and individual SR')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
'''
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))   
'''    
@bot.command(description='Enter link to Tespa team and recieve team analytics')
async def tespa(team):
    output = analyze(team)
    output = '```autohotkey' +'\n'+ output + '```'
    await bot.say(output)
    
@bot.command(description='Enter battletag and recieve sr for given battletag')
async def sr(name):
    output = findSR(name)
    output = '```autohotkey' +'\n' + output + '```'
    await bot.say(output)
'''
@bot.command(description='gachibass')
async def gachi():
	output = '░░░░░▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░' + '\n'
	+ '░░░▓▓▓▓▓▓▒▒▒▒▒▒▓▓░░░░░░░ ' + '\n'
	+ '░░▓▓▓▓▒░░▒▒▓▓▒▒▓▓▓▓░░░░░ ' + '\n'
	+ '░▓▓▓▓▒░░▓▓▓▒▄▓░▒▄▄▄▓░░░░ ' + '\n'
	+ '▓▓▓▓▓▒░░▒▀▀▀▀▒░▄░▄▒▓▓░░░ ' + '\n'
	+ '▓▓▓▓▓▒░░▒▒▒▒▒▓▒▀▒▀▒▓▒▓░░ ' + '\n'
	+ '▓▓▓▓▓▒▒░░░▒▒▒░░▄▀▀▀▄▓▒▓░ ' + '\n'
	+ '▓▓▓▓▓▓▒▒░░░▒▒▓▀▄▄▄▄▓▒▒▒▓ ' + '\n'
	+ '░▓█▀▄▒▓▒▒░░░▒▒░░▀▀▀▒▒▒▒░ ' + '\n'
	+ '░░▓█▒▒▄▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓░ ' + '\n'
	+ '░░░▓▓▓▓▒▒▒▒▒▒▒▒░░░▒▒▒▓▓░ ' + '\n'
	+ '░░░░░▓▓▒░░▒▒▒▒▒▒▒▒▒▒▒▓▓░ ' + '\n'
	+ '░░░░░░▓▒▒░░░░▒▒▒▒▒▒▒▓▓░░ ' + '\n'
	await bot.say(output)
'''    
bot.run('NDk0MzAxODMwMzgyMDkyMzIw.Doxi8g.KfJtft4C_OOo2Xwx0iBksFCu_-M')
