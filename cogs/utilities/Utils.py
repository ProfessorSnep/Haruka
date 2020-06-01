import discord
from discord.ext import commands
import asyncio
import random
import time
import datetime
import pytz
import json

def getRandEmoji(emojis,query=""):
	if query is "":
		return random.choice(emojis)
	choices=[emoji for emoji in emojis if query.lower() in emoji.name.lower()]
	if len(choices)<1:
		return None
	choice= random.choice(choices)
	return choice

def genLog(member, what):
	embd=discord.Embed()
	embd.title=member.display_name
	embd.description=what
	embd=embd.set_thumbnail (url=member.avatar_url)
	embd.type="rich"
	embd.timestamp=datetime.datetime.now(pytz.timezone('US/Eastern'))
	embd=embd.add_field(name = 'Discord Username', value = str(member))
	embd=embd.add_field(name = 'id', value = member.id)
	embd=embd.add_field(name = 'Joined', value = member.joined_at)
	embd=embd.add_field(name = 'Roles', value = ', '.join(map(lambda x: x.name, member.roles)))
	embd=embd.add_field(name = 'Account Created', value = member.created_at)
	embd=embd.add_field(name = 'Profile Picture', value = member.avatar_url)
	return embd

def saveConfig(ctx):
	print("saving")
	with open('Resources.json', 'w') as outfile:
		json.dump(ctx.bot.config, outfile)