def is_palindrome(name):
    if name==name[::-1]:
        return True
    else :
        return False
name=input("enter your name  : ")

print(is_palindrome(name) )