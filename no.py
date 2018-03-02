import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print("Ready when you are xd")
	print("I am running on " + bot.user.name)
	print("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say(":ping_pong: ping!! xSSS")
	print("User has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	embed = discord.Embed(title="{}'s info".format(user.name), color=0x0000ff)
	embed.add_field(name="Name:", value=user.name, inline=True)
	embed.add_field(name="UserID:", value=user.id, inline=True)
	embed.add_field(name="Status:", value=user.status, inline=True)
	embed.add_field(name="Role:" , value=user.top_role)
	embed.add_field(name="Joined at:", value=user.joined_at)
	embed.set_thumbnail(url=user.avatar_url)
	await bot.say(embed=embed)
        except discord.ext.commands.errors.MissingRequiredArgument:
               await bot.say("hi") 
	
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
	embed = discord.Embed(color=0x00ff00)
	embed.set_footer(text="Cyka Blyat")
	embed.add_field(name=":white_check_mark:", value="Successfully kicked: {}".format(user.name), inline=True)
	await bot.say(embed=embed)
	await bot.kick(user)


@bot.command(pass_context=True)
async def embed(ctx):
	embed = discord.Embed(title="test", description="hiec", color=0x00ff00)
	embed.set_footer(text="nignog")
	embed.set_author(name="nigger")
	embed.add_field(name="This is a field", value="nigg nog", inline=True)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cmds(ctx):
	embed = discord.Embed(color=0x0000ff)
	embed.set_footer(text="Cyka Blyat")
	embed.add_field(name="info [username]", value="Tells you information about a user")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def say(ctx, string):
        embed = discord.Embed(title="I said:", description=str(string), color=0x0000ff)
        embed.set_footer(text="Cyka Blyat")
        await bot.say(embed=embed)

bot.run("NDEyODM2ODE3MDUwNjY0OTYx.DWQD3w.WbwHME_aO2JFI24zHBBR1wseEbI")
