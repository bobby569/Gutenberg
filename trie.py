
class Trie:
	def __init__(self):
		self.trie = {}

	def insert(self, arr: List[str]) -> None:
		tmp = self.trie
		for word in arr:
			tmp = tmp.setdefault(word, {})

	def search(self, arr: List[str]):
		ptr = self.trie
		for word in arr:
			ptr = ptr.get(word)
			if not ptr:
				return None
		return ptr
