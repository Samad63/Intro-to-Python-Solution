''' Masking '''

number = "123456761234"
masked = "XXXX-XXXX-" + number[-4:]
print(masked)

# works for any 12-digit number
for n in ("987654321098", "000011184378"):
    print("XXXX-XXXX-" + n[-4:])