qty, price = 4, 12.5
total = qty * price            # fixed: prise - price (name error)
print("Total:", total)         # fixed: missing comma (syntax error)
avg = total / qty              # fixed: removed "+ 1" (logic error)
print("Average price:", avg)