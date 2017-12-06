from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}


    def add_module(self,title):
        module_title  = title.title
        self.modules.append(module_title)
        key = title.title
        value = title.get_grade()
        self.grades[key] = value

    def get_list_modules(self):
        for x in self.modules:
            print(x)

    def get_grades(self):
        for x in self.grades:
            print("%s: %s" %(x, self.grades[x]))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
