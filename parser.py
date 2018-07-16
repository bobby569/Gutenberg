import util

class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.word_dict = None


    def getWordDict(self):
        if self.word_dict:
            return self.word_dict

        txt = open(self.filename, "r")

        word_dict = {}
        for line in txt:
            word_list = util.getWordList(line)
            for word in word_list:
                w = util.extractWord(word.lower())
                word_dict[w] = word_dict.get(w, 0) + 1

        txt.close()
        self.word_dict = word_dict
        return word_dict

    # 2a
    def getTotalNumberOfWords(self):
        txt = open(self.filename, "r")
        cnt = 0

        for line in txt:
            cnt += len(util.getWordList(line))

        txt.close()
        return cnt

    # 2b
    def getTotalUniqueWords(self):
        txt = open(self.filename, "r")
        word_set = set()

        for line in txt:
            word_list = util.getWordList(line)
            for word in word_list:
                word_set.add(word.lower())

        txt.close()
        return len(word_set)

    # 2c
    def get20MostFrequentWords(self):
        word_dict = self.getWordDict()

        i, res = 0, []
        for k in sorted(word_dict, key=word_dict.get, reverse=True):
            res.append([k, word_dict[k]])
            i += 1
            if i >= 20:
                break
        return res

    # 2d
    def get20MostInterestingFrequentWords(self, no_common=100):
        word_dict = self.getWordDict()
        freq_word = util.getTopFrequence(no_common)

        i, res = 0, []
        for k in sorted(word_dict, key=word_dict.get, reverse=True):
            if k in freq_word:
                continue
            res.append([k, word_dict[k]])
            i += 1
            if i >= 20:
                break
        return res

    # 2e
    def get20LeastFrequentWords(self):
        word_dict = self.getWordDict()

        i, res = 0, []
        for k in sorted(word_dict, key=word_dict.get):
            res.append([k, word_dict[k]])
            i += 1
            if i >= 20:
                break
        return res

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
            try:
                period = buffer.index('.')
                buffer = buffer[period+1:]
            except:
                pass
        txt.close()
        return -1

    # 5
    def getAutocompleteSentence(self, startOfSentence):
        pass

    # 6
    def findClosestMatchingQuote(self, string):
        pass


if __name__ == "__main__":
    p = Parser('./1342.txt')
    print("-----------2a-----------")
    print(p.getTotalNumberOfWords())
    print("-----------2b-----------")
    print(p.getTotalUniqueWords())
    print("-----------2c-----------")
    print(p.get20MostFrequentWords())
    print("-----------2d-----------")
    print(p.get20MostInterestingFrequentWords(150))
    print("-----------2e-----------")
    print(p.get20LeastFrequentWords())
    print("-----------3a-----------")
    print(p.getFrequencyOfWord("prejudice"))
    print("-----------4a-----------")
    print(p.getChapterQuoteAppears("It is a truth universally acknowledged, \
                                   that a single man in possession of a good fortune, \
                                   must be in want of a wife."))
