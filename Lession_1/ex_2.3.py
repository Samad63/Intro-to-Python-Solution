''' Distance '''

import math

x1, y1 = 1, 2
x2, y2 = 4, 6
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance:", d)
print("hypot:", math.hypot(x2 - x1, y2 - y1))