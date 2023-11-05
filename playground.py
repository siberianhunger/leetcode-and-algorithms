class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_hash = {}
        for index, num in enumerate(nums):
            num_hash[num] = index

        for index, num in enumerate(nums):
            potential_solution = target - num
            if potential_solution in num_hash and num_hash[potential_solution] != index:
                return [index,  num_hash[potential_solution]]


sol = Solution()
print(sol.two_sum([2, 7, 11, 15], 9))