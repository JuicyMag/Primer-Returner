#This will house any functions I use in the program other than the one I use to call the orogram in main

# 1 I need a function to tell me if any given number is a prime (is_prime),
# 2 then I need a function that returns all primes in a range (calls is_prime) as a list prime_list

#takes a value n and checks to see if it's prime or not
def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if num % n != 0:
                continue
            else:
                return False
        return True
# print(is_prime(18))

#uses is_prime fucntion to return a list of prime numbers when min and max are defined
def list_prime(min, max):
    prime_list = []
    for num in range(min, max):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

