''' Receipt '''

items = [("Notebook", 3, 45.00), ("Pen", 10, 12.50), ("Folder", 2, 80.00)]
print(f"{'Item':<10}{'Qty':>5}{'Price':>10}{'Total':>12}")
print("-" * 37)
subtotal = 0
for name, qty, price in items:
    line = qty * price
    subtotal += line
    print(f"{name:<10}{qty:>5}{price:>10.2f}{line:>12.2f}")
gst = subtotal * 0.18
print("-" * 37)
print(f"{'Subtotal':<25}{subtotal:>12.2f}")
print(f"{'GST (18%)':<25}{gst:>12.2f}")
print(f"{'Grand total':<25}{subtotal + gst:>12.2f}")