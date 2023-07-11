name , char =input("enter comma sepaerted name and character:") . split(",")
print(f"length" ,{len(name)})
# print(f"character {name.lower().count(char.lower())}")


# char.lower()

#without space answer
print(f"character {name.strip().lower().count(char.strip().lower())}")