import sys


def convert_n_to_m(x, n, m):
 import math
 if type(x)!=int and type(x)!=long and type(x)!=str:
  return False
 numbers="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
 num=str(x).upper()
 decimal=0.0
 k=0
 for letter in num[::-1]:
  if letter not in numbers[:n]:
     return False
  decimal=float(numbers.find(letter))*float(math.pow(n,k))+decimal
  k=k+1
 decimal=int(decimal)
 if m==1:
  return "0"*decimal
 convert = ""
 result=decimal
 while result>=1:
  ost=result%m
  result = result//m
  print "result", result
  
  print "osr", ost
  convert=numbers[ost]+convert
  print "convert", convert
 print decimal
 hexy= hex(decimal)
 
 print 'hex' , hexy
 return convert
   
	  
print  convert_n_to_m(123123123123123123123, 11, 16)

# 812358264557662749611 my
# 812358264557662765056 when float
# 812358264557662687802 correct ()73850751323423880709