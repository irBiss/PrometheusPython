

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

 
 
 
for i in range(26):
 z=''
 n=i
 m=i+5
 for j in range(n,m):
  z=z+key[j]
  j=j+1
 print alphabet[i],
 print z
 i=i+1
  
 





 


