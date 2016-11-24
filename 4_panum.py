num=999
pd=0
rpd=0
i=0
while num>900:
    for i in range(1,99):
        pd=num*(num-i)
        pd=str(pd)
        rpd=pd[::-1]
        if pd==rpd:
            print("palindrome:",pd,"num:",num," ",num-i)
            break
    if pd==rpd:break
    num-=1

