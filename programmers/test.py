answer = 0

def dfs(numbers, target, k):
    global answer
    if k == len(numbers):
        sum = 0

        for i in numbers:
            sum += i

        if sum == target:
            answer += 1

    else:
        numbers[k] *= 1
        dfs(numbers, target, k + 1)
        numbers[k] *= -1
        dfs(numbers, target, k + 1)


def solution(numbers, target):
    dfs(numbers, target, 0)
    return answer

numbers = [4,1,2,1]
target = 4
print(solution(numbers, target))

