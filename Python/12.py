import sys

x=str(sys.argv[1])
y=str(sys.argv[2])
print x
print y

s=0
d=0
qty=0
while x<y:
  
  
  q=list(x)
  
  print q
  l=len(q)
  for i in range(l):
   s=s+q[:4]
   d=d+q[4:]
   if s==d:
    qty=qty+1
 
print qty	
   
  
 







