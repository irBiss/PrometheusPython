import sys

z=(sys.argv[1])

z=z.lower()
print z
z.replace (' ', '')
print z
x=list(z)
while ' ' in x: 
    x.remove(' ')

print x
y=len(x)


i=0
p= "YES"


while i<y:
 
 
 if x[i] != x[y-1-i]:
  p = "NO"
 i=i+1
print p




