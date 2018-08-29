import re

from discord.ext import commands

gnu_re = re.compile(r'(?P<GNU>GNU)?(?:.?|\s*)(?P<Linux>Linux)', re.IGNORECASE)

def check(text):
	match = gnu_re.search(text)
	return match and match['Linux'] and not match['GNU']

class Interjection:
	def __init__(self, bot, interjection):
		self.bot = bot
		self.interjection = interjection

	async def on_message(self, message):
		if message.author != self.bot.user and check(message.content):
			await message.channel.send(self.interjection)

def setup(bot):
	message = bot.config['extensions']['interjection']['message']
	if not message:
		return

	bot.add_cog(Interjection(bot, message))
