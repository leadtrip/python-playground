print("Giant buttons")

x = 1
if x == 1:
    # python uses indentation, usually 4 spaces rather than braces for blocks
    print("x is 1")

# python supports either integers or floating point numbers
myint = 7
myfloat = 3.2

mystring1 = 'single quotes'
mystring2 = "double quotes"

a, b, c = 'a', 9, 1.9   # multiple assignment is cool

alist = ['sun', 'mercury', 'venus', 'earth']    #create and fill list
mylist = [] #new list, use append to add elements
mylist.append(1)
mylist.append(2)
print(mylist[0] + mylist[1])

allstuff = alist + mylist   #combine lists with +
print(allstuff)

print(mylist * 4)   #repeat list with *

loadsofmikes = 'mike' * 4 #repeat strings
print(loadsofmikes)

myname = 'mike'
myactivity = 'rolling'
print("Wow %s, you're amazing at %s" % (myname, myactivity))

print(len("How long am I?"))
print(myname.index('k'))
print('keep it down'.upper())
print('keep it down'.lower())
print('keep it down'.capitalize())
print('keep it down'.count('e'))
print('keep it down'[3:7])  # substring


