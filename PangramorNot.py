import string
def is_pangram(string):
    alphabet = set(string.ascii_lowercase)
    return set(string.lower()) >= alphabet

sentence = input("Enter a sentence: ")

if is_pangram(sentence):
    print("Pangram")
else:
    print("Not a pangram")



