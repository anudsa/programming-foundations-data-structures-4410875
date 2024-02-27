#Make a function that checks if a piece of text has matching parenthesis
#() matching, ()),)() not matching, etc. 
#The opening parenthesis always comes before the closing one.
#So, check which appers first, that rules out one case.
#Count the number of opening and closing (additonal to seing its order) 
#in the non matching cases, we either have opened parenthesis that weren't closed
#or closed parentehsis before and open one.
#the function must take in a string and return Boolean.
#We're creating a stack out of a list, namely the string.
pieceOfText="(linkedin)" #matching
pieceOfText2=")(linkedin)" #not matching
pieceOfText3="(linkedin" #not matching
pieceOfText4=")(linkedin" #not matching
pieceOfText5 = "()" #M
pieceOfText6 = "(()"#NM
pieceOfText7 = "())"#NM
pieceOfText8 = "((()))"#M
pieceOfText9 = ")("#NM
pieceOfText10 = ""#NM
pieceOfText11 = "(a(b)c)d"  # Should print True
pieceOfText12 = "()()()"     # Should print True
pieceOfText13 = "a(bcd"     # Should print False
pieceOfText14 = "())(()"   # Should print False
def isMatching(text):
  opened=0;
  closed=0;
  textStack=list(text)
  for character in textStack:
    if character == "(":
      #compare the position of the opening parenthesis vs the closing ones.
      #if closed is greater than opened in this step, it means it found a closing parenthesis before.
      if closed > opened:
        return False
      opened += 1
    elif character == ")":
      closed += 1
  if opened != closed:
    return False
  return True

print(isMatching(pieceOfText)) #True
print(isMatching(pieceOfText2)) #False
print(isMatching(pieceOfText3)) #False
print(isMatching(pieceOfText4)) #False
print(isMatching(pieceOfText5))  # Should print True
print(isMatching(pieceOfText6))  # Should print False
print(isMatching(pieceOfText7))  # Should print False
print(isMatching(pieceOfText8))  # Should print True
print(isMatching(pieceOfText9))  # Should print False
print(isMatching(pieceOfText10)) #true
print(isMatching(pieceOfText11)) #True
print(isMatching(pieceOfText12)) #True
print(isMatching(pieceOfText13)) #False
print(isMatching(pieceOfText14)) #False