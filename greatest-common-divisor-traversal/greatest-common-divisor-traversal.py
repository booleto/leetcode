from typing import List
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

## Union Find class
class UnionFind:
    def __init__(self, n : List[int]) -> None:
        self.find_time : int = 0
        self.t1 : int = 0
        self.init_time : int = 0
        self.find_time : int = 0
        self.union_time : int = 0
        self.gcd_time : int = 0

        self.t1 = time_ns()
        self.parent = list(range(n))
        self.size = [1] * n
        self.groups = n
        self.init_time = time_ns() - self.t1
    
    def find(self, a : int):
        self.t1 = time_ns()
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        self.find_time = time_ns() - self.t1
        return self.parent[a]

    def union(self, a, b):
        self.t1 = time_ns()
        rep_a = self.find(a)
        rep_b = self.find(b)

        if rep_a == rep_b: # same group
            return
        
        size_a = self.size[rep_a]
        size_b = self.size[rep_b]

        ## by size
        if size_a < size_b:
            # self.parent[a] = rep_b
            self.parent[rep_a] = rep_b
            self.size[rep_b] += size_a
        else:
            # self.parent[b] = rep_a
            self.parent[rep_b] = rep_a
            self.size[rep_a] += size_b
        self.groups -= 1
        self.union_time += time_ns() - self.t1

        ## by rank
        # if self.size[rep_a] > self.rank[rep_b]:
        #     self.parent[rep_b] = rep_a
        # elif self.rank[rep_a] < self.rank[rep_b]:
        #     self.parent[rep_a] = rep_b
        # else:
        #     self.parent[rep_b] = rep_a
        #     self.rank[rep_a] += 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        t1 = time_ns()
        num_len = len(nums)
        unvisited = [True] * num_len
        unvisited[0] = False
        visited = [0]
        # uni = UnionFind(num_len)

        for i in visited:
            for j in range(1, num_len):
                # uni.t1 = time_ns()
                if not unvisited[j]:
                    continue
                if gcd(nums[i], nums[j]) > 1:
                    # uni.union(i, j)
                    visited.append(j)
                    unvisited[j] = False
                # uni.gcd_time = time_ns() - uni.t1

        print("time:", time_ns() - t1)
        # print("init time: ", uni.init_time)
        # print("find time: ", uni.find_time)
        # print("union time: ", uni.union_time)
        # print("gcd time: ", uni.gcd_time)
        # return uni.groups == 1
        return len(visited) == num_len


## Stack DFS implementation
# class Solution:
#     def canTraverseAllPairs(self, nums: List[int]) -> bool:
#         num_len = len(nums)
#         unvisited = set(range(num_len))
#         stack = [0]
#         print(sys.getsizeof(unvisited))

#         while stack:
#             node = stack.pop()
#             if node not in unvisited:
#                 continue
#             unvisited.discard(node)
#             for idx in unvisited:
#                 if gcd(nums[node], nums[idx]) > 1:
#                     stack.append(idx)
            
        
#         return len(unvisited) == 0



# print(Solution().canTraverseAllPairs([49,39,20,30,28,35,26,16,10,44]))
# print(Solution().canTraverseAllPairs([2,3,6]))
print(Solution().canTraverseAllPairs([4,3,12,8]))
print(Solution().canTraverseAllPairs([39,35,50,21,42,44,42]))
print(Solution().canTraverseAllPairs([13,75,30,80,40,90,65]))
print(Solution().canTraverseAllPairs([19999 for i in range(100000)]))
