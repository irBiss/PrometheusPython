import sys


def count_holes(n): 
 
 h={'0':1, '4':1, '6':1, '8':2, '9':1}
 sum=0
 if type(n)==str and n[1:].isdigit()==True:
  b=int(n)
  a='%d' %(b)
  for i in a:
   if i in h.keys():
    sum=sum+h[i]
  return sum 
 elif type(n) ==int or type(n)==long:
  a=str(n)
  for i in a:
   if i in h.keys():
    sum=sum+h[i]
  return sum 
 else:
  return 'ERROR'
  
	   
	   
print count_holes('qq') 