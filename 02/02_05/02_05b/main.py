seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]
#Accessing the second student sitting in the third row
#Zero indexing, first rows, then columns.
#print(seating_chart[2][1])

#Display each student with their row and seat number.
print("This is a tuple where the first element is the index(row number) and the second is a list (row content)")
for data in enumerate(seating_chart):
  print(data)


print("Students & rows:")

#start with each row number with sudents in that row
for data in enumerate(seating_chart):
  rowNumber=data[0]
  students=data[1]
  print(f"This is row {rowNumber+1}. The students in it are : {students}")

print("version 2")
for rowNumberIndex,studentsList in enumerate(seating_chart):
  #We get the row number and the row list here
  print(f"\nThis is row {rowNumberIndex+1}. The students in it are : {studentsList}\n")
  for studentSeat,Student in enumerate(studentsList):
    #Now we get the seat number, it's the index of the studentsList & the student name
    print(f"{Student} from row {rowNumberIndex+1} has the seat: {studentSeat+1}")
