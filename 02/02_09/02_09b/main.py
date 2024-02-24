#Create a function that finds the second smallest item in a list of integers
#The list is not sorted
#The list could be empty or only have one item, if so, return none.
#No duplicates in the list
list1 = [5, 8, 3, 2, 6]
list2 = []
list3 = [1]

def find_second_smallest(my_list):
    if (len(my_list)) < 2:
        return "none"
    else:
        return sorted(my_list)[1]

print(find_second_smallest(list3))