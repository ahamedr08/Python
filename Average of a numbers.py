n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = float(input("Enter a number: "))
    numbers.append(num)

average = sum(numbers) / n
print("Average:", average)





