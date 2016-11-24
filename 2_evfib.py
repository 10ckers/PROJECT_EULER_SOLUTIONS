i=1
f=1
sum=0
while True:
    i,f=f,i+f
    if f<=4000000:
        if f%2==0:
            sum+=f
    else:
        break
   # elif f%2==0:
    #    sum+=f
print(sum)


