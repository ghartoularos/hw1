from algs import bubblesort, quicksort

def testing():
    # generate random integers, repeats
    x1 = [4,2,5,3,4]
    y1 = [2,3,4,4,5]

    # negatives
    x2 = [-4,10,23,-2,6]
    y2 = [-4,-2,6,10,23]

    # decimals, repeats
    x3 = [-4.2,10.7,10.3,9.9,9.9]
    y3 = [-4.2,9.9,9.9,10.3,10.7]

    for i, j in ((x1,y1),(x2,y2),(x3,y3)):
        assert list(bubblesort(i)) == j
    for i, j in ((x1,y1),(x2,y2),(x3,y3)):
        assert list(quicksort(i)) == j
