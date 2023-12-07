''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''
#Array = list, each index contains a number of pets per student.
#To find the average you have to add each index content and divide it over the amount of students(index total+1)
numberOfPets = [0,1,0,2,1,1,4,0,0,0,3,2,1,3,0,2,2,4]

def findAverage(numberOfPets):
  sum = 0
  #We need a for loop bc we know the number of iterations, which is the lenght of the array
  for index in numberOfPets:
    sum = sum + index
  arrayLength=len(numberOfPets)
  average = sum / arrayLength
  return(average)

print(findAverage(numberOfPets))

#Mutating the list
#1 student got 3 dogs, 1 got a cat & the last one got 2 dogs.
numberOfPets[2]+=3
numberOfPets[3]+=1
#Accesing the last item can be done with a negative index
numberOfPets[-1]+=2

#New items can be added with the append function
numberOfPets.append(4)

#Average after editing the list
print(findAverage(numberOfPets))