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
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sol = 0
        satis_factor = 0

        for dish in sorted(satisfaction, reverse=True):
            satis_factor += dish
            if satis_factor < 0:
                return sol
            sol += satis_factor
        return sol
    
print(Solution().maxSatisfaction([-1,-8,0,5,-9]))
