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
                word_dict[word] = word_dict.get(word, 0) + 1

        txt.close()
        self.word_dict = word_dict
        return word_dict


    def getTotalNumberOfWords(self):
        txt = open(self.filename, "r")
        cnt = 0

        for line in txt:
            cnt += len(util.getWordList(line))

        txt.close()
        return cnt


    def getTotalUniqueWords(self):
        txt = open(self.filename, "r")
        word_set = set()

        for line in txt:
            word_list = util.getWordList(line)
            for word in word_list:
                word_set.add(word)

        txt.close()
        return len(word_set)


    def get20MostFrequentWords(self):
        word_dict = self.getWordDict()

        i, res = 0, []
        for k in sorted(word_dict, key=word_dict.get, reverse=True):
            res.append([k, word_dict[k]])
            i += 1
            if i >= 20:
                break
        return res


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


    def get20LeastFrequentWords(self):
        word_dict = self.getWordDict()

        i, res = 0, []
        for k in sorted(word_dict, key=word_dict.get):
            res.append([k, word_dict[k]])
            i += 1
            if i >= 20:
                break
        return res


if __name__ == "__main__":
    p = Parser('./1342.txt')
    print(p.getTotalNumberOfWords())
    print(p.getTotalUniqueWords())
    print(p.get20MostFrequentWords())
    print(p.get20MostInterestingFrequentWords(200))
    print(p.get20LeastFrequentWords())
