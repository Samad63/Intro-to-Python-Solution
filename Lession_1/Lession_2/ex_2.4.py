amount = 1788
for d in (500, 200, 100, 50, 20, 10, 5, 2, 1):
    count = amount // d
    amount = amount % d
    if count:
        print(f"{d:>4} x {count}")