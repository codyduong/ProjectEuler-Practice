#god knows this doesnt work, pushed from laptop
import re

l = ['', 1]
for i in range(2,1000):
    s = str(1/i)[2:]
    r = re.search(r'(\d+).*\1', s)
    r2 = re.search(r'^(.)\1*$', s)
    if r2 != None:
        print(r2)
        continue
    try:
        t = len(str(r.group(0)))
        #print(t)
        if len(l[0]) < t:
            l = [r.group(0), t, i]
    except:
        continue

print(l)