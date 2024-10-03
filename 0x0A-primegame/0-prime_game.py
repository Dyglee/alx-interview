#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve(max_num)

    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        prime_count = sum(primes[1:num + 1])
        if prime_count % 2 == 0:
            benWinsCount += 1
        else:
            mariaWinsCount += 1

    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif benWinsCount > mariaWinsCount:
        return "Ben"
    else:
        return None


def sieve(n):
    """Sieve of Eratosthenes to find all prime numbers up to n"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime
