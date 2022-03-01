"""
I would like to find a divisor
that is a square

1- checked if it's a square
2- check all divisiors of the number
"""

def squareFree(x):
    def isSquare(n):
        #Check if n is a square
        limit = int(n ** (1/2))
        for i in range(limit+1):
            if i*i == n:
                return True
        return False
    #Loop over the entirety of the divisiors
    #As soon as we see a divisor that happens to be
    #a square
    #ALL NUMBERS ARE SQUARE FREE UNTIL PROVEN OTHERWISE
    if x == 1:
        return True
    for i in range(2,x+1):
        if x % i == 0:
            if isSquare(i):
                return False
    return True

def fractionOfSquareFreeUpTo(n):
    count = 0
    for i in range(1,n+1):
        if squareFree(i):
            count = count +  1
    fraction = count / n
    return fraction


def similarStringsA(s1,s2):
    """
    ALL STRINGS ARE SIMILAR UNTIL THEY PROVE OTHERWISE
    Strings prove that they are not similar by
    1- Having different lengths
    2- Having more than one different character
    """
    if len(s1) != len(s2):
        return False

    counter = 0 #count the number of different elements
    for i in range(len(s1)):
        #s1 = "abc", s2 = "aab"
        if s1[i] != s2[i]:
            counter = counter + 1
            if counter >= 2:
                return False
    return True

"""
An example of a two-pointer problem

s1 = "abc", s2 = "abcd"
i = 0
j = 0

1) if s1[i] == s2[j]:
    i = i+1
    j = j+1
2) else:
    increment the variable corresponding
    to the string of highest length
    IF WE DO THIS STEP MORE THAN ONCE,
    RETURN FALSE
3) if we finish the entire string
if one of them is not equal to
their lengths, then return

abc
abca
"""
def similarStringsB(s1,s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) == len(s2):
        if similarStringsA(s1,s2):
            return True
        else:
            return False
    #initialize two pointers
    i = 0 #corresponds to s1
    j = 0 #corresponds to s2
    isDoneC = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i = i+1
            j = j+1
        else:
            if isDoneC == 1:
                return False
            isDoneC = 1
            if len(s1) > len(s2):
                i = i + 1
            else:
                j = j + 1
    if len(s1)-i > 2 or len(s2)-j > 2:
        return False
    if abs(i-j) <= 1:
        return True
    if not similarStringsA(s1,s2):
        return False
    return True


#let's assume we did part isUnbroken
#longest unbroken sublist

"""

0- define two variables, one to store the longest length
and the other to define the longest substring/sublist

1- GET ALL SUBLISTS:
for i in range(len(L)):
    for j in range(i,len(L)):
        subL = L[i:j+1]
        #I got ALL SUBLISTS

2- from these sublists, which of them match part a?
which of subL is unbroken?

3-if it is unbroken, is it longer than the longest unbroken
sublist so far? if it is, then replace the values in part 0

"""

def isUnbroken(L):
    for i in range(1,len(L)):
        if abs(L[i-1] - L[i]) > 1:
            return False
    return True

def longestUnbrokenSublist(L):
    longestLen = 0
    longestSubL = []
    for i in range(len(L)):
        for j in range(i,len(L)):
            subL = L[i:j+1]
            if isUnbroken(subL):
                if len(subL) > longestLen:
                    longestLen = len(subL)
                    longestSubL = subL
    return longestSubL


"""

BREAK UNTIL 8:17

Next previous
"""
# inp = int(input("please enter input: "))
# if inp % 2 != 0:
#     print(3*inp + 1)
# else:
#     print(inp // 2)

def isBinary(s):
    for i in range(len(s)):
        if s[i] != "0" and s[i] != "1":
            return False
    return True

def ithDivisor(n,i):
    """
    1- Find all divisors -> store in a list
    2- find the ith element of all divisors
    3- if n <= 0 or i <= 0: return -1
    4- if no divisor whatsoever, return -1
    5- if you're asking for an index that's higher
    than how many divisors we have, return -1
    """
    if n <= 0 or i <= 0:
        return -1
    store = []
    for j in range(1,n+1):
        if n % j == 0:
            store.append(j)
    if len(store) == 0: #no divisors
        return -1
    if i > len(store):
        return -1
    return store[i-1]

def countNumsWithIthDiv(n,i):
    """
    . if n <= 0 or i <= 0: return -1
    0- count = 0
    1- loop for k in range(n+1)
        for each k, check if ithDivisor(k,3) does not return -1
        if it doesn't return -1, count = count + 1
    """
    if n <= 0 or i <= 0:
        return -1
    count = 0
    for k in range(1,n+1):
        if ithDivisor(k,i) != -1:
            count = count + 1
    return count


def isBivalued(L):
    store = []
    for i in range(len(L)):
        if L[i] not in store:
            store.append(L[i])
        if len(store) > 2:
            return False
    return True

def lenOfLongestBivalued(L):
    lenLongest = 0
    for i in range(len(L)):
        for j in range(i,len(L)):
            subL = L[i:j+1]
            if isBivalued(subL):
                if len(subL) > lenLongest:
                    lenLongest = len(subL)
    return lenLongest
