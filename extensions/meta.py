from discord.ext import commands

class Meta:
	def __init__(self, bot, license):
		self.bot = bot
		self.license = license

	@commands.command(name='license', aliases=('copyright',))
	async def license_command(self, context):
		await context.send(self.license)

def setup(bot):
	license = bot.config['extensions']['meta']['license']
	if not license:
		print('WARNING: no license text is configured, but this is an AGPLv3-licensed project!')
		return

	bot.add_cog(Meta(bot, license))
