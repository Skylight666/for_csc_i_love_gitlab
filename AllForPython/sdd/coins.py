
from functools import reduce, lru_cache

@lru_cache(maxsize=None)
def nways_recursive(total, coins):
    """Return how many different ways `total` can be made from `coins`."""
    if not coins: # no coins left
        return (total == 0) # if total is zero; we found a way to make it
    # enumerate all possible ways `first(coins)` can be used to make `total`
    return sum(nways_recursive(total - amount, rest(coins))
               for amount in range(0, total+1, first(coins)))

goal = 200
coins = [1, 2, 5, 10, 20, 50]

# use a linked list to get O(1) first() and rest() operations
coins_list = reduce(lambda lst, x: (x, lst), reversed(coins), None)
# -> (1, (2, (5, (10, (20, (50, (100, (200, None))))))))
first = lambda lst: lst[0]
rest = lambda lst: lst[1]

print(nways_recursive(goal, coins_list))
print(nways_recursive.cache_info())

# iterative solution
# http://stackoverflow.com/q/20353226
nways = [1] + [0] * goal
for c in coins:
    for total in range(1, len(nways)): # all sums
        if c <= total:
            nways[total] += nways[total - c]
print(nways[goal])
