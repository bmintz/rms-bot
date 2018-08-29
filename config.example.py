{
	'tokens': {
		'discord': '',
	},

	'startup_extensions': (
		'jishaku',  # debug extension, provides eval and sh commands
		'extensions.meta',
		'extensions.interjection',
	),

	'extensions': {
		'meta': {
			'license': '\n'.join((
				'RMS bot',
				# the \© is cause Discord for Android displays © as an emoji otherwise
				'Copyright \© <year> <name of author>',
				'',
				'This program is free software: you can redistribute it and/or modify '
				'it under the terms of the GNU Affero General Public License as published by '
				'the Free Software Foundation, either version 3 of the License, or '
				'(at your option) any later version. ',
				'',
				'This program is distributed in the hope that it will be useful, '
				'but WITHOUT ANY WARRANTY; without even the implied warranty of '
				'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the '
				'GNU Affero General Public License for more details.',
				'',
				'You may find the source code at: <link to the source code>.',
			)),
		},

		'interjection': {
			'message':
				"I'd just like to interject for moment. "
				"What you're refering to as Linux, is in fact, GNU/Linux, "
				"or as I've recently taken to calling it, GNU plus Linux. "
				'Linux is not an operating system unto itself, '
				'but rather another free component of a fully functioning GNU system '
				'made useful by the GNU corelibs, shell utilities and vital system components '
				'comprising a full OS as defined by POSIX.',
		},
	},
}
