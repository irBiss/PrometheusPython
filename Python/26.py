import sys


def file_search(folder, filename):
 
 for item in folder:
  if type(item) == list:
   file_search(item, filename)
 
 for item in folder:
  if item != filename:
   path = "false"
  else:
   path=""
 
 if path =="":
  for item in folder:
   path=path+"/"+item
    

  
 
 return path
  
  
  
print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')