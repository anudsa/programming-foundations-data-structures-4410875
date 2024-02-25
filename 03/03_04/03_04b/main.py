#Create a function that takes in a dictionary and creates a new one without the empty values
#An empty dictionary might be given or one with no empty values
user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}
#Create a new dict, iterate through each item of the original dict, check if the values are "None"
#if not, add it to the new dict, if so, do not add it to the new list (just skip it)
#O(n) time complexity:
def update_preferences(user_pref):
    updatedDict = {}
    for key, value in user_pref.items():
        if value != None:
            updatedDict[key]=value
    return updatedDict
#With dictionary comprehension:
def update_preferences_comp(user_pref):
    updatedDict = {
        key:value for key,value in user_pref.items() if value!=None
    }
    return updatedDict
print(update_preferences_comp(user_preferences))
