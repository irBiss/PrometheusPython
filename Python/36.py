import sys


def saddle_point(matrix):
 if len(matrix)==1:
  return (0,0)
 x=0
 y=0
 
 num=0
 xy=()
 list_min=[]
 list_xy=[]
 
 flag=False
 for i in range(len(matrix)):
  
  minimum=min(matrix[i])
  
  for j in range(len(matrix[i])):
   if matrix[i][j]==minimum and matrix[i].count(minimum)==1 :
    xy=(i,j)
    
    list_min.append(minimum)
    list_xy.append(xy)
 for l in range (len(list_xy)):
  max_list=[]
  for i in range (len(matrix)):
   
   max_list.append(matrix[i][list_xy[l][1]])
  if max(max_list)==matrix[list_xy[l][0]][list_xy[l][1]] and max_list.count(max(max_list))==1:
   print list_xy[l]
   print matrix[list_xy[l][0]]
   print max_list.count(max(max_list))
 
 print "list_min", list_min
 print "List_xy" ,list_xy
 print "max_list", max_list
 return False
 
  
	   
	  
print saddle_point([[5,5,5], [5,5,6], [5,4,5]])