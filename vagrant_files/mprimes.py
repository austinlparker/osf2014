import time

def main():
        n = 1
        start = time.time()
        while True:
                if mersenneIsPrime(n):
                        print "M" + str(n) + "=" + str(mersenne(n))
                        elapsed = time.time() - start
                        print "\tfound in %.5fs" % elapsed
                        print ""
                n = n + 1

def mersenne(n):
        return 2 ** n - 1

def mersenneIsPrime(n):
        if not simpleIsPrime(n):
                return False
        if n == 1:
                return False
        if n == 2:
                return True
        m = mersenne(n)
        x = 4
        for i in range(n-2):
                x = (x * x - 2) % m
        return x == 0

def simpleIsPrime(n):
        if n == 1:
                return False
        div = 2
        while div * div <= n:
                if n % div == 0:
                        return False
                div = div + 1
        return True

main()