"""
Problem 1 (Easy):

Write a python code that plays rock paper scissors.
First, player 1 should type what they went for (rock,paper, or scissors)
Second, player 2 should type what they went for
Then, the code should determine who won (or it could be a draw)
eg:
player1: rock
player2: Scissors
answer: player 1 won

eg:
player1: scissors
player2: paper
answer: player 1 won

Step:
1. Ask input from the first user x
2. Ask input from the second user x
3. if user1 == user2, return draw
4. if user1 is rock and user 2 is paper, then user 2 won

"""
"""
user1 = input("Please enter the first user's choice... ")
user2 = input("Please enter the second user's choice... ")

if (user1 == user2):
    print("The match is a draw")
else:
    if (user1 == "rock" and user2 == "paper"):
        print("user 2 won")
    if (user1 == "paper" and user2 == "scissors"):
        print("user 2 won")
    if (user1 == "scissors" and user2 == "rock"):
        print("user 2 won")

    if (user2 == "rock" and user1 == "paper"):
        print("user 1 won")
    if (user2 == "paper" and user1 == "scissors"):
        print("user 1 won")
    if (user2 == "scissors" and user1 == "rock"):
        print("user 1 won")

"""
"""
Problem 2 (Easy):
Write a function findNeedle() which given a list L = ["hay","hay","needle","hay","hay"]
returns if "needle" is in the haystack and where it is located
eg:
L = ["hay","hay","needle","hay","hay"]
answer: the needle is in index 2
L = ["hay","hay","hay","hay","hay"]
answer: the needle does not exist

steps:
1. Check if the input is a list, if not return an error x
2. Loop over the list
3. If "needle" is found in the list, return the index
4. If the loop is over, return -1
"""

def findNeedle(L):
    assert type(L) == list, "Please enter a list value"
    for i in range(len(L)):
        elem = L[i]
        if elem == "needle":
            return i
    return -1

L = ["hay","hay","hay","hay"]
x = findNeedle(L)
print(x)

"""
Problem 3 (Easy):
Design an interface for the password cracking software that accepts input
from the user in terms of the hashed password and runs crack() function
and returns the password to the user
"""

#hashPw = input("Please enter the hashed password: ")
#size = input("Please enter expected size of the password")
#realPw = crack(hashPw)
#print(realPw)

"""
Problem 4 (Medium):
Design a hashcode function that performs a caesar cipher by adding 1 to each digit
as follows:
hash(178) -> 289
hash(787) -> 898
You will not see cases with any 9's

Step:
0. Convert the integer to a string x
1. Loop over the string
2. Convert the digit into an integer, add 1 to it, and then store it back as a string

"""

def hash(num):
    assert type(num) == str, "Please enter a string"
    strNum = str(num)
    ans = ""
    for digit in strNum:
        intDigit = int(digit)
        intDigit = intDigit + 1
        strDigit = str(intDigit)
        ans = ans + strDigit
    return ans

"""
Problem 5 (Medium):
Design the password cracking software that loops over all possible passwords
and guesses which one is the correct one.

After you did that, make it more optimized. Can you use the fact that
if pw1>pw2
then
hash(pw1) > hash(pw2) in your optimization? Hint: Binary Searching

Steps:
1. Run the interface
2. For the crack() function:
2.1 Loop over all possible integers
2.2 run the hash function on the integer
2.3 if the hashed integer == hashedpw, then we know that we found the original password
"""

def crack(hashPw, size):
    assert type(hashPw) == str and type(size) == int, "Please make sure hashpw is string and size is int"
    endOfLoop = "1" + "0"*size #upper boundary
    endOfLoop = int(endOfLoop)
    #I can also set a lower bound
    startOfLoop = "9" * (size-1)
    startOfLoop = int(startOfLoop) + 1
    #if size == 5:
    # start of loop: 9999 + 1 = 10000
    # end of loop: 100000, we know that the range stops at 99999
    for i in range(startOfLoop, endOfLoop):
        if hash(i) == hashPw:
            return i
    return -1

def crackOpt(hashPw,size):
    assert type(hashPw) == str and type(size) == int, "Please make sure hashpw is string and size is int"
    endOfLoop = "1" + "0"*size #upper boundary
    endOfLoop = int(endOfLoop)
    #I can also set a lower bound
    startOfLoop = "9" * (size-1)
    startOfLoop = int(startOfLoop) + 1
    low = startOfLoop
    high = endOfLoop
    hashPw = int(hashPw)
    #######
    while low<=high:
        mid = (low+high) // 2
        hashPwCalc = int(hash(str(mid)))
        if hashPwCalc == hashPw:
            return mid
        elif hashPwCalc > hashPw:
            high = mid - 1
        else:
            low = mid + 1
    if low > high: #in case the binary searching failed
        return -1
    else:
        return mid

#hashPw = input("Please enter the hashed password: ")
#size = int(input("Please enter expected size of the password: "))
#realPw = crackOpt(hashPw,size)
#print(realPw)

"""

Binary searching:

I want to find 18 in a range of numbers:
lowPoint = 1000
highPoint = 9999
hashPw = 5656

loop1:
mid = (1000 + 9999) // 2 #5500
is hash(5500) > 5656?

loop2:
mid = (0 + 5500) // 2 #7750
is hash(7750) > 5656
new upper bound is previous mid = 7750

loop3:
mid = (5500 + 7750) // 2 # 6625
is 12.5 > 18? No it is not! The new lower bound is now 12.5

loop4:
mid = (12 + 25) // 2 18


BREAK UNTIL 8:02
"""
def check(x):
    if x >= 46551512:
        return True
    else:
        return False
"""
Problem 6

Given a function check(x), check(x) is going to be false for all numbers below a number
and is going to be true for all numbers above this number

so for example, if that number was 300, then check(200) == false, check(302) == true

write a function guess() and returns the number where check starts becoming true

steps:
1. loop over numbers until we find the first number that returns true
"""

def guess():
    start = 0
    checker = check(start)
    while checker == False:
        start = start + 1
        checker = check(start)
    return start

def guessOpt():
    low = 0
    high = 100000000
    while low < high:
        mid = (low + high) // 2
        if check(mid) == True and check(mid-1) == False:
            return mid
        elif check(mid) == True and check(mid-1) == True:
            high = mid-1
        else:
            low = mid + 1
    return -1

print(guessOpt())
