import csv
with open('workfile.csv','r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print str(row)
        
