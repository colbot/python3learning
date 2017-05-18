# -*- coding: utf8 -*-
# function define and call


def func1():
    print('hello world!')


def func2(arg1):
    print('hello world, %s!' % str(arg1))


def func3(arg1='Zhang'):
    print('Hello world, %s!' % str(arg1))


def func4(arg1, arg2='Hello'):
    print('%s world, %s!' % (arg2, arg1))


def func5(arg):
    print('string length is {0}'.format(len(arg)))
    return len(arg)


def func6(arg1, *argl, **aall):
    print('arguments are:')
    print('1\t'+str(arg1))
    print('2\t'+str(argl))
    print('3\t'+str(aall))

print('start calling')
func1()
func2('zhang')
f3 = func3
f3()
f3('Li')
func4('Li')
func4('Li', 'Morning')
func4(arg2='Morning', arg1='Zhang')
s = 'hello world!'
print('String length of "%s" is %d' % (s, func5(s)))
func6('start', 'first', 'second', 'end', varg1='a', varg2='b', varg4='d')

argd={'in1': 'q', 'in2': 'w', 'in3': 'e', 'in4': 't'}
argt=('a', 'b', 'c', 'd')
func6(argt)
func6(*argt)
func6(*argt, **argd)


# lambda function
p1 = lambda x, y: (x,y)
print('2 ,3 for lambda is '+str(p1(2, 3)))