def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_height = i
            yellow_width = yellow // i

            if brown == 2 * (yellow_width + yellow_height) + 4:
                brown_height = yellow_height + 2
                brown_width = yellow_width + 2

                return [brown_width, brown_height]

    return answer


num1 = 10
num2 = 2
print(solution(num1, num2))