import sys

x=str(sys.argv[1])
l=len(x)
for i in range(l):
 y=x.replace("()", "")
 x=y

if y=="":
 print "YES"
else:
 print "NO"





