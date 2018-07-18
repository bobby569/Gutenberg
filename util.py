import random, re

class Trie:
	def __init__(self):
		self.trie = {}

	def insert(self, arr):
		tmp = self.trie
		for word in arr:
			tmp = tmp.setdefault(word, {})

	def search(self, arr):
		ptr = self.trie
		for word in arr:
			ptr = ptr.get(word, None)
			if not ptr:
				return None
		return ptr

###############################################
#
#	End of Class. Begining of helper functions.
#
###############################################

def getWordList(line):
    return line.strip().lower().split()

def extractWord(word):
	return re.split('[^a-zA-Z]', word)

def extractChapterNumber(s):
    return s.strip().split()[-1]

def getTopFrequence(top=100):
    freq = open('./freq.txt', "r")

    cnt, word_set = 0, set()
    for line in freq:
        word_set.add(line.strip())
        cnt += 1
        if cnt >= top:
            break

    freq.close()
    return word_set

def getRandomFrom(seq):
    return random.sample(seq, 1)[0] if seq else None

def hasEOS(s):
	length = len(s)

	period = s.index('.') if '.' in s else length
	exclmation = s.index('!') if '!' in s else length
	question = s.index('?') if '?' in s else length

	return min([period, exclmation, question])
