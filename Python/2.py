import sys
from math import exp
from math import  pi

x=float(sys.argv[1])
y=float(sys.argv[2])
z=float(sys.argv[3])

s=(x-y)**2/(2*z**2)

f=1/(z*(2*pi)**(0.5))*exp(-s)


print f
