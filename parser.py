import util

class Parser:
    
    def __init__(self, filename):
        self.filename = filename

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
        txt = open(self.filename, "r")
        word_dict = {}

        for line in txt:
            word_list = util.getWordList(line)
            for word in word_list:
                word_dict[word] = word_dict.get(word, 0) + 1

        i, res = 0, []
        for k in sorted(word_dict, key=word_dict.get, reverse=True):
            res.append([k, word_dict[k]])
            i += 1
            if i >= 20:
                break
        
        txt.close()
        return res

    def get20MostInterestingFrequentWords(self, no_common=100):
        txt = open(self.filename, "r")

        txt.close()
        return

p = Parser('./1342.txt')
print(p.getTotalNumberOfWords())
print(p.getTotalUniqueWords())
print(p.get20MostFrequentWords())