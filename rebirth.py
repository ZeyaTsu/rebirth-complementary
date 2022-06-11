import random
import math

########################################################################
######################### REBIRTH BASIC ################################
#########################    SECTION    ################################
########################################################################

#### Vector: coordinates from points xA, yA, xB, Yb | DET

def vector_x(xa, xb):
    Pa = xb - xa
    return Pa 

def vector_y(ya, yb):
    Pb = yb - ya
    return Pb

def vector_det(x, y, x1, y1):
    det = (x * y1) - (y * x1)
    return det

# Example
# a = vector_x(6, 12)
# b = vector_y(12, 6)
# print(a,b)
# = 6 -6
# c = vector_det(a, b, a1, b1)
# print(c)

#### Generate a random number

def rand(min1, max1):
    rand = random.randint(min1, max1)
    return rand

# d = rebirth.rand(1, 10)
# print(d) random number.
    
#### Number guesser
## Need rebirth.rand(min1, max1) (see example)

def guess(rand):    
    guess = float(input("Rebirth| Guess > "))
    if guess == rand:
        print("Rebirth| You found the correct number.")
    elif guess < rand:
        print("Rebirth| Higher!")
    elif guess > rand:
        print("Rebirh| Lower!")
    return guess

# Example
# d = rebirth.rand(1, 10)
# s = True
# while s:
#    e = rebirth.guess(d)
#    if e == d:
#       s = False
#/!\ rebirth.rand(min1, max1) to make it work!

# Number generator from Pi

def pi_gen(value, times):
    pi_gen = math.pi
    for i in range(1, times+1):
        pi_gen += value
        print(pi_gen)

# Example
# rebirth.pi_gen(2.124, 5)
# = 5.265592653589794
#   7.389592653589794
#   9.513592653589795
#   11.637592653589795
#   13.761592653589796

#### All informations about the Python Module

def info():
    print("Rebirth Complementary | Python Module")
    print("Rebirth Complementary is Rebirth basic but with more features.\n")
    print("- A simple python module using simple functions")
    print("- Useful for some things like vector calculations")
    print("- Less useful but still good like pi_gen")
    print("- Made for fun.")
    return info

# rebirth.info()

#### Generating password /!\ Have fun to customize it by yourself

def password(len):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "[]{}#()*;._-"
    ans = lower_case + upper_case + number + symbol

    length = len
    password = "".join(random.sample(ans, length))

    return password

#### Example
# print("Your new password is", rebirth.password(6))
## OR
# length = int(input("Password length: "))
# print("Your new password is", rebirth.password(length))

#### Ping
def ping():
    print("Pong(1)")
    return ping
    
#### Number: Odd or Even 

def odd_even(number, messageEven, functionEven, messageOdd, functionOdd):
    if number % 2:
        print(messageOdd)
        functionOdd()
    else:
        print(messageEven)
        functionEven()

### None

def none():
    len("None")

### Example
# rebirth.none()
# Use example
# rebirth.odd_even(2, "Even", rebirth.none, "odd", rebirth.none) to call no function

# Example
# rebirth.odd_even(2, "Even", "Odd")
# = Even
## IF YOU WANT 0 MESSAGE TO SAY ODD OR EVEN
# rebirth.odd_even(2, "", "")
# = 
## OTHER EXAMPLE
# rebirth.odd_even(rebirth.rand(1,20), "Even", "Odd")

#### For... loop

def loop(value, times, function):
    for value in range(1, times+1):
        function()

## Value is a 'group' it means that if you want to make a different loop you change the value (which is a
# number)
### Example
# rebirth.loop(1, 10, hi)
# it will repeat the hi() function 10 times in group1.
# rebirth.loop(2, 10, bye)
# it will repeat the bye() function 10 times in group2

#### Infinity Loop (Checker Loop)

def loopinf(value, function):
    for o in range(1, value):
        for p in range(1, value):
            function()
        value = value * 5
            
### Different of the while loop!
### value 4 = True
### value 0 = False
## Example
# rebirth.loopinf(4, hi)
# will repeat the hi() function infinity as long you don't change value by 0
# rebirth.loopinf(0, hi)
# the loop on the hi() function will end.

########################################################################
######################### REBIRTH COMPLEMENTARY ########################
#########################      ZEYATSU C        ########################
#########################      SECTION          ########################
########################################################################

#### Square & Cube Function

def function_sqr(n):
    a = n**2
    print(a)
    if n < 0:
        maxi = n * -2 + 1
    elif n >= 0:
        maxi = n * 2 + 1 

    for w in range(1, maxi):
        n += 1
        a = n**2
        print(a)

def function_cube(n):
    a = n**3
    print(a)
    if n < 0:
        maxi = n * -2 + 1
    elif n >= 0:
        maxi = n * 2 + 1 

    for z in range(1, maxi):
        n += 1
        a = n**3
        print(a)

### Example
# rebirth.function_sqr(-4)
# does the square function from -4 to 4.
# rebirth.function_cube(-4)
# does the cube function from -4 to 4.
## Replace N by a number (+ or -)

#### Call function

def callfunction(function):
    function()

### Example
# def hi():
#   print("hi")
# rebirth.callfunction(hi)
# = hi

### Print message

def say(message):
    print(str(message))

#### Example
# rebirth.say("hi") 
# = hi
## /!\ " " Very important or it doesn't work.

### Caracters counter

def count(PSmes, message, state = str):
    if state == "YES":
        print(PSmes, len(message))
  
### Example
# rebirth.count("Message caracters:", "Hello world", "YES")
# = Message caracters: 11
## OR
# rebirth.count("", "Hello world", "YES")
# = 11
## IF YOU DON'T WANT ANY MESSAGES
# rebirth.count("Message caracters", "Hello word")
# = 
## OR
# rebirth.count("", "Hello world")
# = 

#### Check response 

def check_response(value, value2, function, function1):
    if value == value2:
        function()
    else:
        function1()

### Example
# def same():
#   print("The result is the same number")
# def dif():
#   print("This is not the same number")
# a = 2 + 2
# b = 5 - 1
# rebirth.check_response(a, b, same, dif)
# a & b = 4 so 
# = The result is the same number
## Explanation
# value is the variable (like a = 1+1 or b = 3-1) it could be anything else.
# function is the function in case value = value2
# and function1 is the function in case value is different of value2
# it's like the if and else condition.