num = int(input("Enter a number : "))
num_str = str(num)
sum = 0
for digit in num_str:
    sum += int(digit)
print("Sum of digits : ", sum)
