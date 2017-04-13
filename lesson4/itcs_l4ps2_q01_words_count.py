# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def split_string(source,splitlist):
    result = []
    for pos in range(0,len(splitlist)):
        if not result:
            for word in source.split(splitlist[pos]):
                if word:
                    result.append(word)
        else:
            tempList = []
            for element in result:
                for word in element.split(splitlist[pos]):
                    if word:
                        tempList.append(word)
            result = tempList
    return result

def count_words(content):
    resultList = split_string(content," ,*")
    return len(resultList)

passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
#>>>56

