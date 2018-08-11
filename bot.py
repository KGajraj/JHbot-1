# Discord Bot

import os
import sys
import random
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from variables import tokenVar

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

print("-----------------------------")
print("Loading...")

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="15 Hours"))
	print("Running")
	print("Bot username: " + bot.user.name)
	print("Bot user ID: " + bot.user.id)
	print("-----------------------------")


@bot.group(pass_context=True)
async def help(ctx):
	if ctx.invoked_subcommand is None:
		embedHelp = discord.Embed(title="Commands", colour=0xFFFFFF)
		embedHelp.set_author(name="JHbot", icon_url="http://niconiconii.co.uk/swan.jpg")
		embedHelp.add_field(name="help", value="Show this", inline=False)
		embedHelp.add_field(name="ping", value="pong", inline=False)
		embedHelp.add_field(name="echo", value="Repeats what you said", inline=False)
		embedHelp.add_field(name="tron", value="tron.mp3", inline=True)
		embedHelp.add_field(name="info", value="Tells you info about a user (att them)", inline=False)
		embedHelp.add_field(name="serverinfo", value="Info about the server", inline=False)
		embedHelp.add_field(name="edit", value="Most recently edited message", inline=False)
		embedHelp.add_field(name="img", value="Sends an image", inline=False)
		embedHelp.add_field(name="dab", value="Random dab", inline=False)
		embedHelp.add_field(name="graphics", value="Graphics", inline=False)
		embedHelp.add_field(name="source", value="Bot code", inline=False)
		await bot.say(embed=embedHelp)

@help.command()
async def img():
	images = os.listdir("media/img")
	imagesStr = ""
	for i in range(0,len(images)):
		imagesStr = imagesStr + images[i].replace(".jpg", "") + ", "
		print(imagesStr)
	embedHelpImg = discord.Embed(title="img command images:", description=imagesStr[:-2], colour=0xFFFFFF)
	embedHelpImg.set_author(name="JHbot", icon_url="http://niconiconii.co.uk/swan.jpg")
	await bot.say(embed=embedHelpImg)


@bot.event
async def on_message_edit(msgB, msgA):
	global embedEdit
	user = msgB.author.name
	pfp = msgB.author.avatar_url
	msgBefore = msgB.content
	msgAfter = msgA.content
	if msgBefore != msgAfter:
		embedEdit = discord.Embed(title="Message edited by " + user)
		embedEdit.set_author(name="JHbot", icon_url=pfp)
		embedEdit.colour = 0xffff00
		embedEdit.add_field(name="Before", value=msgBefore, inline=False)
		embedEdit.add_field(name="After", value=msgAfter, inline=False)
@bot.command()
async def edit():
	await bot.say(embed=embedEdit)

@bot.command()
async def ping():
	await bot.say("Pong!")

@bot.command()
async def echo(*, content:str):
	await bot.say(content)

@bot.command()
async def info(user: discord.Member):
	userColour = user.colour
	username = user.name
	userDisc = user.discriminator
	nickname = user.nick
	joinDate = user.joined_at
	madeDate = user.created_at
	profilePicture = user.avatar_url

	embedInfo = discord.Embed()
	embedInfo.colour = userColour
	embedInfo.add_field(name="Username:", value=username + "#" + userDisc, inline=True)	
	embedInfo.add_field(name="Nickname:", value=nickname, inline=True)
	embedInfo.add_field(name="Join date:", value=joinDate, inline=True)
	embedInfo.add_field(name="Account create date:", value=madeDate, inline=True)
	embedInfo.set_thumbnail(url=profilePicture)

	await bot.say(embed=embedInfo)

@bot.command(pass_context=True)
async def serverinfo(ctx):
	server = ctx.message.server 
	pic = server.icon_url
	memberCount = server.member_count
	createDate = server.created_at
	name = server.name

	embedServer = discord.Embed()
	embedServer.add_field(name="Server name: ", value=name)
	embedServer.add_field(name="Members: ", value=memberCount)
	embedServer.add_field(name="Created on: ", value=createDate)
	embedServer.set_thumbnail(url=pic)
	
	await bot.say(embed=embedServer)


@bot.command()
async def source():
	embedGithub = discord.Embed(title="Github source code", url="https://github.com/jstri/JHbot")
	await bot.say(embed=embedGithub)

# @bot.command()
# async def depression():
# 	for i in range(14):
# 		questions = [
# 			"Ive been feeling optimistic about the future",
# 			"Ive been feeling useful",
# 			"Ive been feeling relaxed",
# 			"Ive been feeling interested in other people",
# 			"Ive had energy to spare",
# 			"Ive been dealing with problems well",
# 			"Ive been thinking clearly",
# 			"Ive been feeling good about myself",
# 			"Ive been feeling close to other people",
# 			"Ive been feeling confident",
# 			"Ive been able to make up my mind abut things",
# 			"Ive been feeling loved",
# 			"Ive been interested in new things",
# 			"Ive been feeling cheerful"
# 		]

# 		embedDepression = discord.Embed(title="Commands", colour=0xFFFFFF)
# 		embedDepression.clear_fields()
		
# 		embedDepression.set_footer()
# 		embedDepression.add_field(name=questions[i], value="1: none of the time, 4: all of the time")
# 		await bot.say(embed = embedDepression)


@bot.command(pass_context=True)
async def img(ctx, image: str): #pylint: disable=E0102
	try:
		channel = ctx.message.channel
		await bot.send_file(channel, "media/img/" + image + ".jpg")
	except:
		await bot.say("Image not found")


@bot.command(pass_context=True)
async def graphics(ctx):
	channel = ctx.message.channel
	await bot.send_file(channel, "media/graphics/graphics1.jpg")
	await bot.send_file(channel, "media/graphics/graphics2.jpg")
	await bot.send_file(channel, "media/graphics/graphics3.jpg")


@bot.command(pass_context=True)
async def dab(ctx):
	channel = ctx.message.channel
	file = random.choice(os.listdir("media/dab"))
	await bot.send_file(channel, "media/dab/" + file)
	

@bot.command(pass_context=True)
async def tron(ctx):
	channel = ctx.message.channel
	await bot.send_file(channel, "media/TRON_beginning.mp3")


@bot.event
async def on_message(msg):
	if "NYA" in msg.content.upper():
		await bot.add_reaction(msg, "😹")
	await bot.process_commands(msg)

bot.run(tokenVar)