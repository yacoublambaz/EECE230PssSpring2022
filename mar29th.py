import matplotlib.pyplot as plt
"""

Problem 1: plotting
for i in range(1,6):
    for j in range(1,6):
        plt.plot([1,5],[i,j])
plt.show()
"""

def generateList(n):
    if n == 0:
        return []
    L = generateList(n-1)
    return L + [n] + L


def findIndexOfAZero(L):
    """
    1- How do I know I'm in the right place? if L[mid] == 0
    2- How do I know to look to the left?
    3- How do I know to look to the right?
    If L[mid] is positive and L[low] is also positive, then look to the right
    """
    def rec(L,low,high):
        mid = (low+high) // 2
        if L[mid] == 0:
            return mid
        if (L[mid] > 0 and L[low] > 0) or (L[mid] < 0 and L[low] < 0):
            return rec(L,mid+1,high)
        else:
            return rec(L,low,mid-1)

    return rec(L,0,len(L)-1)

def maxLenOfLShape(M):
    def traverse(M,i,j,isRight):
        #isRight indicates if this branch walks right or no.
        #If the branch walks right, you shouldn't go down after.
        rows = len(M)
        cols = len(M[0])
        #If the branch violates any of the conditions:
        #1. If M[i][j] is not a zero
        #2. If i is out of bounds
        #3. If j is out of bounds
        #return 0 signalling the end of this branch
        if i >= rows or j >= cols or M[i][j] == 0:
            return 0
        down = 0 #to eliminate Variable Not Defined errors
        if not isRight: #If this branch is not a right branch
            down = traverse(M,i+1,j, False) #traverse downwards
        right = traverse(M,i,j+1,True) #traverse rightwards anyway whenever possible
        return 1 + max(down,right)

    currMax = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            #what if we had multiple L's, I need the longer one
            if M[i][j] == 1:
                trav = traverse(M,i,j, False)
                currMax = max(currMax,  trav)
    return currMax

def maxLenOfLShapeDynamicProgramming(L):
    """
    The idea of Dynamic Programming is to find relationships between elements
    In our case, L[i][j] is going to be L[i+1][j] + L[i][j+1]. How can we construct?
    1. Create a 2x2 matrix for going down.
    2. Create a 2x2 matrix for going right.
    3. Populate the matrix in step 1 with the elements in the first row
    4. Populate the matrix in step 2 with elements in the last column
    5. Now, for upMatrix, for each i and j, upMatrix[i][j] = upMatrix[i-1][j] + 1 if M[i][j] == 1
    6. And, for rightMatrix, for each i and J, rightMatrix[i][j] = rightMatrix[i][j+1] + 1 if M[i][j] == 1
    7. Now we have for each M[i][j], the length of how many rights from here, and how many ups from here.
    8. So, for each M[i][j], the length becomes upMatrix[i][j] + rightMatrix[i][j] - 1 (to avoid repitition)
    Finally, locate the biggest M[i][j] and you got the solution!
    """
    n = len(M)

    up = [[0 for i in range(n)] for j in range(n)]
    for j in range(n):
        up[0][j]=M[0][j]
    for i in range(1,n):
        for j in range(n):
            if M[i][j]:
                up[i][j] = up[i-1][j]+1

    right = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        right[i][n-1] = M[i][n-1]
    for i in range(n):
        for j in range(n-2,-1,-1):
            if M[i][j]:
                right[i][j] = right[i][j+1]+1

    maxLen = 0
    for i in range(n):
        for j in range(n):
            if M[i][j]==1:
                currentLen = up[i][j]+right[i][j]-1
                if currentLen > maxLen:
                    maxLen = currentLen
    return maxLen

def plotUnitCircle():
    import matplotlib.pyplot as plt

    def posfn(x):
        return (1-x**(2)) ** (1/2)
    def negfn(x):
        return -1 * (1-x**(2)) ** (1/2)
    iLst = []
    iLstAnsPos = []
    iLstAnsNeg = []
    for i in range(-100,110,10):
        i = i / 100
        iLst.append(i)
        iLstAnsPos.append(posfn(i))
    for i in range(-100,110,10):
        i = i / 100
        iLstAnsNeg.append(negfn(i))
    plt.plot(iLst,iLstAnsPos, 'g')
    plt.plot(iLst,iLstAnsNeg, 'g')

def checkFrequenciesA(L):
    #return True if each element is repeated exactly 3 times
    for i in range(len(L)):
        count = 0
        for j in range(len(L)):
            if L[i] == L[j]:
                count = count + 1
        if count != 3:
            return False
    return True

import copy
def checkFrequenciesB(L):
    L2 = copy.deepcopy(L)
    L2.sort()
    # print(L2)
    for i in range(0,len(L2)-3,3):
        if L2[i] == L2[i+2] and L2[i] == L2[i+3]:
            return False #repeated at least 4 times
        if L2[i] != L2[i+2]:
            return False #repeated less than 3 times
    return True
