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
    def isValid(self, state, candidate, depth):
        for i in range(depth): 
            if state[i] == candidate:
                return False
            elif abs(state[i] -  candidate) == abs(i - depth):
                return False
        return True

    def totalNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return 1
        if n == 2:
            return 0
        if n == 3:
            return 0

        sol_count = 0
        stack : List[List[int]] = [[]]
        while stack:
            state = stack.pop()
            depth = len(state)

            if depth == n:
                sol_count += 1

            for candidate in range(n): # candidate search
                if not self.isValid(state, candidate, depth):
                    continue
                next_state = state.copy()
                next_state.append(candidate)
                stack.append(next_state)
        
        return sol_count
    
print(Solution().totalNQueens(4))
print(Solution().totalNQueens(5))
print(Solution().totalNQueens(7))
print(Solution().totalNQueens(9))