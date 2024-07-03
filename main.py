import discord
import random
import requests
from discord.ext import commands
TOKEN='TOKEN'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot_id=''
@bot.event
async def on_ready():
    global bot_id
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.CustomActivity(name='I AM ALIVE 🖥️'))
    bot_id=bot.user.id


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']



@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(f'Here you have a cute dog video!\n{image_url}')



@bot.command()
async def inventory(ctx):
    embed = discord.Embed(title="Inventory", color=0x00ff00)
    embed.add_field(name="Fiel1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=False)
    await ctx.send(embed=embed)


  
@bot.command()
async def kill(ctx, *, user: str = None):
    if user is None:
        await ctx.reply('Who?')
    else:
        # Verificar si la mención contiene @everyone o @here
        if user == '@everyone' or user == '@here':
            await ctx.send("You cannot kill everyone or here!")
        else:
            try:
                # Intentar convertir el nombre de usuario a un objeto User
                member = await commands.UserConverter().convert(ctx, user)
                await ctx.send(f'<@{ctx.author.id}> killed <@{member.id}>')
                if member.id==ctx.author.id:
                    await ctx.send('You can\'t kill yourself!')
            except discord.ext.commands.UserNotFound:
                await ctx.send('User not found.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



bot.run(TOKEN)
