class Trie:
	def __init__(self):
		self.trie = {}

	def insert(self, word):
		tmp = self.trie
		for ch in word:
			tmp = tmp.setdefault(ch, {})
