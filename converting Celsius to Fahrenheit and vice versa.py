def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C/F): ")

if unit.upper() == "C":
    fahrenheit = celsius_to_fahrenheit(temperature)
    print("Temperature in Fahrenheit:", fahrenheit)
elif unit.upper() == "F":
    celsius = fahrenheit_to_celsius(temperature)
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid unit entered.")
