class Primes:
    
    def __init__(self, max):
        self.max = max
        self.number = 1
    
    def __iter__(self):
        return self
    
    def check_prime(self, number):
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                return False
        return True

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif self.check_prime(self.number):
            return self.number
        else:
            return self.__next__()

def main():
    primes = Primes(10000)
    print(primes)
    for x in primes:
        print(x)

if __name__ == "__main__":
    main()