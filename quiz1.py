"""
Problem 2.a)

Guilty until proven innocent
All substrings are concatenations of two identical substrings until they prove otherwise

How do they prove otherwise?
1) If their lengths are odd
2) If s[i] != s[i+(len(s)//2)]
"""

def repeated(s):
    if len(s) % 2 != 0: 
        return False
    halfLen = len(s) // 2
    firstHalf = 0
    secondHalf = 0
    while secondHalf < len(s):
        secondHalf = firstHalf + halfLen
        if secondHalf >= len(s):
            break
        if s[firstHalf] != s[secondHalf]:
            return False
        firstHalf = firstHalf + 1
    return True

"""
Problem 2.b)

SLIDING WINDOWS!

Steps:
1) for loop to decide length of sliding window
2) slide the window across the string until you see a string that doesn't match
3) if the window finishes the string, it counts as valid
"""

def root(s):
    #define length of sliding window
    for i in range(1,len(s)+1):
        firstWindowStart = 0
        firstWindowEnd = i
        firstWindow = s[firstWindowStart:firstWindowEnd]
        windowLoopStart = i
        windowLoopEnd = windowLoopStart + i
        multiplicity = 1
        while windowLoopEnd <= len(s): 
            secondWindow = s[windowLoopStart:windowLoopEnd]
            if secondWindow != firstWindow:
                break
            else:
                windowLoopStart = windowLoopEnd
                windowLoopEnd = windowLoopEnd + i
                multiplicity += 1
        if multiplicity != 1:
            return (firstWindow, multiplicity)
    return (s,1)

def atMostTwoZeros(L):
    """
    Guilty until proven innocent, all lists have at most two zeroes until proven otherwise.
    They prove otherwise by having... you know... more than two zeros :D
    """
    count = 0
    for elem in L:
        if elem == 0:
            count += 1
            if count > 2:
                return False
    return True

def partBWhichsNameIsTooLong(L):
    """
    The longest ____ sublist formula!
    """
    maxLen = 0
    maxSub = []
    for i in range(len(L)):
        for j in range(i,len(L)):
            subL = L[i:j+1]
            if atMostTwoZeros(subL):
                if len(subL) > maxLen:
                    maxLen = len(subL)
                    maxSub = subL
    return maxSub
