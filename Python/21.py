import sys
x=list(sys.argv[1:])
del x[2]
print x
def clean_list(list_to_clean):
 
    
    for j in range(len(list_to_clean)):
	 
     print list_to_clean
     if list_to_clean[0]==list_to_clean[3]:
	   del list_to_clean[3]
  
     
  
    print list_to_clean
    return list_to_clean
  
print clean_list(x)