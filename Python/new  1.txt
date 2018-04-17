N = None
i = None
R = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


N = float(text_prompt('Enter N'))
if N < 0:
  print('N is invalid')
else:
  i = 0
  R = 1
  for count in range(int(N)):
    i = i + 1
    R = R * i
print(R)