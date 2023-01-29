from collections import defaultdict

def solution(n, results):
    answer = 0
    wins = defaultdict(set)
    loses = defaultdict(set)

    for winner, loser in results:
        wins[loser].add(winner) # 나를 이긴 사람
        loses[winner].add(loser) # 나에게 진 사람

    for i in range(1, n + 1):
        for winner in wins[i]: # 나를 이긴 애들은 나에게 진 애들도 이김
            loses[winner].update(loses[i]) # 나를 이긴 애들별로 내게 진 사람을 걔들에게도 졌다고 update
        for loser in loses[i]: # 나에게 진 애들은 나를 이긴 애들에게도 짐
            wins[loser].update(wins[i]) # 나에게 진 애들별로 나를 이긴 사람이 걔들에게도 이겼다고 update

    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer
n = 5
edge = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, edge))