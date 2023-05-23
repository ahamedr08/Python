def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

string = input("Enter a string: ")

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")








