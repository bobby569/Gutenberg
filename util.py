import random
import re

class Trie:
	def __init__(self):
		self.trie = {}

	def insert(self, word):
		tmp = self.trie
		for ch in word:
			tmp = tmp.setdefault(ch, {})

###############################################
#
#	End of Class. Begining of helper functions.
#
###############################################

def getWordList(line):
    return line.strip().lower().split()

def extractWord(word):
    return re.sub('[^a-z]', '', word)

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
