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
        
        # aux_list : List[ListNode] = [None] * k
        # k_i : int = 0
        # while head.next != None:
        #     if k_i == k:
        #         k_i = 0
        #         next_chunk = head.next
        #         for i in range(1, k):
        #             aux_list[i].next = aux_list[i-1]
        #         aux_list[0] = next_chunk
        #         print(aux_list)
        #         continue
                
        #     aux_list[k_i] = head
        #     k_i += 1
        #     head = head.next

        # return head

        # prev = head
        # head = head.next
        # tail = None
        # index = 0

        # while head.next != None:
        #     index += 1
        #     if index % k == 0: # batch head
        #         head.next = None
        #         tail = head
        #         prev = head
        #         head = head.next
        #     elif index % k == k-1: # batch tail
        #         tail.next = head
        #         prev = head
        #         head = head.next
        #     else:  # batch mid
        #         prev = head
        #         head = head.next
        #         head.next
                
        prev = head
        head = head.next
        prev_batch_head = None
        batch_tail = prev
        batch_head = None
        index = 1

        while head.next != None:
            index += 1
            if index % k == 0: # batch head
                batch_head = head
                prev2 = prev
                prev = head
                head = head.next
                continue

            if index % k == k-1: # batch tail
                # set batch tail path
                batch_tail = head
                if prev_batch_head != None:
                    prev_batch_head.next = batch_tail

                # set batch path
                next_batch = head.next
                head.next = prev
                batch_head.next = next_batch
                head = next_batch
                continue

            next_node = head.next
            next_node.next = head
            head = next_node

        return head

   
    
def listToLinked(ls : List[int]):
    head = ListNode()
    prev = head
    prev.val = ls[0]
    for num in ls:
        node = ListNode()
        node.val = num
        prev.next = node
        prev = node
    return head

test_cases = [
    ([1,2,3,4,5], 2),
    ([1,2,3,4,5], 3)
]

for test, k in test_cases:
    head = listToLinked(test)
    sol = Solution().reverseKGroup(head, k)
    
    print("Test case ", test, ": ")
    while sol.next:
        print(sol, end=' ')


