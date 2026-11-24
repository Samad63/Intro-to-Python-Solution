''' Time Converter '''


total = 10000
hours = total // 3600
rest = total % 3600
minutes = rest // 60
seconds = rest % 60
print(f"{total} s = {hours} h {minutes} min {seconds} s")
