import sys

x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])



if z != 1:
 q="."
else:
 q="!"
 
e="Everybody sing a song:"
a="la"
l=(a+"-")*(x-1)+a


if y==0:
 print e+q
else:
 print e+" "+(l+" ")*(y-1)+l+q

