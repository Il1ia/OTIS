import math
x=int(input("значення х"))
def f(x):
 y=math.pow(math.e, x**2) / math.cos(x+x**4)-(x+math.pow(x, 3))**1/4
 return(y)

print(f(x))