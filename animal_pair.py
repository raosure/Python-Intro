# Write a function that accepts two positive integers as parameters. 
# The first integer is the number of heads and the second integer is 
# the number of legs of all the creatures in a farm which consists of 
# chickens and dogs. Your function should calculate and return the number 
# of chickens and number of dogs in the farm in a list as specified below. 
# If it is impossible to determine the correct number of chickens and 
# dogs with the given information then your function should return None. 
# Example 1, if your function received the following numbers:

def animal_pair(x,y):
	if ( y % 2 != 0):
		return 
	if ( float(y)/2 < x):
		return
	if (x < float(y)/4 ):
		return
	anim = [0,0]
	if ( (float(y) / x) == 4):
		anim[1] = x
	elif ( float(y) / x == 2):
		anim[0] = x
	else:
		while (y > 2 ):
			y = y - 4
			anim[1] = anim[1] + 1
			x = x -1
			if ((2*x - y) == 0):
				anim[0] = x
				y = 0			
	return anim

		

a = int(input())
b = int(input())
animal_pair(a,b)

################### Sample Solution ###################
def _sample_fun_puzzle_ (heads,legs):
    dogs=(legs-heads*2)/2
    if dogs<0 or dogs%1:
        return None
    dogs=int(dogs)
    chickens=heads-dogs
    if chickens< 0:
        return None
    return [chickens,dogs]