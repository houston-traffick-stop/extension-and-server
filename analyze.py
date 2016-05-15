import nltk
import urllib
import BeautifulSoup

def analyzeText(url):
    dataToReturn = []
    information = urllib.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(information)
    for paragraphs in soup.findAll('p', text = True):
        sentences = nltk.word_tokenize(paragraphs)
        for word in sentences:
            dataToReturn.append(word)
    return dataToReturn

