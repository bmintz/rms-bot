from discord.ext import commands

def check(text):
	"""return whether the message contains an occurence of "Linux" without "GNU" """
	had_occurrence = False
	for word in text.lower().split():
		if re.match(r'gnu.linux', word):
			return False
		if word == 'linux':
			had_occurrence = True
	return had_occurrence

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
