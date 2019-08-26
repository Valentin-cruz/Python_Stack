import random
def randInt(min=   , max=   ):
    num = random.random()
    return num

#print(randInt()) 		    # should print a random integer between 0 to 100
import random
def randInt(min="", max=""):
    num = random.random()*100
    round(num)
    return num
print(randInt())

#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
import random
def randInt(min= "", max=""):
    num = random.random()*50
    round(num)
    return num
print(randInt())

#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
import random
def randInt(min="", max=""):
    num = random.random()*100
    round(num)
    return num + 50
print(randInt())
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
import random
def randInt(min="", max=""):
    num = random.random()*500
    round(num)
    return num + 50
print(randInt())