#Determine whether a piece of text has unique characters
#data is a string, iterate through it and compare if the letter has already be seen or not.
def has_unique_characters(data):
    #store characters from word in a set (iterating)
    setOfCharacters=set()
    for character in data:
        setOfCharacters.add(character)
    #alternatively= newSet=set(data)
    if len(data) > len(setOfCharacters) :
        return False
    else:
        return True
print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
