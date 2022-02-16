"""
Problem Solving Techniques

1- Guilty Until Proven Innocent

"""

def isSquare(x):
    """
    Determines if x is a Square or not
    """
    isSquare = False
    for i in range(x):
        if i*i == x:
            isSquare = True

    if isSquare == True:
        return True
    else:
        return False

def isSorted(L):
    """
    Determines if a list is sorted or not
    L = [1,2,3,4,5,6,7,8]
    """
    isSortedAns = True
    for i in range(1,len(L)):
        if L[i] < L[i-1]:
            isSortedAns = False
            break
    return isSortedAns

def isPalindrome(s):
    """
    Determines if s is a Palindrome or not
    A string is palindrome if it reads the same forwards
    and backwards

    magam -> yes
    civil -> not
    anna -> yes

    Steps:
    1. Define two variables i and j, i at 0, j at the len(s)-1
    2. ALL STRINGS ARE PALINDROMES UNTIL THEY PROVE OTHERWISE
    3. if s[i] != s[j]
    4. if s[i] == s[j], i +=1, j -=1
    """
    i = 0
    j = len(s)-1
    isPal = True
    while i <= j:
        if s[i] != s[j]:
            isPal = False
            break
        else:
            i = i+1
            j = j-1

    return isPal

print(isPalindrome("anna"))
print(isPalindrome("magam"))
print(isPalindrome("maya"))

def isValidPara(s):
    """

    Determine if the paranthesis are valid or not
    s = "(Hello Guys)" -> valid
    s = " (Hello (Guys))" -> valid
    s = "((()))" -> valid
    s = "())" -> invalid
    s = ")()(" -> invalid
    s = "()()()()" -> valid

    1. at the end of the checking openPara == closedPara
    2. IF AT ANY POINT: closedPara > openPara: GUILTY!

    "())()("
    openPara = 1
    closedPara = 2
    """

    isValid = True
    openPara = 0
    closedPara = 0
    for letter in s:
        if letter == "(":
            openPara += 1
        if letter == ")":
            closedPara += 1
        if closedPara>openPara:
            return False
    if openPara == closedPara:
        return True
    else:
        return False

"""
2- Repeat a small problem

"""

def getHomingNumber(x):
    """
    x's homing number is a summation of its digits
    131 -> 5
    99 -> 18 -> 9
    587 -> 20 -> 2
    """
    def reduce(x):
        """ Reduce once 99 -> 18 """
        ans = 0
        x = str(x)
        for num in x:
            ans = ans + int(num)
        return ans
    while x >= 10:
        x = reduce(x)
    return x

print(getHomingNumber(952178658))



def shift(L,N):
    """
    Write a function that shifts all elements to the right N times

    L = [0,1,2,4,5,1] N = 3 -> L = [4,5,1,0,1,2]
    L = [0,1,2,4,5,1] -> L = [1,0,1,2,4,5]
    L = [0,1,2,4,5,1]
    temp = 0
    0) i = 1, L[0] = L[1], L = [1,1,2,4,5,1]
    1) i = 2, L[1] = L[2], L = [1,2,2,4,5,1]
    2) i = 3, L[2] = L[3], L = [1,2,4,5,5,1]
    3) i = 4, L[3] = L[4], L = [1,2,4,5,1,1]
    4) i = 5, L[4] = L[5], L = [1,2,4,5,1,1]
    after this, let L[last element] be 0 -> [1,2,4,5,1,0]

    Steps:
    1. Shift to the right once:
        1. Store the last element in a dummy variable
        2. let L[i+1] be L[i]
        3. let L[0] be the last element that we stored earlier
    2. Do that n times
    """
    def shiftOnce(L):
        temp = L[0]
        for i in range(1,len(L)):
            L[i-1] = L[i]
        L[len(L)-1] = temp
        return L
    for i in range(N):
        L = shiftOnce(L)
    return L

print("Shifting problem here: ")
print(shift([0,1,2,4,5,1], 3))





