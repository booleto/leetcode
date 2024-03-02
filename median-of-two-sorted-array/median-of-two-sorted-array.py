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

from statistics import median
from math import ceil


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 == 0:
            return median(nums2)
        if len2 == 0:
            return median(nums1)

        nums_len = len1 + len2
        idx1 = 0
        idx2 = 0
        prev1 = 0
        prev2 = 0
        for i in range(nums_len // 2 + 1):
            prev2 = prev1
            if idx1 < len1 and idx2 < len2:
                if nums1[idx1] < nums2[idx2]:
                    prev1 = nums1[idx1]
                    idx1 += 1
                else:
                    prev1 = nums2[idx2]
                    idx2 += 1
            elif idx1 == len1:
                prev1 = nums2[idx2]
                idx2 += 1
            elif idx2 == len2:
                prev1 = nums1[idx1]
                idx1 += 1
        
        if (len1 + len2) % 2 == 1:
            return prev1
        else:
            return (prev1 + prev2) / 2

        # [0, 1, 2, 3, 4]
        # [0, 1, 2, 3]

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
print(Solution().findMedianSortedArrays([1, 3], [2]))

