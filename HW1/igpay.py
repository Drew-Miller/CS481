#assume input is just one string and is a word
vowels = ['a', 'e', 'i', 'o', 'u']
tag = "ay"

def igpay(original):
    #keep track of casing here
    uppers = keepCase(original)
    original = original.lower()

    #if we start with a vowel as the first letter
    #simply append way and return
    if original[0] in vowels:
        original = original + "way"
        return reCase(original, uppers)

    else:
        # the consonant(s) that we will append
        # to the end of the word
        end = ""
        for c in original:
            #if we hit a vowel, we append the reserved vowels and the tag
            if c in vowels:
                original = original + end + tag
                return reCase(original, uppers)

            # if we currently are not reading vowels
            else:
                #then we append the characters to the end
                end = end + c
                #remove the beginning character
                original = original[1:]

        #if we reach here, then there were no vowels in the word
        #return the word
        return reCase(end, uppers)

#used to return a set number of indices to capitalize based
#on input
def keepCase(word):
    uppers=[]
    for index, c in enumerate(word):
        if c.isupper():
            uppers.append(index)

    return uppers

def reCase(word, uppers):
    l = list(word)

    if (len(uppers) + 2) >= (len(word)):
        for i, item in enumerate(l):
            l[i] = l[i].upper()

    else:
        for i in uppers:
            l[i] = l[i].upper()


    return "".join(l)



if __name__ == "__main__":
    print(igpay("Yes"))
    print(igpay("Parrot"))
    print(igpay("Knights"))
    print(igpay("Add"))
    print(igpay("Office"))
    print(igpay("WHY"))