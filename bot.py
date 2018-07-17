# JHbot by Jay

import sys
import asyncio
from tokenfile import tokenVar

import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = "=")
bot.remove_command("help")

print("-----------------------------")
print("Loading...")

@bot.event
async def on_ready():
	await bot.change_presence(game = discord.Game(name = "15 Hours", url = "http://www.jhgs.bucks.sch.uk/", type = 1))
	print("Running")
	print("Bot username: " + bot.user.name)
	print("Bot user ID: " + bot.user.id)
	print("-----------------------------")


@bot.command()
async def help():
	embedHelp = discord.Embed(
		title = "Commands",
		colour = 0xFFFFFF
	)

	embedHelp.set_author(name = "JHbot", icon_url = "http://niconiconii.co.uk/swan.jpg")
	embedHelp.add_field(name = "=help", value = "Show this", inline = False)
	embedHelp.add_field(name = "=info", value = "Tells you info about a user (att them)", inline = False)
	# embedHelp.add_field(name = "#depression", value = "Depression test", inline = False)
	await bot.say(embed = embedHelp)


@bot.command()
async def info(user: discord.Member):
	
	# await bot.say("The username is: {}".format(user.name))
	# await bot.say("User ID: {}".format(user.id))
	# await bot.say("User status: {}".format(user.status))
	# await bot.say("User joined: {}".format(user.joined_at))
	
	userColour = user.colour
	username = user.name
	nickname = user.nick
	joinDate = user.joined_at
	gamePlaying = user.game

	embedInfo = discord.Embed(title = "User info:")
	embedInfo.add_field(name = "Username:", value = username, inline = True)
	embedInfo.add_field(name = "Nickname:", value = nickname, inline = True)
	await bot.say(embed = embedInfo)
	


@bot.command()
async def depression():
	for i in range(14):
		questions = [
			"Ive been feeling optimistic about the future",
			"Ive been feeling useful",
			"Ive been feeling relaxed",
			"Ive been feeling interested in other people",
			"Ive had energy to spare",
			"Ive been dealing with problems well",
			"Ive been thinking clearly",
			"Ive been feeling good about myself",
			"Ive been feeling close to other people",
			"Ive been feeling confident",
			"Ive been able to make up my mind abut things",
			"Ive been feeling loved",
			"Ive been interested in new things",
			"Ive been feeling cheerful"
		]

		embedDepression = discord.Embed(title = "Commands", colour = 0xFFFFFF)
		embedDepression.clear_fields()
		
		embedDepression.set_footer()
		embedDepression.add_field(name = questions[i], value = "1: none of the time, 4: all of the time")
		await bot.say(embed = embedDepression)

		#discord.on_message

@bot.command()
async def echo(*args):
	output = ""
	for word in args:
		output = output + word
		output = output + " "
	await bot.say(output)


bot.run(tokenVar)