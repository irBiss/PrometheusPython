import sys


def convert_n_to_m(x, n, m):
 
 if type(x)!=int and type(x)!=long and type(x)!=str:
  return False
 numbers="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
 num=str(x).upper()
 decimal=0
 k=0
 for letter in num[::-1]:
  if letter not in numbers[:n]:
     return False
  decimal=numbers.find(letter)*(n**k)+decimal
  k=k+1
 if decimal == 0:
  return "0"
 if m==1:
  return "0"*decimal
 convert = ""
 result=decimal
 while result>=1:
  ost=result%m
  result = result//m
  
  convert=numbers[ost]+convert
  
 return convert
   
	  
print  convert_n_to_m('000ZZZZ', 36, 13)
