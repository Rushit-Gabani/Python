#replace()
#find()

string = "she is beautiful and she is a good dancer"
# print(string.replace(" ","-"))

#print(string.find("is"))

#when 2nd was print that time

is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1 +1)
print(is_pos2)