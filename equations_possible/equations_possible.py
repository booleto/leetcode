### Comment out on leetcode
from typing import *
###


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # consts
        LHS = 0
        RHS = 3
        SIGN = 1

        sets : set[set] = {}
        diffs : list[set] = {}

        for expr in equations:
            if expr[SIGN] == "=":


            if expr[SIGN] == "!":
                diffs.append(expr)


    def sets_register(self, sets : set[set], elements : set[str]) -> None:
        for setmem in sets:
            # union = 0
            if setmem.isdisjoint(elements):
                continue

            # union = 1
            intersect = setmem.intersection(elements)
            if 
            

    # def set_join(self, sets : set[set], ):

