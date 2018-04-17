year = int(raw_input('input year:'))
print (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0))

example_list = ['one', 1, 2.0, True, [0.1, 0.2, 0.3]]
print example_list[-1]
print example_list[1:4]
print example_list[-2:5]
print example_list[4:1]
print example_list[:-1]
print example_list[-2:]
print example_list[::2]
print example_list[:4:3]
print example_list[1::-1]
print example_list[3:0:-1]

x = [1, 2, 3]
x.reverse()
print x #
print x