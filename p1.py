#!/usr/bin/python

# Problem 1 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Start:        July 16, 2014
# Completed:    July 16, 2014
#
# Notes:        Iterative approach

def sumThreeFive(bound):
    sum = 0
    for x in xrange(1,bound):
        if x % 3 == 0:
            sum = sum + x
        elif x % 5 == 0:
            sum = sum + x
    return sum

numberIn = input('Set the upper-bound range: ')

print 'Total Sum: %s' % sumThreeFive(numberIn)
