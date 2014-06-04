# 1. Very nice eqvivalents
a, b, c = 0, 0, 0
print a, b, c

a=b=c=2
print "Trick1: ", a, b, c

# 2. Another simplification

def function_one(a, b):
    if a < b:
        return a
    return b

def function_two(a, b):
    return (a, b)[a < b]

print "Trick2:", function_one(1, 2), function_two(1, 2)

# 3. Nice replacement of range function

print "Trick3:"

for i in range(8):
    print i

print "vs"

for i in [1]*8:
    print i

# 4. Small loops may look better this way
print "Trick4:"
for x in 0,1,2:
    print x

# 5. Use os.urandom() to access random integers faster
import os
print "Trick5:", ord(os.urandom(1))

# 6. Faster check if two values are true (both)

print "Trick6:", True*False, True*True, False*False

# 7. Nice way to assign variables

print "Trick7:"
a, b, c='123'
print a, b, c

# 8. Very hard conditional statements

print "Trick8:"

a = 2
b = 4

if a > 1 and b > 1 and 3 > a and 5 > b:
    print "Works with ends"


if 3 > a > 1 < b < 5:
    print "Works with no ends"

print "Wow, I love python!"

# 9. Timeit decorator
import time
def timeit(func):
    def _inner(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        dt = time.time() - t1
        print "Execution time", dt
        return res
    return _inner

@timeit
def summer(n):
    sum = 0
    for x in range(n):
        sum += x
    return sum

print summer(1000000)
