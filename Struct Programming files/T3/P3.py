def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nextPrimeList(n):
        if (n < 0):
            return print("The input should not be a negative number")
        else:
            for num in range(n,101):
                if isprime(num):
                    print ("The first prime greater than the number entered is: ", num)
                    break

n = int(input("Enter a positive integer: "))     
nextPrimeList(n)
