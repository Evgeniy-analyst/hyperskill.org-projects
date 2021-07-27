# Save the input in this variable
ticket = list(input())
b = [int(digit) for digit in ticket]
# Add up the digits for each half
half1 = b[0] + b[1] + b[2]
half2 = b[-1] + b[-2] + b[-3]

# Thanks to you, this code will work
# print(b)
# print(half1, half2)
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
