def getWordList(line):
    return line.strip().split()

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
