# Python3
# Author: George Hartoularos
# UCSF BMI203 Algoirthms Winter 2018
# Homework 1

import numpy as np
import random

def isinputcool(seq,acount,ccount,inp,lo=None,hi=None):
    '''
    Function checks quality of input for both main functions before
    performing algorithms.

    Example input:
    bubblesort([1,5,2,3,4,8,4],5,3,)
    Example output:
    [1,2,3,4,4,5,8]
    '''
    trivial = False
    acount += 1

    # catch a non-list
    try:
        seq = list(seq)
        acount += 1
    except:
        print('For input: %s\n   Input: not iterable.' % str(inp))
        trivial = True
        acount += 1
        return trivial, None, acount, ccount

    # catch non-finite data
    try:
        ccount += len(seq) # for below, isn't "in" like a bunch of "==" statements?
        if False in np.isfinite(seq):
            print('For input: %s\n   Input: sequence has invalid object' \
            ' type(s).' % str(inp))
            trivial = True
            acount += 1
            return trivial, None, acount, ccount
    except:
        print('For input: %s\n   Input: sequence has invalid object' \
        ' type(s).' % str(inp))
        trivial = True
        acount += 1
        return trivial, None, acount, ccount

    # catch empty data
    ccount += 1
    if len(seq) == 0:
        print('For input: %s\n   Input: sequence is empty, nothing ' \
        'to sort.' % str(inp))
        trivial = True
        acount += 1
        return trivial, None, acount, ccount

    # catch a trivial case
    ccount += 1
    if list(set(seq)) == [seq[0]]: # detect trivial case of equal elements
        trivial = True
        acount += 1
        return trivial, seq, acount, ccount

    return trivial, None, acount, ccount

def bubblesort(seq,returncounts=False):

    """
    Function goes element-by-element through the list, and 
    determines if the element after it is bigger or smaller. If 
    smaller, it defines a new list with the 2 elements in question 
    switched. Will repeat this until the list is no longer out of 
    order. Then one final edge run confirms the list is ordered. 
    Returned list is in increasing order, smallest elements first, 
    biggest elements last.

    Example input:
    bubblesort([1,5,2,3,4,8,4])
    Example output:
    [1,2,3,4,4,5,8]
    """
    acount = 0 # intialize assignemnt counting
    ccount = 0 # intialize conditional counting

    inp = seq # new list obj gets redefined, no need for list comp
    acount += 1

    trivial, val, acount, ccount = isinputcool(seq, acount, ccount, inp)

    # this is in the trivial case that the seq is comprised of a single value
    # As Tamas mentioned in the comments, Python's  short circuiting will make 
    # the ccount inaccurate unless its split up
    ccount += 1 # for first conditional  below
    if trivial == True:
        ccount += 1 #  for second conditional below
        if val != None: 
            print('For input: %s' % str(inp))
            print('   Assignments: %d' % acount)
            print('   Conditionals: %d' % ccount)
            print('   Sequence: %s' % str(seq))
            return val
    else: # trying to count conditionals kinda precludes the use of elif, sad
        ccount += 1
        if trivial == True:
            return

    unordered = 1 # initialize unordered
    acount += 1
    while unordered == 1:
        ccount += 1 # for while above
        unordered = 0 # initialize to ordered, give it a chance!
        acount += 1 # for unordered above
        for i in range(len(seq)):
            prefix = seq[:i] # beginning part of list
            comp0 = [seq[i]] # left element for comparison
            try: # this will error if at end of list
                comp1 = [seq[i+1]] # right element for comparison
                suffix = seq[(i+2):] # end part of list
            except: # you've reached the end of the list, leave the for loop
                break
            ccount += 1 # for if below
            if comp0[0] > comp1[0]: # simple comparison
                unordered = 1 # the list is unordered, cycle through again
                # make new list in modified order:
                seq = np.concatenate((prefix,comp1,comp0,suffix))
                acount += 2
            acount += 5 # 4 for explicit assignemnts + 1 for the implicit "i="
    ccount += 1 # for edge while loop evaluation
    # print('For input: %s' % str(inp))
    # print('   Assignments: %d' % acount)
    # print('   Conditionals: %d' % ccount)
    # print('   Sequence: %s' % str(seq))
    if returncounts:
        return acount, ccount
    else:
        return seq

