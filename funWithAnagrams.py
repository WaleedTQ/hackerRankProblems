def removeAnagrams(textOld, textNew):
    indexList = []
    for i in range(0, len(textOld)):
        for x in range(i+1, len(textNew)):
            if checkIfAnagram(textOld[i], textNew[x]):
                if (not x in indexList):
                    indexList.append(x)

    count = 0
    result = []
    for i in range(0, len(textOld)):
        if i not in indexList:
            result.append(textOld[i])
    return result

def checkIfAnagram(word1, word2):
    if (sorted(word1) == sorted(word2)):
        return True
    return False


def funWithAnagrams(text):
    # Write your code here
    resultantList = text.copy()
    listLength = int(len(text)) - 1
    removeAnagrams(text,resultantList)

    resultantList.sort()
    return resultantList
    
/*** Hacker Rank code here ***/
