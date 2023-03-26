#
# 처음 생각한 정렬 방법
#
# 1 3 5 6 0
#
# 정렬 결과 리스트 index 0을 정하기 위해
# 처음 1을 변수 a에 두고, 주어진 리스트 돌면서 가장 작은 지 확인
#
# 돌면서 작은 애가 있으면 변수 a에 더 작은 숫자를 저장
#
# 끝까지 돌면서 가장 작은 숫자는 정렬 결과 리스트 index 0에 고정
#
# index 1 증가, 변수 a = 0으로 초기화
# index 1의 자리를 정하기 위해 주어진 리스트의 index 1부터 다시 끝까지 돌음
# 가장 작은 숫자를 index 1 자리에 고정
#
# ..
#
# index가 주어진 리스트 길이가 되면 멈추고, 정렬 결과 리스트 반환



inputArr = [1,3,5,6,0]

def suminSort(inputArr):
    arrLen = len(inputArr)
    remainArr = inputArr
    resultArr = []

    for i in range(arrLen):
        minVal = remainArr[0]

        for j in range(i+1, len(remainArr)):
            if remainArr[j] < minVal:
                minVal = remainArr[j]

        resultArr.insert(i, minVal)
        remainArr.remove(minVal)

    return resultArr

print(suminSort(inputArr))



