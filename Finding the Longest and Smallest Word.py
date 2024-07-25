txt = input(": ")

#finding the longest word
longestWord = max(txt.split(), key=len)
smallestWord = min(txt.split(), key=len)
print(longestWord,"\n",smallestWord)