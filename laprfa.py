#To find the largest prime factor of num
num=600851475143
r=int(num/2)
for i in range(2,r):
    cnt=0
    for j in range(2,int(i/2)):  
        if i%j==0:
            cnt+=1
    if cnt<1 and num%i==0:
        print(i)    #prints the prime numbers.We have to check the listed prime #numbers and we find that 6857 is the largest PN.


