#stacks
#ordered lists where you can only add and remove from the top
stackOfCards = []
stackOfCards.append("carta1")
stackOfCards.append("as")
stackOfCards.append("joker")
print(stackOfCards)
#bottom = left = front 
#top = right = back
removed=stackOfCards.pop()
print(stackOfCards)
print(removed)
#retrieving last element without deleting it:
print(stackOfCards[-1])
#check if stack is empty, true if the list has items, false if it's empty
if stackOfCards:
  print("Not empty")
else:
  print("empty")
#find size of the stack
size=len(stackOfCards)
print(size)