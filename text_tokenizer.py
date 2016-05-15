import csv
import nltk

textWriter = file('data.csv','w')
textAnalysis = csv.writer(textWriter)

textData = file('workfile.csv','r')
DA = csv.reader(textData)
for row in DA:
    print str(row)
