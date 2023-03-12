#!/usr/bin/python3
""" choosing a prime number from the set and removing number and its multiples from the set
"""


def isWinner(x, nums):
    """Determines the winner of a prime game with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    k = max(nums)
    primes = [True for _ in range(1, k + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, k + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than k in nums for each round
    for _, k in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: k])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
