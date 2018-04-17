import sys
x=int(sys.argv[1])
y=int(sys.argv[2])

def counter(n, m):
 i=0
 sf=[]
 if n> m:
  while i != m:
   
   sf.append(1)
   
   i=i+1
  sf.append(m)
  for j in range(m,n):
   next=0
   for k in range (m):
    next=sf[len(sf)-k-1]+next
   sf.append(next)
 else:
  while i != m:
   
   sf.append(1)
   i=i+1
 print sf   
 return sf[n-1]
  
  
  
print counter(x, y)