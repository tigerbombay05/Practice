no1 = float(input("Enter First Number: "))
no2 = float(input("Enter Second Number: "))
operator = input("Enter Operator: ")
result = 0

if (operator == "+"):
    result = no1 + no2
elif (operator == "-"):
    result = no1 - no2
elif (operator == "*"):
    result = no1 * no2
elif (operator == "/"):
    result = no1 / no2

print(f"{no1} {operator} {no2} = {result}")