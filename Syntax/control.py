# -*- coding:utf-8 -*-
# python flow control syntax

# if
a = 1
b = 2
if a == 1:
    print("a is 1")
elif b > 2:
    print("b above 2")
else:
    print("nothing")

if a > 0 and b > 0:
    print("a and b are both positive")

if a > 0 or b > 0:
    print(" a or b is positive")

if not a == 0:
    print('a is not 0')

# no switch-case, use if-elif-else instead
if a == 0:
    pass
elif a == 1:
    pass
elif a == 2:
    pass
elif a == 3:
    pass
else:
    print("default branch")


# for
# only support for-in state to loop
c = [1, 2, 3, 4, 5]
d = ('a', 'b', 'q', 'w', 't')
e = {1: '1', 2: '0', 4: 'df', 5: 'er'}
for i in range(9):
    print("num is %d".format(i))
for i in range(2, 15, 3):
    print("step increase now at %d" % i)
for i in c:
    print('current num is '+str(i))
for ch in d:
    print("current char is "+ch)
for s in e:
    print("dic key %s : value %s" % (s, e[s]))
else:
    print("loop finished with out break")

# while state to loop
x = 0
while x < 10:
    x = x + 1
    print("x is %d" % x)
x = 0
while True:
    x = x + 1
    if x > 10:
        break
    if x % 2 == 0:
        continue
    print('x loop at %d' % x)
else:
    print("loop finished with out break")

# boolean state
# in & not in
# is & is not
# >, >=, <, <=, ==
# and, or, not
# no assign in boolean expression