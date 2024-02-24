# Tuples are immutable array-like structures
coordinate = (2,3)
x= coordinate[0]
y= coordinate[1]
print(f"The x axis is {x} & y is {y}, therefore the coordinate is {coordinate}")
#function that returns 2 variables, area and perimeter of square
def squareOperations(side):
  area=side*side
  perimeter=4*side
  return (area,perimeter)

area, perimeter = squareOperations(2)

print(f"The area is: {area} The perimeter is: {perimeter}")


