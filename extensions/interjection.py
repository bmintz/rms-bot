import re

from discord.ext import commands

gnu_re = re.compile(r'(?P<GNU>GNU)?(?:.?|\s*)(?P<Linux>Linux)', re.IGNORECASE)

def check(text):
	"""return whether the message contains an occurence of "Linux" without "GNU" """
	iterated = False
	for match in gnu_re.finditer(text):
		iterated = True
		if match['GNU']:
			return False
	# don't return True if the message contains neither GNU nor Linux
	# (ie, finditer was empty)
	return iterated

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
