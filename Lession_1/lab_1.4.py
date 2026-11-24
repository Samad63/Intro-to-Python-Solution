P = 100000
r = 7.5 / 100
n = 4
t = 5

A = P * (1 + r / n) ** (n * t)
interest = A - P
print(f"Amount    : {A:,.2f}")
print(f"Interest  : {interest:,.2f}")