import math
x=int(input("значення х"))
y=int(input("значення y"))
a=int(input("значення a"))
t=int(input("значення t"))
z=2.33*math.pi*(x*math.sin(y)+y*math.cos(a))+math.pow(math.e,a*t)
print(z)