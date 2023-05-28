class Solution:
    """
    1. Initialize a list of booleans of size n and set all values to True
    2. Set the first and second values to False
    3. Initialize a variable p to 2
    4. While p * p < n
        a. If is_prime[p] is True
            i. Iterate through the list from p * p to n with a step of p
                1. Set is_prime[i] to False
        b. Increment p by 1
    5. Return the sum of is_prime
    """
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        #   Start from the first prime number 2
        p = 2

        #   Sieve of Eratosthenes algorithm
        while p * p < n:
            if is_prime[p]:
                for i in range(p * p, n, p):
                    is_prime[i] = False
            p += 1

        return sum(is_prime)
