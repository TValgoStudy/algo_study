# 10830 행렬 제곱



## 다른 사람 풀이

https://hooongs.tistory.com/114

```python
import sys
sys.stdin = open('input.txt')

# 두 행렬의 곱을 구하는 함수
def multiply(matrix_1, matrix_2):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
            result[i][j] %= 1000
    return result

def devide(B, matrix):
    if B == 1:
        return matrix
    elif B == 2:
        return multiply(matrix, matrix)
    else:
        tmp = devide(B//2, matrix)
        if B % 2 == 0: # B가 짝수면
            return multiply(tmp, tmp)
        else: # B가 홀수면
            return multiply(multiply(tmp, tmp), matrix)


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = devide(B, A)
for i in range(N):
    for j in range(N):
        print(answer[i][j]%1000, end=" ")
    print()
```



## 알아둬야 할 것

1. 행렬의 곱 구하는 방법

```python
def multiply(matrix_1, matrix_2):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
```

2. 숫자가 매우 큰데 계산이 단순하면 분할 정복을 이용하여 시간을 단축할 수 있음.

   예를 들어 보면, B = 14인 경우

   14

   7

   3

   1

   devide(1, matrix) => return matrix => tmp = matrix

   이제 다시 B를 확인하면 홀수(3)이므로 (tmp 곱 tmp 곱 matrix) 를 하면 matrix 세제곱이 나오게 됨

   이제 다시 B를 확인하면 홀수(7)이므로 다시 (tmp 곱 tmp 곱 matrix)를 하면 matrix 7제곱이 나옴

   이제 다시 B를 확인하면 짝수(14)이므로 (tmp 곱 tmp)를 하여 matrix 14제곱이 나옴

==> 14 - 7 - 3 - 1 - 3 - 7 - 14 분해 후 재조립하는 느낌??





