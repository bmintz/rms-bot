#!/usr/bin/env python
# encoding: utf-8

import logging

import discord
from discord.ext import commands

import utils

class RMS(commands.AutoShardedBot):
	def __init__(self):
		super().__init__(command_prefix=commands.when_mentioned)

		with open('config.py') as f:
			self.config = utils.OptionalDict(eval(f.read(), {}))

		self.load_extensions()

	def load_extensions(self):
		for extension in self.config['startup_extensions']:
			self.load_extension(extension)

	async def on_ready(self):
		print(f'Logged in as: {self.user} (ID: {self.user.id})')

	async def login(self, **kwargs):
		await super().login(self.config['tokens']['discord'], **kwargs)

if __name__ == '__main__':
	RMS().run()
