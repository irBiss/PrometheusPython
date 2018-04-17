import sys

x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
e="Everybody sing a song:"
l="La-La"
q="!"
if z != 1:
 q="."
 if y==0:
  print e+q
 else:
  print e+(l+" ")*(y-1)+l+q
else:
 print e+(l+" ")*(y-1)+l+q

