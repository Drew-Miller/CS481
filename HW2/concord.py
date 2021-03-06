#! usr/bin/env python3
#import statement

import sys
import collections
from collections import Counter
from con import *

#one way to print our results
#PRINT to TERMINAL
def sort(concord):
    #sort all of the items by key (word)
    concord = collections.OrderedDict(sorted(concord.items()))

    #sort the files that they are in alphabetically
    for k in concord.keys():
        #sort the key by the items in it (textfile names)
        concord[k] = collections.OrderedDict(sorted(concord[k].items()))

    return concord

def sysprint(concord):
    for k in concord.keys():
        print(k, end="")

        #summate the occurrances
        sum = 0
        for v in concord[k]:
            sum += len(concord[k][v])

        print(" (" + str(sum) + "):")

        #print the stream name
        for v in concord[k]:
            print("\t" + v + ":", end="")

            #outputs a list of the lines in that file
            #for which this word occurred
            #and the amount of occurrences
            for index, c in enumerate(Counter(concord[k][v])):
                if index != 0:
                    print(",", end="")
                print(" " + str(c), end="")
                if Counter(concord[k][v])[c] > 1:
                    print("(" + str(Counter(concord[k][v])[c]) + ")", end="")

            print()





#main function of the script
if __name__ == "__main__":
    concord = {}
    fileDicts = {}
    #set each file input concordance as the value
    #and the filename as the key
    for index, arg in enumerate(sys.argv):
        if not index > 0:
            continue

        stream = open(arg)
        fileDicts = concordance(stream, False)

        #iterate through each of the keys
        for key in fileDicts.keys():

            #if the key does not exist, we set it to a new dictionary
            if key not in concord.keys():
                #append the list of values from that concord
                #to the file name in the dictionary
                concord[key] = {}

            #add the new textfile:lines pair into the dictionary
            concord[key].update({arg:fileDicts[key]})

    sysprint(sort(concord))