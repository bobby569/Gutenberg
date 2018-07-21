import util
import collections, heapq

class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.word_dict = None
        self.word_trie = None
        self.setWordDict()


    def setWordDict(self):
        txt = open(self.filename, "r")

        word_dict = {}
        for line in txt:
            word_list = util.getWordList(line)
            for word in word_list:
                for w in util.extractWord(word):
                    if w:
                        word_dict[w] = word_dict.get(w, 0) + 1

        txt.close()
        self.word_dict = word_dict


    def getNextWordDict(self):
        txt = open(self.filename, "r")

        prev_word, next_words = "", collections.defaultdict(set)
        for line in txt:
            words = util.getWordList(line)
            words.insert(0, prev_word)
            prev_word = words[-1]

            for x, y in zip(words, words[1:]):
                if x.isalpha() and y.isalpha():
                    next_words[x].add(y)

        txt.close()
        return next_words


    def getWordTrie(self):
        if self.word_trie:
            return self.word_trie

        txt = open(self.filename, "r")

        buffer, word_trie = "", util.Trie()
        for line in txt:
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

        txt.close()
        self.word_trie = word_trie
        return word_trie


    def printAllSentence(self, ptr, sentence, res):
        if not ptr:
            res.append(sentence.strip())
            return
        for k, v in ptr.items():
            self.printAllSentence(v, "%s %s" % (sentence, k), res)


    # 2a
    def getTotalNumberOfWords(self):
        return sum(self.word_dict.values())

    # 2b
    def getTotalUniqueWords(self):
        return len(self.word_dict)

    # 2c
    def get20MostFrequentWords(self):
        h = []
        for k, v in self.word_dict.items():
            if v > 3:
                heapq.heappush(h, (v, k))
                if len(h) > 20:
                    heapq.heappop(h)
        return sorted([[k, v] for v, k in h], key=lambda x: x[1], reverse=True)

    # 2d
    def get20MostInterestingFrequentWords(self, no_common=100):
        freq_word = util.getTopFrequence(no_common)

        h = []
        for k, v in self.word_dict.items():
            if k not in freq_word:
                heapq.heappush(h, (v, k))
                if len(h) > 20:
                    heapq.heappop(h)
        return sorted([[k, v] for v, k in h], key=lambda x: x[1], reverse=True)

    # 2e
    def get20LeastFrequentWords(self):
        h = []
        for k, v in self.word_dict.items():
            if v <= 3:
                heapq.heappush(h, (-v, k))
                if len(h) > 20:
                    heapq.heappop(h)
        return sorted([[k, -v] for v, k in h], key=lambda x: x[1])

    # 3a
    def getFrequencyOfWord(self, word):
        txt = open(self.filename, "r")
        cnt, res = 0, []

        for line in txt:
            if line.startswith("Chapter"):
                res.append(cnt)
                cnt = 0
            else:
                cnt += line.count(word)

        txt.close()
        res.append(cnt)
        return res[1:]

    # 4
    # In order to keep relatively small buffer,
    # at most one period can appear in quote.
    def getChapterQuoteAppears(self, quote):
        quote = quote.lower()
        txt = open(self.filename, "r")
        ch, buffer = "", ""

        for line in txt:
            if line.startswith("Chapter"):
                ch = util.extractChapterNumber(line)
                buffer = ""
            buffer += line.lower().strip() + " "
            if quote in buffer:
                txt.close()
                return int(ch)
            idx = buffer.index('.') if '.' in buffer else -1
            buffer = buffer[idx+1:]
        txt.close()
        return -1

    # 5a
    def generateSentence(self):
        next_words = self.getNextWordDict()
        sentence = ['the']

        while len(sentence) < 20:
            last_word = sentence[-1]
            next = util.getRandomFrom(next_words[last_word])
            if not next:
                break
            sentence.append(next)

        return ' '.join(sentence)

    # 6a
    def getAutocompleteSentence(self, startOfSentence):
        word_trie = self.getWordTrie()
        pieces = util.getWordList(startOfSentence)
        ptr = word_trie.search(pieces)

        res = []
        self.printAllSentence(ptr, "", res)
        return ["%s %s" % (startOfSentence, s) for s in res]

    # 7a
    def findClosestMatchingQuote(self, quote):
        txt = open(self.filename, "r")

        ch, buffer = "", ""
        curr = ["", "", 0]  # [chapter, actual-quote, similarity]

        for line in txt:
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

        txt.close()
        return "%s - Chapter %s" % (curr[1], curr[0])
