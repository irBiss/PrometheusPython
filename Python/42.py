import sys 


class Student(object):
 def __init__ (self, name, conf):
  self.name=name
  self.conf=conf
  self.labs = [0 for x in range(self.lab_num)]
 def make_lab (self, m, n=0):
  self.labs[n] = m
  
conf = {
 'exam_max': 30,
 'lab_max': 7,
 'lab_num': 10,
 'k': 0.61,
}
oleg = Student('Oleg', conf)

print oleg.conf