"""
3- ... wait, I know this from before!
hint: is it binary searching? is it two-sum problem? is it a two-pointer problem?

Big O notation:

L = [1,2,4,5,1,2,4,5] check if 8 is in the list
O(1) x = 5
O(logN)
L = [1,2,4,5,6,7,9,10] check if 8 is in the list
0) L = [6,7,9,10]
1) L = [9,10]
2) L = []
O(N) where N == len(list)

O(N^2) given x, give me two numbers whose squares add up to x, i*i + j*j == x


Traveling salesman problem NOT OPTIMIZED: O(N^2 * 2 ^ N)

L = [9,4,2,1,2,6,8] return two elements that add up to 7
"""

def getBestMovieTimings(movieList, movieRunTimeList, flightLen):
    """
    Write a function that gets two movies with lengths that add up to the length
    of the flight.
    movieList = ["PoC", "Dark Knight", "AoT"]
    runTimes = [70, 90, 50]
    flightLen = 120

    Steps:
    1. Loop for i in range len movieList
    2. Loop for j in range i, len movielist
    if movieRunTimeList[i] + movieRunTimeList[j] == flightLen:
        return movieList[i], movieList[j]
    """
    for i in range(len(movieList)):
        for j in range(i+1,len(movieList)):
            if movieRunTimeList[i] + movieRunTimeList[j] == flightLen:
                return (movieList[i], movieList[j])
    return (-1,-1)


def findPeak(L):
    """
    Given a list L as such [1,2,3,5,8,6,4,3,2,1]
    find the index of the peak number

    THINK ABOUT BINARY SEARCHING AS FOLLOWS:
    1. How do I know I reached the right element?
    2. How do I know to look to the right? (Increase my lower bound)
    3. How do I know to look to the left? (Decrease my upper bound)

    IN USUAL BINARY SEARCH:
    1) is L[mid] == x: return mid
    2) is L[mid] > x: low = mid+1
    3) is L[mid] < x: high = mid-1

    In our case:
    1) if L[mid] > L[mid-1] AND L[mid] > L[mid+1] return mid #is this the peak?
    2) if L[mid] > L[mid-1]: low = mid+1
    3) if L[mid] < L[mid-1]: high = mid-1

    """

    low = 0
    high = len(L)-1
    while low<=high:
        mid = (low+high)//2
        if L[mid] > L[mid-1] and L[mid] > L[mid+1]: #isPeak?
            return mid
        elif L[mid] > L[mid-1]: #ascending half
            low = mid+1
        else:
            high = mid-1 #descending half
    return -1

print(findPeak([1,2,3,4,5,6,8,7,5,4,2]))

def squaresOfSortedListTwoSum(L,x):
    """
    Given a sorted list, return two numbers in the list whose squares add up to x
    L = [1,2,5,7,9,11] x = 85, the two elements are 2 and 9
    """
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] ** 2 + L[j] ** 2 == x:
                return (i,j)
    return (-1,-1)

def squaresOfSortedListPointers(L,x):
    """
    L = [1,2,5,7,9,11], x = 85
    THREE CONDITIONS:
    1) L[i] squared + L[j] squared == x: return i,j
    2) L[i] squared + L[j] squared > x: decrease j
    3)2 L[i] squared + L[j] squared < x: increase i
    _______________________
    0) i = 0, j = 5, 1 + 121 = 122
    1) i = 0, j = 4, 1 + 81 = 82
    2) i = 1, j = 4, 4 + 81 = 85
    """
    i = 0
    j = len(L)-1
    while i <= j:
        if L[i]**2 + L[j] **2 == x:
            return (i,j)
        if L[i]**2 + L[j] **2 < x:
            i = i+1
        else:
            j = j-1
    return (-1,-1)


def sumOfTwoSquares(x):
    """
    Write a function that given x finds two square numbers that add up to x: i*i + j*j == x
    Hint: We're looking for a O(nlogn) solution
    """
    return
