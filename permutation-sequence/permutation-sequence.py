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

class Solution:
    def __init__(self):
        self.cache : dict = {1 : 1}

    def series(self, n : int):
        if n in self.cache:
            return self.cache[n]
        
        ret = self.series(n-1) + n
        self.cache[n] = ret
        return ret
    

    def getPermutation(self, n: int, k: int) -> str:
        permu_list = []
        temp_k = k
        for i in reversed(range(1, n+1)):
            s_i = self.series(i)
            permu_list.append(temp_k // s_i)
            temp_k = temp_k % s_i

        sol = ""
        chosen : List[bool] = [False for i in permu_list] # 1 if chosen, 0 if not
        for i in range(n): # loop through permu_list
            empty_count = 0
            for j in range(n): # loop through chosen
                if chosen[j]:
                    continue
                
                if empty_count == permu_list[i]:
                        chosen[j] = True
                        sol = sol + str(j)
                        break
                empty_count += 1
                    

                # while temp_idx < permu_list[i]:
                #     if chosen[temp_idx]:
                #         temp_idx += 1

            # while pos in chosen: # TODO: fix result printing
            #     pos += 1
            # chosen.add(pos)
            # sol = sol + str(pos)
        print(permu_list)
        return sol
    
print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(4, 2))