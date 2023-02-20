from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidateList = candidates[:]
        prev_elements = []

        # 주어진 candidate 리스트 내에서 가능한 모든 중복포함 조합
        # 에서 합이 target과 일치하면 results에 추가

        def listSum(elements):
            sum = 0
            for e in elements:
                sum += e
            return sum

        def dfs(elements, target):
            if len(elements) == len(candidates) + 1:
                return

            for e in elements:
                prev_elements.append(e)

                if listSum(prev_elements) == target:
                    results.append(prev_elements)

                next_elements = elements[:]
                next_elements.remove(e)

                dfs(next_elements, target)

                prev_elements.pop()

        dfs(candidateList, target)
        return results


solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))