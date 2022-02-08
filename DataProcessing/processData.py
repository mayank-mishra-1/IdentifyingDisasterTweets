import csv
import numpy as np

words = []
wordCount = []

nonDisasterWords = []
nonDisasterWordCount = []


def tokenizeString(tweet):
    wordsInTweet = []
    currWord = ""
    for i in tweet:
        if(i == ' ' or i == '.' or i == '?' or i == '!'):
            wordsInTweet.append(currWord)
            currWord = ""
        else:
            currWord += i
    return wordsInTweet

def takeSecond(elem):
    return elem[1]

def populateIgnoreWords():
    ignoreWords = ['']
    with open('ignoreWords.txt') as file:
        fileReader = csv.reader(file, delimiter=',')
        for row in fileReader:
            ignoreWords.append(row[0])
    return ignoreWords


ignoreWords = populateIgnoreWords()

print("Sifting through data...")
with open('Data/train.csv') as file:
    fileReader = csv.reader(file, delimiter=',')
    for row in fileReader:
        wordsInTweet = tokenizeString(row[3])
        for j in wordsInTweet:
            if j not in ignoreWords:
                if(row[4] == '1'):
                    if j not in words:
                        words.append(j)
                        wordCount.append(1)
                    else:
                        index = words.index(j)
                        wordCount[index] += 1
                else:
                    if j not in nonDisasterWords:
                        nonDisasterWords.append(j)
                        nonDisasterWordCount.append(1)
                    else:
                        index = nonDisasterWords.index(j)
                        nonDisasterWordCount[index] += 1

    wordsAndWordCount = []
    nonDisasterWordsAndCount = []
    print("Data Collected...")

    for idx in range(len(words)):
        wordsAndWordCount.append((words[idx], wordCount[idx]))
    wordsAndWordCount.sort(reverse=True,key = takeSecond)
    for idx in range(len(nonDisasterWords)):
        nonDisasterWordsAndCount.append((nonDisasterWords[idx], nonDisasterWordCount[idx]))
    nonDisasterWordsAndCount.sort(reverse=True,key = takeSecond)


    with open('topWordsDisasterTweets.txt','a') as outputfile:
        for i in wordsAndWordCount:
            outputfile.write(str(i))
            outputfile.write("\n")
    with open('topWordsNonDisasterTweets.txt','a') as outputfile:
        for i in nonDisasterWordsAndCount:
            outputfile.write(str(i))
            outputfile.write("\n")
    print("Data written... Process Complete.")

   
  