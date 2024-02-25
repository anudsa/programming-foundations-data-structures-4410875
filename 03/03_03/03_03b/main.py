user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}
#Changing value of a key
user_preferences["language"]="Spanish"

#Adding value
user_preferences["color"]="red"
#Delete item
del user_preferences["timezone"]
#delete and retrieve
removed_value = user_preferences.pop('font_size')
print(removed_value)
print(user_preferences)
