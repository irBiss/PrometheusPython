
import sys

x=str(sys.argv[1]).replace(' ','')

l=len(x)
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz' 

decode=''
codeab=''

newtext=''
for letter in x: 
 y=alphabet.find(letter)
 text=''
 if y!=-1:
  text=text+'a'
 else:
  text=text+'b'
 newtext=newtext+text

l=len(newtext)



for i in range (0,l,5):
 codeab=newtext[i:i+5]
 
 if len(codeab)== 5:
  
  decode = decode+alphabet[key.find (codeab)]
  
print decode   


