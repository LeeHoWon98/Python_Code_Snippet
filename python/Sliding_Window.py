#리스트 안에 일정한 인덱스 만큼을 더해 최대값을 찾는 문제
numbers = list(map(int, input().split()))
n = int(input())

window = sum(numbers[:n])
result = window

for i in range(n, len(numbers)):
    window += numbers[i] - numbers[i - n]
    result = max(result, window)

print(result)