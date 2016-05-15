import pickle
import random
from collections import Counter

def addWord(data, sentence):
    searchWord = sentence[-1]
    collectedData = []
    badwords = ['!','t','u2014','"','m','U0001f339','wo',')','(',']','/',':','U0001f496','yours','u260e','ufe0f','$','u2705','U0001f4a8','U0001f4b2','U0001f4a82','u2022','&','~','U0001f445','-','U0001f4a6','u2605','u221ae','u278b','and','u25ba','U0001f44c','n713-429-1951']
    for bigram in data:
        if str(bigram[0]) == str(searchWord) and str(bigram[1]) not in badwords:
            collectedData.append(str(bigram[1]))
    c = Counter(collectedData)
    wordsToAdd = c.most_common(25)
    print wordsToAdd
    return wordsToAdd[random.randint(0,len(wordsToAdd))][0]

def createQuote(data, length = 10):
    corpus = []
    sentence = []
    textToAnalyze = pickle.load(open(data,'rb'))
    for bigrams in textToAnalyze:
        for word in bigrams:
            if word not in corpus:
                corpus.append(word)
    x = random.randint(0, len(corpus))
    random_word = corpus[x]
    sentence.append(random_word)
    while len(sentence) < length:
        adding_word = addWord(textToAnalyze, sentence)
        sentence.append(adding_word)
    return sentence


advert = createQuote('pickled_corpus2.p',13)
print advert
