import math
x= float(input("значення х"))
if x>= -0.7:
   r=-6*x**2+math.sin(x),
elif x>-9.9:
   r=math.log10(math.fabs(x+math.sin((x))))
else:
   r=12+math.fabs(math.sin(2*x))
   
print(r)