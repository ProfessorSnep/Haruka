import asyncio
import datetime
import random
import time

import discord
import pytz
import yaml
from discord.ext import commands


def getRandEmoji(emojis, query="", ctx=None):
	if ctx:
		banned = ctx.bot.config["emoteBanned"].copy()
		if ctx.message.guild:
			if ctx.message.guild.id in banned:
				banned.remove(ctx.message.guild.id)
		emojis = list(filter(lambda x: not(x.guild.id in banned), emojis))
	if query == "":
		return random.choice(emojis)
	choices = [emoji for emoji in emojis if query.lower() in emoji.name.lower()]
	if len(choices) < 1:
		return None
	choice = random.choice(choices)
	return choice


async def yay(ctx):
	emoji = getRandEmoji(ctx.message.guild.emojis, "yay")
	if emoji is None:
		emoji = getRandEmoji(ctx.bot.emojis, "yay")
	await ctx.message.add_reaction(emoji)


def genLog(member, what):
	embd = discord.Embed()
	embd.title = member.display_name
	embd.description = what
	embd = embd.set_thumbnail(url=member.avatar_url)
	embd.type = "rich"
	embd.timestamp = datetime.datetime.now(pytz.timezone('US/Eastern'))
	embd = embd.add_field(name='Discord Username', value=str(member))
	embd = embd.add_field(name='id', value=member.id)
	embd = embd.add_field(name='Joined', value=member.joined_at)
	embd = embd.add_field(name='Roles', value=', '.join(
		map(lambda x: x.name, member.roles)))
	embd = embd.add_field(name='Account Created', value=member.created_at)
	embd = embd.add_field(name='Profile Picture', value=member.avatar_url)
	return embd


def saveConfig(ctx):
	print("saving")
	with open('Resources.yaml', 'w') as outfile:
		yaml.dump(ctx.bot.config, outfile)
