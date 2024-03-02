from typing import List, Optional
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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        
        aux_list : List[ListNode] = [None] * k
        k_i : int = 0
        while head.next != None:
            if k_i == k:
                k_i == 0
                next_chunk = head.next
                for i in range(1, k):
                    aux_list[i].next = aux_list[i-1]
                aux_list[0] = next_chunk
                print(aux_list)
                continue
                
            aux_list[k_i] = head
            k_i += 1
            head = head.next

        return head