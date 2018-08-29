from collections import defaultdict

class OptionalDict(defaultdict):
	"""a dict that can be accessed with any key any amount of times

	>>> OptionalDict()['this']['is']['really']['neat'] == {}
	True
	"""

	def __init__(self, *args, **kwargs):
		super().__init__(type(self), *args, **kwargs)

	def __bool__(self):
		return len(self) == 0
