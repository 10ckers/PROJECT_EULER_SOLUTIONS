import time
t1=time.time()

marked = [0] * 20000000
value = 3
s = 2
while value < 20000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 20000000:
            marked[i] = 1
            i += value
    value += 2
print(s)
print(time.time()-t1)
