num = int(input("Enter a number: "))
num_str = str(num)
order = len(num_str)
sum = 0

for digit in num_str:
    sum += int(digit) ** order

if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")







