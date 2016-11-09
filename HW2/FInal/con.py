import string
def concordance(f, unique):
    #read in every line of the stream
    myDict = {}
    exclude = set()

    for index, line in enumerate(f):
        ##for every word in that line
        for word in line.split():

            #do some word parsing here
            word = word.lower()

            #if the ending is not an alphabet character
            if not word[-1].isalpha():
                word = word[:-1]

            #if the first letter is not an alpha
            if not word[0].isalpha():
                word = word[1:]

            #now that we are in the word,
            #make sure to keep all hyphens and apostrophes
            myChar = []
            for c in word:
                #if we have a letter hyphen or apostrophes
                if c.isalpha() or c is '-' or c is '\'':
                    myChar.append(c)

            #print word after reassembly
            word = ''.join(myChar)

            #if we have a brand new word, we add it to the dictionary
            if word not in myDict.keys():
                myDict[word] = []

            #now we check our unique key
            #if true, we cannot add the index twice
            if unique:
                #if we do not have the index in the list
                if index not in myDict[word]:
                    myDict[word].append(index)

            #if the unique key is false, we add it no matter what
            else:
                myDict[word].append(index)

    return myDict