first = complex(input((" Enter the first number")))
second = complex(input(("Enter the second number")))
result = first + second
print(result)

# print(type(first))
# print(type(second))

if result.imag == 0:
    print("The result is a real number:", result.real)
