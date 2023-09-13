#!/usr/bin/env python3

class Person:
    
    #Initialize : creates working copy of Person class with __init__
    #creates instance or object that we can assign attributes to
    #self is reference to the currect instance of the class and is used
    #to access its attributes
    def __init__(self, name):
        self.name = name
