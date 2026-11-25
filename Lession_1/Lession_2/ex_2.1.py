''' Electricity Unit '''

old, new = 12345, 12652
rate, fixed = 6.50, 100

units = new - old
bill = units * rate + fixed
print("Units used :", units)
print(f"Bill amount: {bill:.2f}")