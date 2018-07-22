import parser

if __name__ == "__main__":
    p = parser.Parser('./1342.txt')
    print("-----------2a-----------")
    print(p.getTotalNumberOfWords())
    print("-----------2b-----------")
    print(p.getTotalUniqueWords())
    print("-----------2c-----------")
    print(p.get20MostFrequentWords())
    print("-----------2d-----------")
    print(p.get20MostInterestingFrequentWords(200))
    print("-----------2e-----------")
    print(p.get20LeastFrequentWords())
    print("-----------3a-----------")
    print(p.getFrequencyOfWord("sister"))
    print("-----------4a-----------")
    print(p.getChapterQuoteAppears("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."))
    print("-----------5a-----------")
    print(p.generateSentence())
    print("-----------6a-----------")
    res = p.getAutocompleteSentence("I do not")
    for s in res:
        print(s)
    print("-----------7a-----------")
    print(p.findClosestMatchingQuote("universally acknowledged"))
