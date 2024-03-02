from typing import *
import numpy as np

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # handle empty lists
        # print("Test case: ", lists) # debug
        # t1 = time.time_ns() # debug
        if len(lists) == 0:
            return None
        lists = [node for node in lists if node is not None]
        if len(lists) == 0:
            return None
        # preprocess_time = time.time_ns() - t1 # debug

        # sorted_ls = np.array([])
        sorted_ls = []
        lists_processed = 0
        arr = None
        idx_min = None
        # t1 = time.time_ns() # debug
        while True:
            # arr = np.array([node.val if node is not None else np.nan for node in lists])
            # idx_min = np.nanargmin(arr)
            # sorted_ls = np.append(sorted_ls, lists[idx_min])

            arr = [node.val if node is not None else np.nan for node in lists]
            idx_min = np.nanargmin(arr)
            sorted_ls.append(lists[idx_min])
            
            if lists[idx_min].next is None:
                lists[idx_min] = None
                lists_processed += 1
                if lists_processed == len(lists):
                    break
            
            else:
                lists[idx_min] = lists[idx_min].next
        # arr_parse_time = time.time_ns() - t1 # debug

        # map(lambda idx: sorted_ls[idx].next = sorted_ls[idx + 1] if idx + 1 < len(sorted_ls) else None,
        #     range(len(sorted_ls))
        # )

        # t1 = time.time_ns() # debug
        ls_length = len(sorted_ls)
        for i in range(0, ls_length - 1):
            sorted_ls[i].next = sorted_ls[i + 1]

        sorted_ls[-1].next = None
        # format_time = time.time_ns() - t1 # debug

        # print("preprocess: ", preprocess_time)
        # print("arr parse: ", arr_parse_time)
        # print(" + np array none filter")
        # print(" + argmin")
        # print(" + ")
        # print("format: ", format_time)

        return sorted_ls[0]