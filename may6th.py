def numberOfDistinct(L):
    D = {}
    count = 0
    for elem in L:
        if elem not in D:
            count+=1
            D[elem] = 1 #value is not important
    return count

# print(numberOfDistinct([5,1,1,0,5,-3,0]))
# print(numberOfDistinct([8,0,33,9,10]))
# print(numberOfDistinct([0.3, 0.1, 0.3, -7.2]))
# print(numberOfDistinct([2,2,2,2,2]))
# print(numberOfDistinct([]))

class NetUser:
    def __init__(self,name,email):
        assert type(name) == str, "bad input!"
        assert type(email) == str, "bad input!"
        self.name = name
        self.email = email
        self.movies = {}
    def addMovie(self,title):
        assert type(title) == str
        self.movies[title] = 0
    def rateMovie(self,title,score):
        assert title in self.movies
        assert type(score) == int
        assert score > 0
        self.movies[title] = score
    def commonMovies(self,other):
        assert type(other) == NetUser
        ans = []
        for key in self.movies.keys():
            for key2 in other.movies.keys():
                if key == key2:
                    ans.append(key)
        return ans
    def __str__(self):
        ans = ""
        ans += "Name: " + self.name + "\n"
        ans += "Email: " + self.email + "\n"
        ans += "Number of movies in dictionary: " + str(len(self.movies)) + "\n"
        ans += "It’s movie time because EECE 230 (which is fun and easy) is over!"
        return ans

# IB=NetUser("IbnBalluta The Explorer","ite@sydney.ude.au")
# IB.addMovie("The Mask of Zorro")
# IB.rateMovie("The Mask of Zorro",10)
# IB.addMovie("The 100 year-old man who climbed out of the window and disappeared")
# IB.rateMovie("The 100 year-old man who climbed out of the window and disappeared",9)
# IB.addMovie("The Matrix")
# IB.addMovie("Amelie")
# MS=NetUser("Majhoul Al-Shoubasi","mas@gmail.moc")
# MS.addMovie("The Matrix")
# MS.rateMovie("The Matrix",10)
# MS.addMovie("The Godfather")
# MS.addMovie("Howl’s Moving Castle")
# print(IB,"\n")
# print(MS,"\n")
# print(MS.commonMovies(IB))

import graph

def buildStarGraph(n):
    G = graph.UndirectedGraph()
    for i in range(n):
        G.addNode(i)
    for i in range(1,n):
        G.connect(0,i)
    return G
# for n in (1,2,6):
#     G= buildStarGraph(n)
#     print(G)

def sortUnimodalList(L):
    def mergeTwoSortedLists(L1,L2):
        i = 0 #L1 [1,2,5]
        j = 0 #L2 [2,3,8,10,12]
        ans = [] #[1,2,2,3]
        while i < len(L1) and j < len(L2):
            if L1[i] > L2[j]:
                ans.append(L2[j])
                j = j+1
            else:
                ans.append(L1[i])
                i = i+1
        while i < len(L1):
            ans.append(L1[i])
            i = i+1
        while j < len(L2):
            ans.append(L2[j])
            j = j + 1
        return ans
    peak = max(L)
    for i in range(len(L)):
        if L[i] == peak:
            indexOfPeak = i
    firstHalf = L[:indexOfPeak]
    secondHalf = L[indexOfPeak:][::-1] #extracted the second half and reversed it
    ans = mergeTwoSortedLists(firstHalf,secondHalf)
    for i in range(len(ans)):
        L[i] = ans[i]

# L  = [1]
# print("L :", L)
# sortUnimodalList(L)
# print("L sorted:", L,"\n")
# L = [1,2]
# print("L :", L)
# sortUnimodalList(L)
# print("L sorted:", L,"\n")
# L = [1,2,4,7,11,10,8,4,-9]
# print("L :", L)
# sortUnimodalList(L)
# print("L sorted:", L,"\n")
# L = [1,2,5,20]
# print("L :", L)
# sortUnimodalList(L)
# print("L sorted:", L,"\n")
# L = [20,5,2,1]
# print("L :", L)
# sortUnimodalList(L)
# print("L sorted:", L,"\n")

def cumulativeMatrix(M):
    import copy
    C = copy.deepcopy(M)
    #i is the row
    #j is the column
    for i in range(1,len(M)):
        C[i][0] = C[i-1][0] + M[i][0]
    for j in range(1,len(M[0])):
        C[0][j] = C[0][j-1] + M[0][j]
    for i in range(1,len(M)):
        for j in range(1,len(M[0])):
            C[i][j] = C[i-1][j] + C[i][j-1] + M[i][j] - C[i-1][j-1]
    return C
# import numpy as np
# M1 = [[1,2],[3,4]]
# M2 = [[5,-2,1]]
# M3 = [[1],[10],[3]]
# M4 = [[1,5,3,4],[-4,2,10,0],[9,81,7,7]]
# for M in (M1,M2,M3,M4):
#     print("M")
#     print(np.matrix(M))
#     print("C")
#     print(np.matrix(cumulativeMatrix(M)),"\n")
#


