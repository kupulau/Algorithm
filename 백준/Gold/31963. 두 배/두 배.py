import math
import sys; input = sys.stdin.readline

# 연속된 두 수를 비교하여 조작 횟수를 계산하는 함수
def sol(arr, n):
    tmp = 0  # 총 조작 횟수
    cnt_arr = [0] * n  # 각 인덱스에서의 조작 횟수를 기록하는 배열
    for i in range(1, n):
        # 이전 수를 현재 수로 나눈 비율을 기반으로 필요한 2의 제곱 횟수를 계산
        ratio = math.ceil(math.log2(arr[i - 1] / arr[i])) + cnt_arr[i - 1]
        if ratio > 0:
            cnt_arr[i] = max(0, ratio)  # 조작 횟수 계산
            tmp += cnt_arr[i]  # 총 조작 횟수에 추가
    return tmp  # 최종 조작 횟수 반환

n = int(input())  # 수열의 길이 입력
arr = list(map(int, input().split()))  # 수열의 요소들 입력
print(sol(arr, n))  # 조작 횟수 계산 결과 출력