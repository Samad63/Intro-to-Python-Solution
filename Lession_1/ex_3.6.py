def rle(s):
    if not s:
        return ""
    out = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            out.append(s[i - 1] + str(count))
            count = 1
    out.append(s[-1] + str(count))
    return "".join(out)
def unrle(t):
    out, i = [], 0
    while i < len(t):
        ch, j = t[i], i + 1
        while j < len(t) and t[j].isdigit():
            j += 1
        out.append(ch * int(t[i + 1:j]))
        i = j
    return "".join(out)
from itertools import groupby
print(rle("aaabccdddd"))
print("".join(f"{k}{len(list(g))}" for k, g in groupby("aaabccdddd")))
print(unrle(rle("aaabccdddd")))