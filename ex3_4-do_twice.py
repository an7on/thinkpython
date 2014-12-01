# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 14:07:57 2014

@author: Antonio
"""

# 1.
def do_twice(f):
    f()
    f()
    
def print_spam():
    print 'spam'
    
#do_twice(print_spam)



# 2.
def do_twice(f, v):
    f(v)
    f(v)
    
def print_something(s):
    print s

do_twice(print_something, 'antonio')



# 3.
def print_twice(s):
    print s
    print s

print_twice('spam')



# 4.  
def do_twice(f, v):
    f(v)
    f(v)

def print_twice(s):
    print s
    print s

do_twice(print_twice, 'spam')


# 5.
def do_four(f, v):
    f(v)
    f(v)
    
def print_twice(s):
    print s
    print s
    
do_four(print_twice, 'spam')