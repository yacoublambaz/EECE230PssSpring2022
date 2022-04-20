"""

Recursion 3

Revisiting Maze Traversal + Enumeration's nicer brother, backtracking

"""
import copy
def pathSum(maze,targetSum):
     """
     Write a code that given a maze, check if the sum of the numbers
     in ANY path starting at 0,0 add up to the targetSum
     Example: maze = [[1,2,10,5,2],[3,5,4,2,1],[-2,-9,-10,2]]
     targetSum = 0
     """
     def dfs(maze, isVisited, targetSum, sumSoFar, i, j):
        if i < 0 or j < 0 or i >= len(maze) or j>=len(maze[0]):
             #This is not valid. Get out!
            return
        if isVisited[i][j] == False:
            return
        isVisited[i][j] = False
        sumSoFar = sumSoFar + maze[i][j]
        if sumSoFar == targetSum:
            return True
        if sumSoFar > targetSum:
            return False
        isVisited = copy.deepcopy(isVisited)
        up = dfs(maze,isVisited, targetSum, sumSoFar, i-1,j)
        down = dfs(maze,isVisited, targetSum, sumSoFar, i+1,j)
        right = dfs(maze,isVisited, targetSum, sumSoFar, i,j+1)
        left = dfs(maze,isVisited, targetSum, sumSoFar, i,j-1)
        return up or down or left or right

     isVisited = copy.deepcopy(maze)
     return dfs(maze,isVisited, targetSum,0,0,0)

maze = [[1,2,10],
        [3,5,4],
        [-2,-9,-10]]

"""
Generate All Binary Strings of Length N:
from your slides
n = 0 -> [""]
n = 1 -> ['0','1']
n = 2 -> ['00','01','10','11']
"""

def genBinStr(n):
    if n == 0:
        return ['']
    Y = genBinStr(n-1)
    ans = []
    for elem in Y:
        ans.append(elem + '0')
        ans.append(elem + '1')
    return ans


"""
Generate a list of all valid paranthesis with n open and n closed paranthesis
n = 0 -> ['']
n = 1 -> ['()']
n = 2 -> ['()()', '(())']
"""

def allPara(n):
    #solution from dr. bazzi, this is the most efficient
    #it's absolutely insane. We will use backtracking to solve the problem
    if n == 0:
        return ['']
    ans = []
    for k in range(n):
        X = allPara(k)
        Y = allPara(n-1-k)
        for x in X:
            for y in Y:
                ans.append('(' + x + ')' + y)
    return ans

def allPara(n):
    def isValid(st):
        open = 0
        closed = 0
        for char in st:
            if char == '(':
                open+= 1
            if char == ')':
                closed+=1
            if closed > open:
                return False
        return open == closed
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    Y = allPara(n-1)
    ans = []
    for elem in Y:
        for i in range(len(elem)):
            curr = elem[:i] + '()' + elem[i:]
            if isValid(curr):
                if curr not in ans:
                    ans.append(curr)
    return ans

"""
Given n, return all the non-decreasing lists of length n with
values ranging from 1 to n inclusive
Meaning, if n == 1, return [[1]]
If n == 2, return [[1,1], [1,2], [2,2]]
If n == 3, return [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3], [1, 3, 3], [2, 2, 2], [2, 2, 3], [2, 3, 3], [3, 3, 3]]

n,k
n being the max number
k being the length of the list
n == 3 and k == 0: [[]]
n == 3 and k == 1: [[1],[2],[3]]
n == 3 and k == 2: [[1,1],[1,2],[1,3],[2,2][2,3][3,3]]
If n == 3 and k == 3 return [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3], [1, 3, 3], [2, 2, 2], [2, 2, 3], [2, 3, 3], [3, 3, 3]]
"""
def allLst(n):
    def backtrack(n,k):
        if k == 0:
            return [[]]
        if k == 1:
            return [[i] for i in range(1,n+1)]
        Y = backtrack(n,k-1)
        ans = []
        for elem in Y:
            #elem is a list [1,1]
            lastDigit = elem[len(elem)-1]
            for i in range(lastDigit,n+1):
                ans.append(elem + [i])
        return ans
    return backtrack(n,n)
    
"""
Write a function genStr(n), which given n,
returns a list of all length n strings that have abc in them,
but in a way that no two letters are repeated consecutively.
For example, abca is allowed but aabc is not allowed.
genStr(0) returns [‘’]
genStr(1) returns [‘a’,’b’,’c’]
genStr(2) returns [’ab’, ’ac’, ’ba’, ’bc’, ’ca’, ’cb’]
genStr(3) returns [’aba’, ’abc’, ’aca’, ’acb’, ’bab’, ’bac’, ’bca’, ’bcb’, ’cab’, ’cac’, ’cba’, ’cbc’]

"""
def genStr(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['a','b','c']
    Y = genStr(n-1)
    ans = []
    for elem in Y:
        for char in ['a','b','c']:
            if elem[len(elem)-1] != char:
                ans.append(elem + char)
    return ans


"""
Generate all permutations of a list
L = ["A","B","C"]
gives
["B","C"] "A"
["C","B"] "A" "B"

"""
#bazzi's solution
# def genPerms(L):
#     n = len(L)
#     if n == 0:
#         return [[]]
#     X = genPerms(L[1:])
#     Y = []
#     for P in X:
#         for i in range(n):
#             Y.append(P[:i] + [L[0]] + P[i:])
#     return Y

"""
Generate all permutations of a list
L = ["A","B","C"]
gives
["B","C"] "A"
[["C","B","A"]] "A" "B"
"""
def genPerms(L):
    if len(L) == 1:
        return [L[:]]
    result = []
    for i in range(len(L)): #need to do it n times
        x = L.pop(0)
        perms = genPerms(L)
        for i in range(len(perms)):
            perm = perms[i]
            perm.append(x)
            perms[i] = perm
        result = result + perms
        L.append(x)
    return result



def visitIsland(map):
    def dfs(map,i,j):
        if i < 0 or j < 0 or i >= len(map) or j >= len(map[0]):
            #out of bounds
            return 
        if map[i][j] == '2' or map[i][j] == '0':
            #visited
            return
        #mark as visited
        map[i][j] = '2'
        up = dfs(map,i-1,j)
        bot = dfs(map,i+1,j)
        left = dfs(map,i,j-1)
        right = dfs(map,i,j+1)
    numIslands = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '1':
                numIslands+=1
                dfs(map,i,j)
    return numIslands

map = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","1"],
  ["0","0","0","1","0"]
] 
      

        
        
