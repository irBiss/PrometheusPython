import sys


def file_search(folder, filename):
 
 for item in folder:
  if type(item) != list:
   path=''
   if str(folder).find(filename)==-1 and folder[str(folder).find(filename)]!=filename:
    path="False"
    print folder[str(folder).find(filename)]
   else:
    for i in range (len(folder)):
	  path=path+str(folder[i])+'/'
    print path
  else:
   file_search(item, filename)
    

  

 return path
  
  
  
print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
