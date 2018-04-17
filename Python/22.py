import sys
x=sys.argv[1]
x=sys.argv[1]

def counter(x, y):
 
 li=list_to_clean
 new_list=[]
 
 l=len(list_to_clean)
 for i in range(l):
     
  for j in range(l) :
   
   
   if list_to_clean[j]!=li[i] and li[i] not in new_list:
    
    new_list.append(li[i])
  if len(new_list)==0:
   new_list.append(list_to_clean[0])
    
 return list(new_list)
  
  
  
print clean_list(x)