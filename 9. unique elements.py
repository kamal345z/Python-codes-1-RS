userinput = input("Enter elements separated by spaces: ").split()
if len(userinput) == len(set(userinput)):
    print("All elements are unique.")
else:
    print("There are duplicates.")