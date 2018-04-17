import sys


def encode_morze(n): 
 t=n.strip()
 m=t.upper()
 coded=[]
 flag=0
 morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--..",
	" " : "__"}
 
 for i in m:
  if i in morse_code.keys():
  
   letter=morse_code[i.upper()]
   flag=1
     
  else:
   letter=""  
  coded.append(letter)
 if flag==0:
  return ""
 cod='__'.join(coded)
 co=cod.replace(".", "^ ")
 c=co.replace("-","^^^ ")
 a=c.strip()
 
 return a.replace(" ", "_")
	   
	   
print encode_morze('In a hole in the ground there lived a hobbit') 