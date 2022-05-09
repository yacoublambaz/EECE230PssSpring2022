def antipodal(L):
    D = {}
    maxint = 0
    minint = 0
    for elem in L:
        maxint = max(abs(elem),maxint)
        minint = min(abs(elem),minint)
        if elem not in D:
            D[elem] = 1
        else:
            D[elem] += 1
    for i in range(minint,maxint+1):
        if i in D:
            if -1*i not in D or D[i] != D[-1*i]:
                print(i)
                return False
    return True

#problem 2
class intMod(object):
    def __init__(self,a=0,b=1):
        assert type(a) == int and type(b) == int and b > 0, "Invalid Type!"
        self.a = a % b
        self.b = b
    def __str__(self):
        ans = "{} (mod  {})".format(self.a,self.b)
        return ans
    def __add__(self,other):
        assert type(other) == intMod, "Invalid Operation!"
        assert other.b == self.b, "Invalid Operation!"
        return intMod((self.a + other.a)%self.b, self.b)
    
    def __sub__(self,other):
        assert type(other) == intMod, "Invalid Operation!"
        assert other.b == self.b, "Invalid Operation!"
        return intMod((self.a - other.a)%self.b, self.b)
    def __neg__(self):
        return intMod(-1*self.a % self.b, self.b)

    def __mul__(self,other): 
        assert type(other) == intMod, "Invalid Operation!"
        assert other.b == self.b, "Invalid Operation!"
        return intMod((self.a * other.a)%self.b, self.b)
    
# x = intMod(7,10)
# y = intMod(4,10)
# z = intMod(17,10)
# print(x)
# print(y)
# print(z)
# print(x+y)
# print(-x)
# print(x-y)
# print(x*y)


def zeroSumCorners(M):
    #slow implementation
    rows = len(M)
    columns = len(M[0])
    for i1 in range(rows):
        for i2 in range(i1,rows):
            for j1 in range(columns):
                for j2 in range(j1,columns):
                    if M[i1][j1] + M[i2][j1] + M[i1][j2] + M[i2][j2] == 0:
                        return True
    return False

def zeroSumCorners(M):
    #faster implemetation
    #assumes the idea that you do not need to loop twice over the columns (j)
    rows = len(M)
    columns = len(M[0])
    D = {}
    for j in range(columns):
        for i1 in range(rows):
            for i2 in range(i1,rows):
                if i1 != i2:
                    sum = M[i1][j] + M[i2][j]
                else:
                    sum = M[i1][j]
                if -1*sum in D:
                    if D[-1*sum][1] == i1 and D[-1*sum][2] == i2:
                        return True
                else:
                    D[sum] = (j,i1,i2)
    print(D)
    return False

# M = [[2,5],[-8,1]]         
# M = [[1,-50,3,6,11],[1,2,6,5,3],[1,-50,3,6,11],[3,7,8,3,2],[1,-8,3,1,-4],[20,7,-5,3,-10]]
# print(zeroSumCorners(M))

def generateAll(n):
    #slow, no memoization, using normal recursion and backtracking
    def rec(n,curr):
        if n < len(curr):
            return []
        if n == len(curr):
            return [curr]
        branch1 = rec(n,curr+"00")
        branch2 = rec(n,curr+"111")
        return branch1 + branch2
    if n == 0:
        return [""]
    return rec(n,"")

def generateAll(n):
    #faster, no memoization, using enumeration
    if n == 1:
        return []
    if n == 0:
        return [""]
    if n < 0:
        return []
    X = generateAll(n-2)
    Y = generateAll(n-3)
    ans = []
    for x in X:
        ans.append(x + "00")
    for y in Y:
        ans.append(y + "111")
    return ans

def generateAll(n):
    #fastest, using memoized enumeration
    def mem(n,L):
        if n == 1:
            return []
        if n == 0:
            return [""]
        if n < 0:
            return []
        if L[n] != -1:
            return L[n]
        else:
            X = mem(n-2,L)
            Y = mem(n-3,L)
            ans = []
            for x in X:
                ans.append(x + "00")
            for y in Y:
                ans.append(y + "111")
            L[n] = ans
            return L[n]
    L = [-1 for i in range(n+1)] 
    return mem(n,L)
# print(generateAll(0))
# print(generateAll(1))
# print(generateAll(2))
# print(generateAll(3))
# print(generateAll(4))
# print(generateAll(5))
# print(generateAll(6))
# print(generateAll(7))
# print(generateAll(8))
# print(generateAll(9))
