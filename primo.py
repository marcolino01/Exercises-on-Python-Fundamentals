from cmath import asin, cos, sin, sqrt
from math import radians


print("hello world")


print(10**10)
print(sqrt(10))

r=6371
λ1=radians(59.9)
ϕ1 =radians(10.8)
λ2=radians(49.3) 
ϕ2=radians(-123.1)
d=2*r*asin(sqrt((sin(1/2*(ϕ2-ϕ1))**2)+cos(ϕ1)*cos(ϕ2)*(sin(1/2*(λ2-λ1))**2)))
print(d)
