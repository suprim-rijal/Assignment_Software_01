# #Task6
import random as rd
n = 0 
userinput = int(input("How many random points do youwant to generate?"))
num = userinput
while userinput>=1:
 x = rd.uniform(-1,1) 
 y = rd.uniform(-1,1)
 if x**2 + y**2 <1:
    n+=1
 userinput-=1
pi = 4 * n / num
print(f"Approximation of pi is {pi}")
