"""
https://leetcode.com/problems/guess-number-higher-or-lower/description/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""


class Solution:
    def __init__(self, g_num):
        self.g_num: int = g_num

    def guess(self, num: int) -> int:
        if num == self.g_num:
            return 0
        elif num < self.g_num:
            return 1
        elif num > self.g_num:
            return -1

    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            middle = low + ((high - low)//2)
            # middle = (low + high) // 2
            g = self.guess(middle)
            if g == 0:
                return middle
            elif g == 1:
                low = middle + 1
            elif g == -1:
                high = middle - 1


s = Solution(1702766719)
print(s.guessNumber(2126753390))
