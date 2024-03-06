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
    def __init__(self) -> None:
        pass

    def next_step(self, grid, pos, prev_dir=None):
        pass
        
            
    def isValid(self, grid, pos, dir, empty_count):
        next_x, next_y = self.sum(pos, dir)
        if grid[next_x][next_y] == 1:
            return False
        if grid[next_x][next_y] == 2:
            if empty_count == 0:
                return True
            else:
                return False
        
        return True


    def sum(self, x1, x2):
        return (x1[0] + x2[0], x1[1] + x2[1])
    

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        empty_count = sum(row.count() for row in grid)
        stack = []