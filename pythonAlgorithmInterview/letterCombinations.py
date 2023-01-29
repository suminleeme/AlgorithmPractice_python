#leetcode 17. Letter Combinations of a Phone Number
from typing import List

class Solution:
    def letterCombinations(self, digits:str) -> List[str]:
        def dfs(index, path):
            # digits 숫자 끝까지 탐색해서 조합을 만들었으면, result에 추가한다.
            if len(path) == len(digits):
                result.append(path)
                return

            # 지금 숫자 자리에서 만든 조합 path를 가지고, 다음 숫자 자리를 탐색한다. (index 안넣으면 같은 숫자별 알파벳 내끼리도 매핑된다.)
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)

        if not digits:
            return []

        # 숫자별 문자 리스트 dict를 만든다.
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        # 반환할 조합 결과 리스트 result를 만든다.
        result = []

        # 숫자별로 연결된 문자 조합을 digits 전체 숫자만큼 탐색하면서 만든다.
        dfs(0, "")

        return result

solution = Solution()
print(solution.letterCombinations("23"))