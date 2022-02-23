"""


1- Two sum problem
Given a list and a number, find two numbers in the list that add up to this number

2- Two pointers approach

3- Binary search

4- Sliding windows problem

MSSP -> 1) Three for loops -> O(N^3)
        2) Two for loops and slicing -> O(N^3) -> uses the sum()
        3) Two for loops but smarter -> O(N^2)

Problem:
Find the maximum length of continuous 1's in a list

L = [0,0,1,1,1,1,0,1,1,1,0,0,0,1,1], 4 1s
0) I start i and j at 0,0
1- Increment i and j until we see a 1
2- When we see a 1, increment j lahalha
3- stop incrementing j when we see a 0, at this point increment both i and j at the same time
until repeat step 2

"""
def countOne(L):
    maxCount = 0
    i, j = 1,1
    currCount = 0
    while i < len(L):
        #increment i and j until we see the first 1
        if L[i] == 1:
            break
        i = i + 1
        j = j + 1

    while i < len(L) and j < len(L):
        if L[j] == 1:
            currCount = currCount + 1
            j = j + 1
        elif L[j] == 0 and L[j-1] == 1:
            i = j
            maxCount = max(currCount, maxCount)
            currCount = 0
            i = i + 1
            j = j + 1
        else:
            i = i + 1
            j = j + 1
    return maxCount
#print(countOne([0,0,1,1,1,1,0,1,1,1,0,0,0,1,1]))
# inp1 = int(input("Please enter first var: "))
# inp2 = int(input("Please enter second var: "))
# inp3 = int(input("Please enter third var: "))
#
# if inp1 < inp2 and inp2 < inp3:
#     print("yes consecutive")
# else:
#     print("not consecutive")

#Problem 2.1
# n = int(input("Please enter the upper bound: "))
# ans = 0
# for i in range(1,n+1):
#     curr = 1 / (i**(2))
#     ans += curr
# print(ans)

#Problem 2.2
# from math import pi
#
# err = float(input("Please enter the error: "))
# def trunc(n):
#     ans = 0
#     for i in range(1,n+1):
#         curr = 1 / (i**(2))
#         ans += curr
#     return ans
# i = 1
# while True:
#     if (((pi**2) / 6) - trunc(i)) < err:
#         print(i)
#         break
#     else:
#         i = i+1


# def lengthLCSS(s1,s2):
#     slower implmentation, no sliding windows
#     # 1. variable to indicate starting point: i
#     # 2. variable to indicate endpoint: j
#     # 3. We want to snip s1[i:j]
#     # 4. if s1[i:j] in s2: we need to see its length, and update accordingly
#     maxLen = 0
#     for i in range(len(s1)): #1. variable to indicate starting point: i
#         for j in range(i,len(s1)): # 2. variable to indicate endpoint: j
#             subS = s1[i:j+1] # 3. We want to snip s1[i:j] our substring
#             if subS in s2: # 4. if s1[i:j] in s2: we need to see its length, and update accordingly
#                 maxLen = max(maxLen, len(subS))
#     return maxLen

def lengthLCSS(s1,s2):
    def slide(s2, subS, lenW):
        k = 0 #the start of my current window at s2
        while k <= len(s2) - lenW:
            if s2[k:k+lenW] == subS:
                return True
            else:
                k = k + 1
        return False
    #with sliding windows
    maxLen = 0
    for i in range(len(s1)):
        for j in range(i,len(s1)):
            subS = s1[i:j+1]
            lenW = len(subS) #length of my window

            if slide(s2,subS,lenW) == True:
                maxLen = max(maxLen, lenW)
    return maxLen



def consecutive(L):
    assert type(L) == list, "L must be list"
    for num in L:
        assert type(num) == int, "nums must be integers"
    for i in range(1,len(L)):
        if L[i-1] + 1 != L[i]:
            return False
    return True



def minSliceCut(L):

    """
    Steps:
    1- start i and j at 0
    2- increment i and j until we see two non-censective elements
    3- when you do, increment j until you see that L[i] and L[j] are consecutive
    4- the window is in between
    5- what if j goes out of bounds? return L[i:]
    6- what if i does not start as consecutive, while loop until we do find two consecutive elements
    and slice up until those
    """
    i = 0
    j = 0
    minlen = len(L)
    minslice = []
    while i < len(L)-1 and j < len(L):
        if L[i] == L[i+1]-1:
            i = i+1
            j = j+1
        else:
            j = j + 1
            everythingElse = L[:i] + L[j:]
            if consecutive(everythingElse):
                if len(L) - len(everythingElse) < minlen: #if the length of the thing to be sliced is less
                    minlen = len(L) - len(everythingElse)
                    minslice = L[i:j]
    return minslice
print(minSliceCut([5,6,7,8,9,10]))
print(minSliceCut([1,2,5,2,3]))
print(minSliceCut([5,6,7,8,1,5,8,9,10]))
print(minSliceCut([5,6,7,1,0,1,0,9,10]))
print(minSliceCut([7,1,0,1,0,9,10]))
print(minSliceCut([3,2,1]))
