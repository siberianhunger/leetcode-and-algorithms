class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        for i in strs:
            if i[0] != strs[0][0]:
                return ""
        prefix = strs[0][0]
        for index, item in enumerate(strs):
            for letter_num in range(len(item)):
                if (
                        index < len(strs) - 1 and
                        len(strs[index + 1]) > letter_num > len(prefix) and
                        item[letter_num] == strs[index + 1][letter_num]
                ):
                    prefix = item[:letter_num]
        return prefix


strs = [
    "flower",
    "flow",
    "flight"
]

print(Solution().longestCommonPrefix(strs))
