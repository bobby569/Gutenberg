import math
import random
import re
from typing import List, Set


def getWordList(line: str) -> List[str]:
    return line.strip().lower().split()


def extractWords(word: str) -> List[str]:
	return re.split('[^a-zA-Z]', word)


def extractChapterNumber(s: str) -> str:
    return s.strip().split()[-1]


def getTopFrequence(top=100) -> Set[str]:
	word_set = set()
	with open('./freq.txt', "r") as freq:
		for _ in range(top):
			word_set.add(freq.readline().strip())
	return word_set


def getRandomFrom(seq) -> str:
    return random.sample(seq, 1)[0] if seq else None


def hasEOS(s: str) -> int:
	length = len(s)

	period = s.index('.') if '.' in s else length
	exclmation = s.index('!') if '!' in s else length
	question = s.index('?') if '?' in s else length

	return min(period, exclmation, question)


def calcSimilarity(s1: List[str], s2: List[str]) -> int:
	set1, set2 = set(getWordList(s1)), set(getWordList(s2))
	return len(set1 & set2)
