# Iteration

# Enumerate function
string = "Abracadabra"
for index, element in enumerate(string):
    print(index, element)

# Dummy variable
for __ in string:
    print(__)

# For-else
for i in range(50):
    print(i)
    if i == 51:
        break
else:
    print("Done.")
