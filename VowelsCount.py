string = input("Enter a string: ")
vowels = "aeiou"
count = 0

for char in string.lower():
    if char in vowels:
        count += 1

print("Number of vowels:", count)


