# Given
x = 10000.0
y = 3.0
print(x / y)
print(10000 / 3)
# What is happening?
# Python 2: 3333 3333, unless import __future__
# Python 3: 3333.3333... 3333.3333....

# Given
print(x - 1 / y)
print((x - 1) / y)
# What is happening?
# Python 2: 10000 3333
# Python 3: 9999.6666... 3333.0

# Given 
x = 'foo'
y = 'bar'
# Create 'foobar' using x and y
print(x + y)
# Create 'foo -> bar' using x and y
print(x + ' -> ' + y)

# Given
x = 'hello world'
# from x create 'HELLO WORLD'
print(x.upper())
# from x create 'hellX wXrld'
print(x.replace("o", "X"))

# Given
x = 10000.0
y = 3.0
# print "10000 / 3 = 3333" using x and y
print("%.0f / %.0f = %.0f" % (x, y, x / y))

# Given
x = ['hello', 'world']
# print 'helloworld'
print("".join(x))
# print 'hello world'
print(" ".join(x))
# print 'hello
# world'
print("\n".join(x))

# Given
x = "Monty Python and the Holy Grail"
# create the list ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']
print(x.split(" "))
y = "one,two,three,four"
# create the list ['one', 'two', 'three', 'four'
print(y.split(","))
