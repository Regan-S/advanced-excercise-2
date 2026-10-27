import math

a = 5
b = 10
c = 7

a += 3

b *=2

c %= 4

result = math.sqrt(a**2 + b**2 + c**2)

print(f"{result:.2f}")

x = int(input("enter integer x: "))
y = int(input("enter integer y: "))
z = int(input("enter integer z: "))

is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50

final_condition = is_even and is_positive and is_in_range

print(final_condition)


base_score = float(input("enter your base score: "))

adjusted_score = base_score + 5 - 10

final_score = max(0.0, min(adjusted_score, 100.0))

if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "b"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"        
else:
    grade = "f"

    print(f"final score: {final_score}")
    print(f"grade: {grade}")


    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Enter an operation (+, -, *, /, %, **): ")


try:
    if operation == "+":
        result = num1 + num2
    elif operation == "_":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    elif operation == "**":
        result = num1 ** num2
    else:
        result = "Invalid operation selected"

    print(f"Result: {result}")         

except ZeroDivisionError:
    print("Error: Division or modulus by zero is not allowed.")   

