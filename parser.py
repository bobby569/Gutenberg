import collections
import heapq
from typing import List, Tuple

import util
from trie import Trie

class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.word_dict = None
        self.word_trie = None
        self.setWordDict()


    def setWordDict(self) -> None:
        word_dict = {}
        with open(self.filename, "r") as fd:
            for line in fd:
                for word in util.getWordList(line):
                    for w in util.extractWords(word):
                        if w:
                            word_dict[w] = word_dict.get(w, 0) + 1
        self.word_dict = word_dict


    def getNextWordDict(self) -> collections.defaultdict:
        prev_word, next_words = "", collections.defaultdict(set)
        with open(self.filename, "r") as fd:
            for line in fd:
                words = [prev_word] + util.getWordList(line)
                prev_word = words[-1]

                for x, y in zip(words, words[1:]):
                    if x.isalpha() and y.isalpha():
                        next_words[x].add(y)
        del next_words[""]
        return next_words


    def getWordTrie(self) -> Trie:
        if self.word_trie:
            return self.word_trie

        buffer, word_trie = "", Trie()
        with open(self.filename, "r") as fd:
            for line in fd:
                if line.startswith("Chapter"):
                    buffer = ""
                    continue
                buffer += line.lower().strip() + " "

                while True:
                    idx = util.hasEOS(buffer)
                    if idx == len(buffer):
                        break
                    sentence = buffer[:idx+1]
                    buffer = buffer[idx+1:].lstrip()
                    word_trie.insert(sentence.split())

        self.word_trie = word_trie
        return word_trie


    def printAllSentence(self, ptr, sentence, res) -> None:
        if not ptr:
            res.append(sentence.strip())
            return
        for k, v in ptr.items():
            self.printAllSentence(v, "%s %s" % (sentence, k), res)


    # 2a
    def getTotalNumberOfWords(self) -> int:
        return sum(self.word_dict.values())

    # 2b
    def getTotalUniqueWords(self) -> int:
        return len(self.word_dict)

    # 2c
    def get20MostFrequentWords(self) -> List[Tuple[str, int]]:
        h = []
        for k, v in self.word_dict.items():
            if v > 3:
                heapq.heappush(h, (v, k))
                if len(h) > 20:
                    heapq.heappop(h)
        return sorted([[k, v] for v, k in h], key=lambda x: -x[1])

    # 2d
    def get20MostInterestingFrequentWords(self, no_common=100) -> List[Tuple[str, int]]:
        freq_word = util.getTopFrequence(no_common)

        h = []
        for k, v in self.word_dict.items():
            if k not in freq_word:
                heapq.heappush(h, (v, k))
                if len(h) > 20:
                    heapq.heappop(h)
        return sorted([[k, v] for v, k in h], key=lambda x: -x[1])

    # 2e
    def get20LeastFrequentWords(self) -> List[Tuple[str, int]]:
        h = []
        for k, v in self.word_dict.items():
            if v <= 3:
                heapq.heappush(h, (-v, k))
                if len(h) > 20:
                    heapq.heappop(h)
        return sorted([[k, -v] for v, k in h], key=lambda x: x[1])

    # 3a
    def getFrequencyOfWord(self, word: str) -> List[int]:
        cnt, res = 0, []
        with open(self.filename, "r") as fd:
            for line in fd:
                if line.startswith("Chapter"):
                    res.append(cnt)
                    cnt = 0
                else:
                    cnt += line.count(word)
        res.append(cnt)
        return res[1:]

    # 4
    # In order to keep relatively small buffer,
    # at most one period can appear in quote.
    def getChapterQuoteAppears(self, quote: str) -> int:
        ch, buffer, quote = "", "", quote.lower()
        with open(self.filename, "r") as fd:
            for line in fd:
                if line.startswith("Chapter"):
                    ch = util.extractChapterNumber(line)
                    buffer = ""
                buffer += line.lower().strip() + " "
                if quote in buffer:
                    return int(ch)
                idx = buffer.find('.')
                buffer = buffer[idx+1:]
        return -1

    # 5a
    def generateSentence(self) -> str:
        sentence, next_words = ['the'], self.getNextWordDict()

        for _ in range(19):
            last_word = sentence[-1]
            _next = util.getRandomFrom(next_words[last_word])
            if not _next:
                break
            sentence.append(next)

        return ' '.join(sentence)

    # 6a
    def getAutocompleteSentence(self, startOfSentence: str) -> List[str]:
        word_trie = self.getWordTrie()
        pieces = util.getWordList(startOfSentence)
        ptr = word_trie.search(pieces)

        res = []
        self.printAllSentence(ptr, "", res)
        return ["%s %s" % (startOfSentence, s) for s in res]

    # 7a
    def findClosestMatchingQuote(self, quote: str):
        ch, buffer = "", ""
        curr = ["", "", 0]  # [chapter, actual-quote, similarity]

        with open(self.filename, "r") as fd:
            for line in fd:
                if line.startswith("Chapter"):
                    ch = util.extractChapterNumber(line)
                    buffer = ""
                    continue
                buffer += line.lower().strip() + " "
                while True:
                    idx = util.hasEOS(buffer)
                    if idx == len(buffer):
                        break
                    sentence = buffer[:idx+1].strip()
                    sim = util.calcSimilarity(quote, sentence)
                    if sim > curr[2]:
                        curr = [ch, sentence, sim]
                    buffer = buffer[idx+1:].lstrip()
        return "%s - Chapter %s" % (curr[1], curr[0])
