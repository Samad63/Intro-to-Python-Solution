''' Swap without temp '''
# tuple assignment
a, b = 10, 25
a, b = b, a
print("tuple swap :", a, b)


# arithmetic only
a, b = 10, 25
a = a + b
b = a - b 
a = a - b
print("arithmetic :", a, b)