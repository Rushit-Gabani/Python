# name = input("enter your name ")
# temp_var=""
# i =0
# while i<len(name):
#     if name[i] not in temp_var:
#         temp_var += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#         i += 1
        
        
        
# for infinty loop 

# while True:
    # print("hello world")
    
# using for loop 
name =input("enter your name : ")
temp =""
for i in range(0,len(name)):
    if name[i] not in temp :
     temp += name[i]
     print(f"{name[i]} : {name.count(name[i])}")
    i += 1    