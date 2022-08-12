from functions import *
import constants as c
#this is where i will call the function and will use other files to run.
#This program will take a min and max value and will return all primes as a list in that range

def run():
   a = list_prime(c.MIN,c.MAX)
   print(a)

if __name__ == '__main__':
    run()