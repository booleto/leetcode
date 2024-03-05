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
import copy as cp


# class Solution:
#     def isValid(self, state : List, pos, candidate):
#         if candidate in state[pos[0]]:
#             return False
        
#         if candidate in [state[i][pos[1]] for i in range(9)]:
#             return False
        
#         r_start = pos[0] // 3 * 3
#         r_end = r_start + 3
#         c_start = pos[1] // 3 * 3
#         c_end = c_start + 3

#         if candidate in [state[r][c] for r in range(r_start, r_end) for c in range(c_start, c_end)]:
#             return False
        
#         return True
    

#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """

#         board_int = [[0 for i in range(9)] for j in range(9)]
#         empty_cells = 0
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == '.':
#                     board_int[r][c] = 0
#                     empty_cells += 1
#                 else:
#                     board_int[r][c] = int(board[r][c])
                

#         # Stack backtracking
#         stack = [(board_int.copy(), (0, 0), empty_cells)]
#         while stack:
#             state, pos, empt  = stack.pop()

#             if empt == 0:
#                 board_int = state
#                 break

#             # candidate search
#             for r in range(pos[0], 9):
#                 for c in range(pos[1], 9):
#                     if state[r][c] != 0:
#                         continue

#                     # Contraints checking
#                     for candidate in range(1, 10):
#                         if self.isValid(state, [r, c], candidate):
#                             state[r][c] = candidate
#                         stack.append((state.copy(), (r, c), empt - 1))

#         print(board_int)

class Solution:
    def nextEmpty(self, board_int, pos):
        for i in range(pos[0]*9 + pos[1], 9*9):
            if board_int[i // 9][i % 9] == 0:
                return (i //9, i % 9)

        return (-1, -1)
    

    def isValid(self, board_int : List, pos, candidate):
        if candidate <= 0 or candidate >= 10:
            return False

        if candidate in board_int[pos[0]]:
            return False
        
        if candidate in [board_int[i][pos[1]] for i in range(9)]:
            return False
        
        r_start = pos[0] // 3 * 3
        r_end = r_start + 3
        c_start = pos[1] // 3 * 3
        c_end = c_start + 3

        if candidate in [board_int[r][c] for r in range(r_start, r_end) for c in range(c_start, c_end)]:
            return False
        
        return True
    

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        board_int = [[0 if board[i][j] == '.' else int(board[i][j]) for j in range(9)] for i in range(9)]
                

        # Stack backtracking
        stack = [(board_int[0][0], (0, 0))]
        while stack:
            state, (row, col) = stack[-1]
            board_int[row][col] = state

            # cell search
            next_row, next_col = self.nextEmpty(board_int, (row, col))
            if next_row == -1:
                break
            

            for candidate in range(1, 10): # pick first candidate of next cell
                if self.isValid(board_int, (next_row, next_col), candidate):
                    stack.append((candidate, (next_row, next_col)))
                    break
            else: # if no candidates found, backtrack
                while True:
                    candidate, (row, col) = stack.pop() # backtrack
                    board_int[row][col] = 0

                    for candidate in range(candidate + 1, 10): # get new candidate for current cell
                        if self.isValid(board_int, (row, col), candidate):
                            stack.append((candidate, (row, col)))
                            break
                    else:
                        continue
                    break
                    # if no candidates, further backtrack


        # Save results
        for r, row in enumerate(board_int):
            for c, cell in enumerate(row):
                board[r][c] = str(board_int[r][c])

        print(board)


Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
