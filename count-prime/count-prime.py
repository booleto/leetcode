from typing import *
from collections import *
import itertools
import functools
from math import *
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

import sys
from time import time_ns


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        
        sieve = [False for i in range(n)]
        count = n - 2
        for divisor in range(2, int(sqrt(n)) + 1):
            for number in range(divisor**2, n, divisor):
                if sieve[number]:
                    continue
                # if number % divisor == 0 and number // divisor != 1:
                sieve[number] = True
                count -= 1
        # print(sieve)
        return count


# print(Solution().countPrimes(10))
# print(Solution().countPrimes(20))

t1 = 0
delta = 0
delta_sum = 0
iters = 100
for i in range(iters):
    t1 = time_ns()
    Solution().countPrimes(1990)
    delta = time_ns() - t1
    delta_sum += delta

print("Average runtime: ", delta_sum / iters)
