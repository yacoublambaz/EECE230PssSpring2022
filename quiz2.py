"""
problem 1)
"""

def funAndEasy(n):
    fileName = "funEasy" + str(n) + ".txt"
    fhandle = open(fileName,"w")
    for i in range(n):
        fhandle.write("EECE 230 is Fun and Easy!\n")
    fhandle.close()

"""
Problem 2
"""
def checkList(L):
    """
    1. Sort the list
    2. Loop over the element
    3. Use binary searching to find the double
    """
    def binarySearch(L,x,low,high):
        if low <= high:
            mid = (low+high)//2
            if L[mid] == x: 
                return True
            elif L[mid] > x:
                return binarySearch(L,x,low,mid-1)
            else:
                return binarySearch(L,x,mid+1,high)
        else:
            return False
    L.sort()
    for i in range(len(L)):
        elem = L[i]
        if binarySearch(L,2*elem,i,len(L)-1):
            return True
    return False

"""
Problem 3
"""
def indexOfMisplacedZero(L):
    def rec(L,low,high):
        if low <= high:
            mid = (low+high)//2
            #1. how do I know I'm in the right place?
            if L[mid] == 0:
                return mid
            #How to know to look to the right?
            elif L[mid] != mid:
                return rec(L,mid+1,high)
            else:
                return rec(L,low,mid-1)
        return -1
    return rec(L,0,len(L)-1)

"""
Problem 4.a slow (no memoization)
"""
def numOfDecompositions(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        return numOfDecompositions(n-1) + numOfDecompositions(n-3)

def numOfDecompositionsFast(n):
    #with memoization
    def mem(n,L):
        if n >=0:
            if L[n] != -1:
                return L[n]
            if n == 0:
                return 1
            else:
                L[n] = mem(n-1,L) + mem(n-3,L)
            return L[n]
        else:
            return 0
    L = [-1 for i in range(n+1)]
    return mem(n,L)

def numOfDecompositionsB(n,m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        branch1 = numOfDecompositionsB(n-1,m)
        branch2 = 0
        if m != 0:
            branch2 = numOfDecompositionsB(n-3,m-1)
        return branch1 + branch2

        

