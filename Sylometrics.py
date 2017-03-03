def byFreq(pair):
    return pair[1]
    
def shakespeare():
    textList = ["macbeth.txt" , "othello.txt" , "allswell.txt"]
    finalListShake = []
    for i in range(0,len(textList)):
        text = open(textList[i],'r').read()
        text = text.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = text.replace(ch, '')
        words = text.split()
        finalListShake += [words]  
    #construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1
    #output analysis of n most frequent words.
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    D = {}
    for i in range(50):
        word, count = items[i]
        cnt = count
        txtLength = len(counts)
        ratio = 1.0 * cnt/txtLength
        D[word] = ratio
    return(D)
    
def melville():
    textList = ["moby.txt" , "bartleby.txt" , "omoo.txt"]
    finalListMel = []
    for i in range(0,len(textList)):
        text = open(textList[i],'r').read()
        text = text.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = text.replace(ch, '')
        words = text.split()
        finalListMel += [words]  
    # construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1
    # output analysis of n most frequent words.
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    D = {}
    for i in range(50):
        word, count = items[i]
        cnt = count
        txtLength = len(counts)
        ratio = 1.0 * cnt/txtLength
        D[word] = ratio
    return(D)
    
def main():
    '''analyzes word frequency in a file and returns n most frequent words.'''
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.")
    # get the sequence of words from the file
    fname = raw_input("File to analyze: ")
    textList = fname.split(" ")
    finalList = []
    for i in range(0,len(textList)):
        text = open(textList[i],'r').read()
        text = text.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = text.replace(ch, '')
            text = text.replace('"','')
        words = text.split()
        finalList += [words]  
    # construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1
    # output analysis of n most frequent words.
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    D = {}
    for i in range(50):
        word, count = items[i]
        c = count
        t = len(counts)
        ratio = 1.0 * c/t
        D[word] = ratio
    return D
 
#loop thru the dict main (unknown)
#check if specific word is in shakespeare dict and check if it is in melville's
#if it is get the diff or the ratios
#add it to a sumed "variable" that keeps track of all the differences
#if its not make the ratio differences equal to 0 and add that to the sumed variable
#repeat for melville.
