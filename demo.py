"""
Applications--->login, billing, profile management

variables, loops/control statements, objects of user defined classes, functions
             package(library)
|                                  |
module(login)                 module(billing)
|
class ..........class2
|
properties&methods


"""

VERSION=1.0

def display():
    print("Welcome to my library!")


class Operations:

    def __init__(self):
        pass


    def sqrt(self, val):
        return val**(1/2)

    def factorial(self, n):
        if n==0 or n==1:
            return 1
        else:
             return n*self.factorial(n-1)



