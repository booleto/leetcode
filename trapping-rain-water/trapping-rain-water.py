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
    # def trap(self, height: List[int]) -> int:
    #     total_rain = 0
    #     stack : List[int] = []
    #     count = len(height)
    #     stack.append(0)
    #     prev = 0

    #     for i in range(1, count):
    #         prev = None
    #         while len(stack) > 1: #TODO: AAAAAAAAAAAAAAAAAAAAAAAA
    #             if height[i] < height[stack[-1]]:
    #                 break

    #             if height[i] < height[stack[-2]]:
    #                 total_rain += (height[i] - height[stack[-1]]) * (i - stack[-2] - 1)
    #                 stack.pop()
    #                 continue
                
    #             total_rain += (height[stack[-2]] - height[stack[-1]]) * (i - stack[-2] - 1)
    #             stack.pop()
    #         else:
    #             if not stack:
    #                 stack.append(i)
    #                 continue


    #             if height[stack[-1]] <= height[i]:
    #                 total_rain += abs(height[stack[-1]] - height[i]) * (i - stack[-1] - 1)
    #                 stack.clear()
    #             stack.append(i)
    #             continue

    #         stack.append(i)

        # return total_rain
    def getRainAt(self, i: int, height: List[int], stack: List[int], prev : int) -> int:
        rain = 0
        while len(stack) > 0:
            if height[stack[-1]] > height[i] and prev == None:
                stack.append(i)
                break

            if height[stack[-1]] > height[i] and prev != None:
                rain += (height[i] - height[prev]) * (i - stack[-1] - 1)
                prev = None
                stack.append(i)
                break

            if height[stack[-1]] < height[i] and prev != None:
                rain += (height[stack[-1]] - height[prev]) * (i - stack[-1] - 1)
                prev = stack.pop()
                continue

            if height[stack[-1]] < height[i] and prev == None:
                prev = stack.pop()
                # stack.append(i)
                continue

            if height[stack[-1]] == height[i] and prev == None:
                stack.pop()
                stack.append(i)
                break

            if height[stack[-1]] == height[i] and prev != None:
                rain += (height[i] - height[prev]) * (i - stack[-1] - 1)
                stack.pop()
                stack.append(i)
                break
        else:
            stack.append(i)
        
        return rain
    

    
    def trap(self, height: List[int]) -> int:
        total_rain = 0
        stack : List[int] = []
        prev = None
        count = len(height)

        stack.append(0)

        for i in range(1, count):
            prev = None
            total_rain += self.getRainAt(i, height, stack, prev)

        return total_rain
                    

# print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(Solution().trap([4,2,0,3,2,5]))
# print(Solution().trap([1,2,3,4,5,5]))
print(Solution().trap([5,2,1,2,1,5]))
        