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
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        empty_count = sum(row.count() for row in grid)