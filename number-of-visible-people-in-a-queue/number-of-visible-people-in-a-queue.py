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
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result : List[int] = [0 for person in heights]
        heights_len = len(heights)
        for i in reversed(range(heights_len)):
            for j in range(i+1, heights_len):

                result[i] += 1
                if heights[i] <= heights[j]:
                    break
                
        return result


print(Solution().canSeePersonsCount([10,6,8,5,11,9]))