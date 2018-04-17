import sys

x=str(sys.argv[1])
y=str(sys.argv[2])
flag=0
while x<=y:
 z=list(x)
 z.reverse()
 l=len(z)
 while l<6:
  z.append (0)
  l=len(z)
 

 d=0
 s=0
 
 s=s+int(z[0])+int(z[1])+int(z[2])
 d=d+int(z[3])+int(z[4])+int(z[5])
 if s==d:
  flag=flag+1
 
 x=int(x)+1
 x=str(x)
 
print flag

 





 


