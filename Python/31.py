import sys


def find_most_frequent(text):
 
 text = text.lower() 
 res=[]
 numbers = ',.:;!?-...'
 new=text
 for char in numbers:
    
    new = new.replace(char, ' ')  
    
 new=new.strip()
 
 count = {}.fromkeys(new.split(" "))
 
 new=new.split(" ")
 for item in count:
  count[item]=0
 
 
 
 for element in new:
  if element!='':
   count[element]=count[element]+1
  
 count_val=max(count.values())
 

 for i in count:
  if count[i]==count_val and i!='':
   res.append(i)
  
 return res
 
	   
	   
print find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.') 