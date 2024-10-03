#!/usr/bin/python3


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]

    def count_primes(n):
        return len(sieve(n))

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        prime_count = count_primes(n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
