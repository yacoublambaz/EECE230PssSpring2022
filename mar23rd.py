"""
Recursion 2: Divide and Conquer and Maze Traversal

Revisiting


Example 1: Binary Search, implement binary searching recursively

"""
def binSearch(L,x):
    """
    1. How do I know that I'm in the right place? L[mid] == x
    2. How do I know to look to the left? L[mid] > x
    3. How do I know to look to the right? L[mid] < x
    """
    def binSearchRec(L,x,low,high):
        mid = (low+high) // 2
        if low <= high:
            if L[mid] == x:
                return mid
            elif L[mid] > x:
                return binSearchRec(L,x,low,mid-1)
            else:
                return binSearchRec(L,x,mid+1, high)
        else:
            return -1
    low = 0
    high = len(L)-1
    return binSearchRec(L,x,low,high)



"""
Example 2: Find how many even elements in the list

Given a list L = [1,3,5,1,3,1,1,1,7,2,2,2] return how many even elements
are in the list.

All odd numbers will appear before all even numbers

O(LogN)

1- how do I know that all my list is even?
if the first element is even, then return len(list)
2- how do I know that all my list is odd?
if the last element is odd, return 0
3- how do I know I'm in the right place?
if L[mid] is odd, and L[mid+1] is even
or L[mid] is even and L[mid-1] is odd
4- how do I know to look to the left?
if L[mid] is even and L[mid-1] is even
5- how do I know to look to the right?
if L[mid] is odd and L[mid+1] is odd
"""
def countEven(L):
    def countEvenRec(L,low,high):
        if low <= high:
            mid = (low+high) // 2
            if L[mid] % 2 == 0 and L[mid-1] % 2 != 0:
                print("return here 1")
                return len(L) - mid
            if L[mid] % 2 != 0 and L[mid+1] % 2 == 0:
                print("return here 2")
                return len(L) - mid - 1
            if L[mid] % 2 == 0 and L[mid-1] % 2 == 0:
                return countEvenRec(L,low,mid-1)
            if L[mid] % 2 != 0 and L[mid+1] % 2 != 0:
                return countEvenRec(L,mid+1, high)
        else:
            return -1
    if L[0] % 2 == 0:
        return len(L)
    if L[len(L)-1] % 2 != 0:
        return 0
    low = 0
    high = len(L)-1
    return countEvenRec(L,low,high)

L = [1,3,5,1,3,1,1,1,7,2,2,2]
L = [1,1,1,1,1]
print(countEven(L))
"""
Example 3:
Find contiguous elements of different signs

Given a list L = [-1,-2,-3,-5,-1,2,3,4]

Return the index i were i and i+1 have different signs
"""
def findChange(L):
    def findChangeRec(L,low,high):
        if low <= high:
            mid = (low+high)//2
            if L[mid] > 0 and L[mid-1] < 0:
                return (mid-1,mid)
            if L[mid] < 0 and L[mid+1] > 0:
                return (mid,mid+1)
            if L[mid] > 0 and L[mid-1] > 0:
                return findChangeRec(L,low,mid-1)
            if L[mid] < 0 and L[mid+1] < 0:
                return findChangeRec(L,mid+1, high)
        else:
            return -1
    if L[0] > 0:
        return 0
    if L[len(L)-1] < 0:
        return len(L)-1
    low = 0
    high = len(L)-1
    return findChangeRec(L,low,high)

"""
    if you answer the questions but some test cases still fail
    1. What's special about this case?
    Does it have any extra conditions?

    2. Where do you tackle this condition? In the recursive function
    or the wrapper one?
"""
"""
Example 4: Dictionaries

1) dict = {"one":"uno", "two":"duos", "three":"tres"}

How a dictionary works?
Assume a list L = [0,0,0,"Sup",0,0,0,0,0,0]
assume that you have an element {13:"Sup"}
Let's assume that the hashing algorithm is % 10
13 % 10 = 3

Searching a dictionary is O(1) rather than searching a list
which is O(n)


2) Counting problem

3) Example 1) Similar lists

4) Example 2) two-sum problem
d = {}
#d[key] = value
d["One"] = "Uno" #Adding
d["One"] = "Wahad" #Updating

if "One" in d: #One exists in the dictionary
for elem in d.items():
    key = elem[0]
    value = elem[1]

"""



def counting(s):
    """
    Given a string S, return how many of each letter is in S
    if s = "aaabc" -> {a:3, b:1, c:1}
    """
    d = {} #initialize dictionary
    for letter in s:
        if letter not in d: #is the letter not in the dic yet?
            d[letter] = 1 #If yes, put it with value 1
        else: #Is the letter in the dic?
            d[letter] = d[letter] + 1 #Increment by 1
    return d

print(counting("Hello guys my name is Yacoub here to taech you 230"))




def similar(L1,L2):
    """
    Given two lists L1 and L2, return True if L1 and L2 are similar
    Two lists are similar if they have the same elements
    not necessarily in the same order
    L1 = [1,1,2,3,8,1,2]
    L2 = [2,1,8,2,3,1,4]
    """
    def count(L):
        #returns which elements are in L and how many?
        d = {} #initialize dictionary
        for letter in L:
            if letter not in d: #is the letter not in the dic yet?
                d[letter] = 1 #If yes, put it with value 1
            else: #Is the letter in the dic?
                d[letter] = d[letter] + 1 #Increment by 1
        return d
    countL1 = count(L1)
    countL2 = count(L2)
    return countL1 == countL2


def twoSum(L, x):
    """
    Given a list L and a number x, return two numbers in L
    that add up to x

    if x1 + x2 = t
    in our O(n^2) Solution
    loop over x1 in L
    loop over x2 in L

    a faster way to do this
    search for x1 such that t-x2 = x1

    L = [5,4,7,2,10,3] x = 12
    d = {5:0,4:1}
    """
    d = {}
    for i in range(len(L)):
        if x - L[i] in d: #If it's in the dictionary?
            return (L[i], x - L[i])
        else:
            d[L[i]] = i




"""
Example 5.

Given an m x n grid of characters board and a string word,
return true if word exists in the grid starting at i = 0 and j = 0.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once.

board = [["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]]
word = "ABCCED"
result is True
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word = "CCE" -> False
"""
import copy
def findWord(board,word):
    def findWordRec(board,replica,word,i,j,wordSoFar):
        if word == wordSoFar:
            return True
        if replica[i][j] != False: #If we didn't visit
            replica[i][j] = False
            print(wordSoFar)
            if len(wordSoFar) < len(word):
                wordSoFar = wordSoFar + board[i][j]
                #top
                top = 0
                bottom = 0
                left = 0
                right = 0
                if i != 0:
                    # print("top: ",i-1, " ", j)
                    top = findWordRec(board,replica, word,i-1,j,wordSoFar)
                #bottom
                if i != len(board)-1:
                    # print("bottom: ",i+1," ", j)
                    bottom = findWordRec(board,replica, word,i+1,j,wordSoFar)
                #left
                if j != 0:
                    # print("left: ",i, " ", j-1)
                    left = findWordRec(board,replica, word,i,j-1,wordSoFar)
                #right
                if j != len(board[0])-1:
                    # print("right: ",i, " ", j+1)
                    right = findWordRec(board,replica, word,i,j+1,wordSoFar)
                if top == True or bottom == True or left == True or right == True:
                    return True
        else:
            print()
            # print("Oops already visited")
    replica = copy.deepcopy(board)
    return findWordRec(board,replica,word,0,0,"")

board = [["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]]

word = "ABCE"
print(findWord(board,word))
