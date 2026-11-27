''' Intials '''

name = "Avul Pakir Jainulabdeen Abdul Kalam "
parts = name.split()
intials = [p[0] + "." for p in parts[:-1]]
print(" ".join(intials + [parts[-1]]))