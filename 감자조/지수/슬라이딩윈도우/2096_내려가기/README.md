### 내 풀이

1. 이렇게 푼 이유?

   - 슬라이딩 윈도우는 모르겠고, 프로그래머스의 땅따먹기였나 그 DP문제랑 똑같아서 DP로 접근
   - 처음에 풀때는 DP배열을 3*n짜리로 만들었다가 메모리 초과
   - 그래서 DP배열을 길이가 3인 일차원 배열로 만들어서 반복문에 들어가면 a,b,c라는 변수로 기존 값을 임시 지정해둠.
   - 근데 그래도 메모리 초과나서 인풋도 따로 밖에서 안받고 반복문 안에서 받으니까 통과!
   
2. 실행시간

   - 4624ms (python)

3. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   # 4624ms
   N = int(input())
   
   for i in range(N):
       x, y, z = map(int, input().split())
   
       if i == 0:
           minArr = [x, y, z]
           maxArr = [x, y, z]
           continue
   
       a, b, c = minArr
       minArr[0] = x + min(a, b)
       minArr[1] = y + min(a, b, c)
       minArr[2] = z + min(b, c)
   
       a, b, c = maxArr
       maxArr[0] = x + max(a, b)
       maxArr[1] = y + max(a, b, c)
       maxArr[2] = z + max(b, c)
   
   
   print(max(maxArr), min(minArr))
   ```



### 다른 사람의 풀이

1. 실행시간

   - 292ms

2. 코드

   ```python
   import sys
   
   N = int(sys.stdin.readline().rstrip())
   max_ = [0]*3
   min_ = [0]*3
   
   for i in range(N):
       a, b, c = map(int, sys.stdin.readline().rstrip().split())
   
       max_[0], max_[1], max_[2] = max_[0]+a if max_[0]>max_[1] else max_[1]+a, max(max_)+b, max_[1]+c if max_[1]>max_[2] else max_[2]+c
       min_[0], min_[1], min_[2] = min_[0]+a if min_[0]<min_[1] else min_[1]+a, min(min_)+b, min_[1]+c if min_[1]<min_[2] else min_[2]+c
       
   print(max(max_), min(min_))
   ```
   
3. 해설

   - 완전 똑가고 min max 대신 조건문으로 구한거?
   - 단 저걸 한줄이 아니라 서로 다른 줄로 할 경우에 max[0]이 바뀌는게 그 아래 max[1]이나 2에 영향을 주는데, 저렇게 한줄로 구현하면 저 한줄이 진행될 동안 우항에 있는 max는 그대로 있는 듯함.



### 슬라이딩 윈도우

슬라이딩 윈도우는 부분합을 구하는 상황등에서 자주 쓰인다. 부분합을 구할때 매번 슬라이싱이나 반복문으로 새로 합을 구할 필요가 없이, 이동한 만큼 추가된 영역은 더해주고, 범위에서 벗어난 부분만 빼줌으로써 연산수를 줄이는 알고리즘이다.

![서브배열의 공통된 요소 예시](https://blog.fakecoding.com/content/images/wordpress/2020/07/xScreen-Shot-2020-07-21-at-18.47.22.png.pagespeed.ic.l6N19VxvDW.webp)

출처 : https://blog.fakecoding.com/archives/algorithm-slidingwindow/