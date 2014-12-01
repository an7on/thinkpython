# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 14:25:24 2014

@author: Antonio
"""

# 1.

print '+',
print '- '*4,
print '+',
print '- '*4,
print '+'

print '|',
print ' '*8,
print '|',
print ' '*8,
print '|'

print '|',
print ' '*8,
print '|',
print ' '*8,
print '|'

print '|',
print ' '*8,
print '|',
print ' '*8,
print '|'

print '+',
print '- '*4,
print '+',
print '- '*4,
print '+'

print '|',
print ' '*8,
print '|',
print ' '*8,
print '|'

print '|',
print ' '*8,
print '|',
print ' '*8,
print '|'

print '|',
print ' '*8,
print '|',
print ' '*8,
print '|'

print '+',
print '- '*4,
print '+',
print '- '*4,
print '+'


# 2.
def row1():
    print '+',
    print '- '*4,
    print '+',
    print '- '*4,
    print '+',
    print '- '*4,
    print '+',
    print '- '*4,
    print '+'


def row2():
    print '|',
    print ' '*8,
    print '|',
    print ' '*8,
    print '|',
    print ' '*8,
    print '|',
    print ' '*8,
    print '|'

def draw_grid():
    row1()
    row2()
    row2()
    row2()
    row1()
    row2()
    row2()
    row2()
    row1()
    row2()
    row2()
    row2()
    row1()
    row2()
    row2()
    row2()
    row1()
    
draw_grid()