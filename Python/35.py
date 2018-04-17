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
  k=0
  minimum=min(matrix[i])
  for j in range(len(matrix[i])):
   if matrix[i][j]==minimum and k<=1:
    xy=(i,j)
    k=k+1
    list_min.append(minimum)
    list_xy.append(xy)
  
 print list_min
 print  list_xy
 
 for l in range (len(list_xy)):
  k=0
  maximum=matrix[list_xy[l][0]][list_xy[l][1]]
  point = list_xy[l]
  for j in range(len(matrix[i])):
   if maximum >= matrix[j][list_xy[l][1]] and k<=1:
    k=k+1
    if j== len(matrix[i])-1:
	  return point
   
 return False
    
 
  
    
  
print ([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]) 