def quicksort(seq,lo=0,hi='whole',returncounts=False):
    """
    Function takes in a sequence, start and end point to sort the elements of 
    the sequence between and including start and end. Start and end are 
    required for algorithm, but will default to entire sequence if no start 
    and end indices are passed. Initiate 'pivot' at start (first element by 
    default or at the index passed to 'lo') and initiate cursors immediately 
    to right of pivot (i) and at furthest point from pivot (j). Inch the 
    cursors closer to each other until they (1) reach a value greater than (i)
    and less than (j) the pivot, or (2) they hit each other. If (1) switch the
    elements at i and j and continue, or if (2) switch the elements at pivot 
    and collision point and stop. This guarantees that the pivot is now in 
    its sorted position, regardless of the order of the elements below and 
    above it. Then simply recursively apply this to the former and latter
    portions of the sequence (left and right of the pivot) until the sequence
    is of length 1, which is by definition ordered.
    """
    acount = 0 # intialize assignemnt counting
    ccount = 0 # intialize conditional counting

    inp = [i for i in seq] # need list comp for mutable object type 'list'
    acount += 1

    # Pre-processing start
    trivial, val, acount, ccount = isinputcool(seq, acount, ccount, inp)
    acount += 2 # above

    # As Tamas mentioned in the comments, Python's  short circuiting will make 
    # the ccount inaccurate unless its split up
    ccount += 1 # for first conditional  below
    if trivial == True:
        ccount += 1 #  for second conditional below
        if val != None: 
            print('For input: %s' % str(inp))
            print('   Assignments: %d' % acount)
            print('   Conditionals: %d' % ccount)
            print('   Sequence: %s' % str(seq))
            return val
    else:
        ccount += 1 # below
        if trivial == True:
            return

    ccount += 1 # below
    if hi == 'whole': # extract the index of the last element
        hi = len(seq) - 1
        acount += 1 # above
    # Pre-processing end 

    '''
    Need to nest in a larger function so that I can use input data quality checks,
    else checks will be run on every recursive call to function.
    '''
    def quicksorter(seq,lo,hi,acount,ccount): 
        '''
        Define the partition function that will place the pivot in the correct
        position and *partition* the function into two smaller sequences
        '''
        def partition(seq,lo,hi,acount,ccount):
            pivot = seq[lo] # define pivot
            i = lo + 1 # left cursor
            j = hi # right cursor
            while True: # do until break when j < i (collision)
                while i <= j and seq[i] <= pivot:
                    ccount += 2 # for above conditionals
                    acount += 1 # for below assignment
                    i += 1 # inch up
                while seq[j] >= pivot and j >= i:
                    ccount += 2 # for above conditionals
                    acount += 1 # for below assignment
                    j -= 1 # inch down
                if j < i:
                    break
                else: # store temporary variable k to swtich elements efficiently
                    k = seq[i]
                    seq[i] = seq[j] # do the switch
                    seq[j] = k
                    acount += 3
                ccount += 3 # for final edge case of while loops above
            k = seq[lo] # same storing for k above to swtich
            seq[lo] = seq[j]
            seq[j] = k
            acount += 6 # for assingments outside while True loop
            ccount += 1 # for while True loop
            return j, acount, ccount # j becomes the cusp of the new sequences
        if lo < hi: # stop recursion
            acount += 1 # for assignment below
            pivot, acount, ccount = partition(seq,lo,hi,acount,ccount)
            quicksorter(seq,lo,pivot-1,acount,ccount) #recursive calls of subsequence
            quicksorter(seq,pivot+1,hi,acount,ccount)
        ccount += 1 # for above conditional
        return seq, acount, ccount
    seq, acount, ccount = quicksorter(seq,lo,hi,acount,ccount) # gotta return something
    if returncounts:
        return acount, ccount
    else:
        return seq



