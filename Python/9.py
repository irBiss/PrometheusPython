import sys

z=str(sys.argv[1])

z=z.lower()
x=list (z)

while ' ' in x: 
    x.remove(' ')


y=len(x)


i=0
p= "YES"


while i<y:
 
 
 if x[i] != x[y-1-i]:
  p = "NO"
 i=i+1
print p




