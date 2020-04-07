x = 5
y = 6
z = x + y
print('Hello World\nWelcome back to python!\n')
print( x, '+', y, '=', z)

print('')
myTuple = 'Tyler', 26
print(type(myTuple))
print(myTuple)

mySet = {1 : "World"}
mySet.clear()
mySet = {2 : "Hello"}

#Even Method identifier
def myfunc(num):
    if num %2 == 0:
        return 'Is even'
    else:
        return 'Is odd'

def p(a):
    #shorter print method
    return print(a)

p("hello")

#Sets will not repeat the same input
#Sets are not in order
myset = set(['Hello', 'world', 'hello', 'world', 'myName'])

print('\n')
print(myset)


print('\n')
print(myfunc(9))
print('\n')

print('\n')
print(myfunc(104))
print('\n')

print('\n')
print(myfunc(912412241))
print('\n')


print('\n')
print(myfunc(0))
print('\n')

print(mySet)
print(type(mySet))