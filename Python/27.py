import sys


def file_search(folder, filename): 

  path = folder[0] + '/'
  if filename in folder:
     return path + filename
  elif filename not in folder:
     path = folder[0] + '/'
     for item in folder:
      if isinstance (item,list):
       res = file_search(item, filename)
       if res != False:
        path = path + str(res)
        return path
  
  return False
	   
	   
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
