# Linear Search
my_list = [8, 5, 0, 3, 9, 7]
ITEM = 7
#find the position of the given item
#Linear Search
def isElementInList(ITEM,LIST):
  for index,item in enumerate(LIST):
    if item == ITEM :
      print("The item has the index: {}".format(index)) 
      return True
  print("The item is not in the list") 
  return False
print(isElementInList(ITEM,my_list))
#Alternatively:
print(f"{my_list[my_list.index(ITEM)]} is in position {my_list.index(ITEM)}")