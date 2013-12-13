#This is an example of good code structure, dont worry if you dont understand all of it
#now, you will !

import time
import uitls

from random import randint


class GenRandomNumber(object):
    ''' Random number generator class '''
    
    def __init__(self, range, increment):
        #initilisation class
       
        self.range = range
        self.increment = increment
       
    def gen_rand_num(self):
        #method to return random number from range
        
        #get a random number form the range using the increment supplied in init
        random_number = randint(self.range, self.increment)
        
        #sleep for a few seconds
        time.sleep(3)
        
        #return the random number:
        return random_number
        
if __name__ = __main__():

    #instatiate the class
    generator = GenRandomNumber([1, 10], 1)
    
    #get a random numnber
    rand_num = generator.gen_rand_num()
    
    #print the random number generated
    print "Here is the random number : {}".format(rand_num)
    
