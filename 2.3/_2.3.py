a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

import math

D = b**2 - 4 * a *c

print(D)

if(D<0):

#z = a*math.pow(x,2) + b*x +c == 0


x1 =( -b + math.pow((math.pow(b,2) -4*a*c),0.5) )/(2*a)

x2 = (-b - math.pow((math.pow(b,2) -4*a*c),0.5)) /2*a

print(x1)
print(x2)

