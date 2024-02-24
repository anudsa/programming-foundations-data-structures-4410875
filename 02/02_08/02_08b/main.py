my_list = [1, 7, 3]
print(sorted(my_list, reverse = True))
studentGrades=[("abc",23),("xyz",22),("poi",90),("qwe",32)]
print(sorted(studentGrades))
print(sorted(studentGrades,key= lambda inputTuple:inputTuple[0]))
#Here we are sorting based on the element with index 1 of the tuple 
print(sorted(studentGrades,key= lambda inputTuple:inputTuple[1]))
print(sorted(studentGrades,key= lambda inputTuple:inputTuple[1],reverse=True))