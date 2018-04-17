import sys

N = int(sys.argv[1])
s = None
i = 0
p = 0
r = 1

if N < 0:
  s='N is invalid'
if N == 1 or N==2:
	s=1
if N ==0:
	s= 0

     
if N>2:
   for count in range(int(N-1)):
    i = i + 1
    s = p+r
    p = r
    r=s
print(s)