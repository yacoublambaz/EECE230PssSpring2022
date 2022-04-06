"""import matplotlib.pyplot as py

plt.plot([-1,1],[-1,1])
plt.plot([-1,1],[0,0])
plt.plot([0,0],[-1,1])
plt.plot([-1,-1],[1,-1])

plt.show()"""


def reverseIter(L):
    i = 0
    j = len(L)-1
    while i<=j:
        L[i],L[j] = L[j],L[i] #swaps them
        i = i+1
        j = j-1

def reverseList(L):
    def rec(L,i,j):
        if i <=j:
            L[i],L[j] = L[j],L[i] #swaps
            rec(L,i+1,j-1)
    rec(L,0,len(L)-1)

def areDisjoint(L):
    #Sort the tuples in L depending on the start time
    L.sort(key = lambda I:I[0])
    #[(1, 1.9), (2, 5), (11, 25), (100, 150)]
    for i in range(len(L)-1):
        if L[i][1] >= L[i+1][0]: #end time of prev
        #is bigger than the start time of next
            return False
    return True

def maximalIntervals(L):
    #T1(1,5), T2(2,3)
    #T1 overlaps T2 if T2[1] < T1[1]
    L.sort(key = lambda I:I[0])
    if len(L)==0:
        return []
    ans = [L[0]]
    for i in range(len(L)-1):
        t1 = L[i]
        t2 = L[i+1]
        if t1[1] < t2[1]:
            ans.append(t2)
    return ans

def readFileAndPlot(fileName):
    fhandle = open(fileName, 'r')
    counter = 0
    for line in fhandle:
        line = line.strip() # 123 -> 123 (no spaces)
        if counter == 0:
            plt.title(line)
        if counter == 2:
            xAxis = line.split()
        if counter == 4:
            yAxis1 = line.split()
        if counter == 6:
            yAxis2 = line.split()
    plt.plot(xAxis, yAxis1)
    plt.plot(xAxis, yAxis2)

def findClosest(L,x):
    def rec(L,x,low,high):
        if low<=high:
            mid= (low+high)//2
            #1. How do I know I'm in the right place?
            if L[mid] == x:
                return L[mid]
            if L[mid]<x and L[mid+1] > x:
                if x-L[mid] > L[mid+1] - x:
                    return L[mid+1]
                else:
                    return L[mid]
            if L[mid-1] < x and L[mid] > x:
                if x - L[mid-1] > L[mid] - x:
                    return L[mid]
                else:
                    return L[mid-1]
            #2. How do I know to look to the left?
            if L[mid] > x and L[mid-1] > x:
                return rec(L,x,low,mid-1)
            #3. How do I know to look to the right?
            else:
                return rec(L,x,mid+1,high)
    if x < L[0]:
        return L[0]
    if x > L[len(L)-1]:
        return L[len(L)-1]
    low = 0
    high = len(L)-1
    return rec(L,x,low,high)

def minimumDistanceL(A,B):
    A.sort()
    B.sort()
    minD = 100 #arbitrary number
    for elem in A:
        closestElem = findClosest(B,elem)
        distance = abs(elem-closestElem)
        minD = min(minD,distance)
    return minD

"""
0: nothing
1: left
2: right
3: both
1:0
2:0
3:0
0:1
0:2
0:3
____
1:1
2:1
3:1
1:2
2:2
3:2
1:3
2:3
3:3
h2 = h1*h1 + h1*h0*2
"""

def numberOfBalancedBinTrees(h):
    if h == 0:
        return 1
    if h == 1:
        return 3
    else:
        firstHalf = numberOfBalancedBinTrees(h-1)*numberOfBalancedBinTrees(h-1)
        secondHalf = 2*numberOfBalancedBinTrees(h-1) * numberOfBalancedBinTrees(h-2)
        return firstHalf + secondHalf

def numMem(h):
    def num(h,L):
        #1. Is this a problem that I solved before?
        if L[h] != -1:
            return L[h]
        #2. Is this a base case?
        if h == 0:
            return 1
        if h == 1:
            return 3
        #3. Else, solve it and store it for me
        L[h] = num(h-1,L)*num(h-1,L) + 2*num(h-2,L)*num(h-1,L)
        return L[h]
    L = [-1 for i in range(h+1)]
    return num(h,L)

def numberOfDistinct(L):
    L.sort()
    counter = 1
    if len(L) == 0:
        return 0
    for i in range(1,len(L)):
        if L[i] != L[i-1]:
            counter = counter + 1
    return counter

def sortUnimodalList(L):
    #1. Find the index of mode
    #2. let i be 0 and j be len(L)-1
    #3. compare L[i] with L[j], add smaller to the answer
    #4. finally, I'm gonna have a list sorted
    indexOfMode = 0
    if len(L) <= 1:
        return
    for i in range(1,len(L)-1):
        if L[i] > L[i+1] and L[i] > L[i-1]:
            indexOfMode = i
            break
    if L[0] > L[1]: #first element is mode
        indexOfMode = 0
    if L[len(L)-1] > L[len(L)-2]:
        indexOfMode = len(L)-1
    i = 0
    j = len(L)-1
    ans = []
    while i < indexOfMode and j > indexOfMode:
        if L[i] < L[j]:
            ans.append(L[i])
            i = i+1
        else:
            ans.append(L[j])
            j = j - 1
    while i < indexOfMode:
        ans.append(L[i])
        i = i+1
    while j > indexOfMode:
        ans.append(L[j])
        j = j -1
    ans.append(L[indexOfMode])
    for i in range(len(L)):
        L[i] = ans[i]