def hasIsolatedElement(L):
    D = {}
    for elem in L:
        D[elem] = 0 #value not important
    for elem in L:
        if elem-1 not in D and elem+1 not in D:
            return True
    return False

# L1 = [7,1]
# L2 = [5,1,8,2,7,3]
# L3 = [1]
# L4 = [11,1,2,10,3]
# L5 = [5,1,2,6,3,4]
# L6 = [1,2]
# L7 = []
# for L in (L1,L2,L3,L4,L5,L6,L7):
#     print(L,":",hasIsolatedElement(L))
import graph

G = graph.UndirectedGraph()
G.addNode("A")
G.addNode("B")
G.addNode("C")
G.addNode("D")
G.addNode("E")
G.addNode("F")
G.addNode("G")
G.connect("A","B")
G.connect("B","C")
G.connect("B","G")
G.connect("B","E")
G.connect("C","E")
G.connect("C","D")
G.connect("D","G")
G.connect("G","F")

def hasTriangle(G):
    #I'm going to see if any of my neighbor's neighbors
    #contains one of my neighbors
    DictOfNbor = G.adj
    for item in DictOfNbor.items(): #loops over all nodes
        node = item[0]
        itsNeighbors = item[1] #the nodes connected to mynode
        for neighbor in itsNeighbors:
            #I wanna see if any of my neighbors' neighbors has
            #node as its neighbor
            scndNeighbor = DictOfNbor[neighbor]
            for neighbor in itsNeighbors:
                if node in scndNeighbor:
                    return True
    return False

print(hasTriangle(G))

def decompose(s):
    if len(s) == 0 or len(s) == 1:
        return [s]
    if len(s) == 2:
        return [s[0] + ' ' + s[1], s]
    ans = []
    branch2 = decompose(s[:len(s)-2]) #up until but not including last two chars
    branch1 = decompose(s[:len(s)-1])
    for item in branch2:
        new = item + ' ' + s[len(s)-2:]
        ans.append(new)
    for item in branch1:
        new = item + ' ' + s[len(s)-1:]
        ans.append(new)
    return ans

def twoConcatenation(L,t):
    #t = abcxd
    #item = axv
    #if xd is in the dictionary does not mean that item + xd = t
    D = {}
    for i in range(len(L)):
        elem = L[i]
        D[elem] = i #value not important
    for i in range(len(L)):
        elem = L[i]
        lenOfElem = len(elem)
        toBeFound = t[lenOfElem:]
        if toBeFound in D:
            if elem + toBeFound == t:
                return (i, D[toBeFound])
    return (-1,-1)
# L = ["ab","abc","axy","ca","bbc","a"]
# for t in ("abcca","abca","caabc","cabbc","caca","ca","caaca","cabbca","xy"):
#     print(twoConcatenation(L,t))

def twoNeighborhood(G,u):
    dictOfN = G.adj
    dictOfAns = {}
    for neighbor in G.adj[u]: #neighbors of u
        if neighbor not in dictOfAns:
            dictOfAns[neighbor] = 0 #value not important
        for sneighbor in G.adj[neighbor]: #getting the neighbors of neighbor
            if sneighbor not in dictOfAns:
                dictOfAns[sneighbor] = 0
    return list(dictOfAns.keys())

def decompositions(n):
    if n == 1:
        return ['1']
    ans = []
    for i in range(1,n):
        X = decompositions(i)
        for item in X:
            new = item + "+" + str(n-i)
            ans.append(new)
    ans.append(str(n))
    return ans

def numberOfWaysOut(M):
    def dfs(M,i,j):
        #if out of bounds
        if i < 0 or j < 0:
            return 0
        if i >= len(M) or j >= len(M[0]):
            return 0
        if M[i][j] == False:
            return 0
        if i == len(M)-1 and j == len(M[0])-1:
            return 1
        bot = dfs(M,i+1,j)
        right = dfs(M,i,j+1)
        return bot + right
    return dfs(M,0,0)

def maxAreaOfIsland(island):
    def dfs(island,i,j):
        if i < 0 or j < 0:
            return 0
        if i >= len(island) or j >= len(island[0]):
            return 0
        if island[i][j] == 2 or island[i][j] == 0:
            return 0
        if island[i][j] == 1:
            island[i][j] = 2
            up  = dfs(island,i-1,j)
            bot = dfs(island,i+1,j)
            left = dfs(island,i,j-1)
            right = dfs(island,i,j+1)
            return 1 + up + bot + left + right

    currMax = 0
    for i in range(len(island)):
        for j in range(len(island[0])):
            if island[i][j] == 1:
                currentPatch = dfs(island,i,j)
                currMax = max(currMax,currentPatch)
    return currMax
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))
