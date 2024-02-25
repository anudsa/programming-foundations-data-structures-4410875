# Key: State
# Value: Capital
countriesAndCapitals={
  "Mexico":"Mexico City",
  "Albania":"Tirana",
  "Malaysia":"Kuala Lumpur",
                   }
#print(f"The capital of Malasya is: {countriesAndCapitals['Malaysia']}")
print("\nVersion 1: \n")
for key in countriesAndCapitals.keys():
  print(f"The capital of {key} is: {countriesAndCapitals[key]}")
print("\nVersion 2: \n")

for country, capital in countriesAndCapitals.items():
  print(f"The capital of {country} is: {capital}")