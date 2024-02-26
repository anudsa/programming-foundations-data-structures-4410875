#sets
primaryColor = set(["red","yellow","blue"])
primaryColor2 = {"red","yellow","blue"}
#checking membership
def isPrimary(colorsSet):
  if color in colorsSet:
    return True
  else:
    return False
isPrimary(primaryColor2)
primaryColor2.add("black")
color="black"
print(isPrimary(primaryColor))
print(isPrimary(primaryColor2))
