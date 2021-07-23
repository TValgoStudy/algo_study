### 내 풀이

1. 해설, 포인트

   - 이건 좀 노답인게, C++도 제일 빠른게 820ms고 python으로 통과한 사람 없음
   - 처음에 생각했던 s1 방법이 c++에서는 통하는 방법이었지만, 파이썬으로는 안됨
        - ABCD를 AB합/CD합으로 나누어 구하고 이진탐색을 시도
   - 안되서 블로그 참고, 굳이 이진 탐색 할 필요 X
   - AB합 구한후, CD 합을 반복문으로 구하면서 dict에 동일한 값이 있다면 그때의 value들을 더하면 됨
   - value 전체를 구하는건 중복된 값을 내는 서로 다른 조합이 있고, 이건 서로 다른 경우로 치기 때문  

2. 실행시간

   - pypy : 11056ms

3. 코드

   ```python
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    A, B, C, D = [], [], [], []
    answer = 0
    
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    
    total = {}
    for a in A:
        for b in B:
            total[a+b] = total.get(a+b, 0) + 1
    
    for c in C:
        for d in D:
            answer += total.get(-(c+d), 0)
    
    print(answer)

   ```

<br/>




### 다른 사람의 풀이

1. 실행시간

   - 5788ms

2. 코드

   ```python
    import sys
    input = sys.stdin.readline
    n = int(input())
    
    mat = [[0] * 4 for _ in range(n)]
    for _ in range(n):
        a, b, c, d = map(int,input().split())
        mat[_][0] = a
        mat[_][1] = b
        mat[_][2] = c
        mat[_][3] = d
    
    a_list = [0] * (n * n)
    b_list = [0] * (n * n)
    
    for i in range(n):
        for j in range(n):
            a_list[n * i + j] = mat[i][0] + mat[j][1]
            b_list[n * i + j] = mat[i][2] + mat[j][3]
    
    a_list.sort()
    b_list.sort()
    
    s = 0
    e = n*n-1
    res = 0
    while s <= n*n-1 and e >= 0:
        temp = a_list[s] + b_list[e]
        if temp == 0:
            left_cnt = 0
            for i in range(s, n*n):
                if a_list[i] == a_list[s]:
                    left_cnt += 1
                else:
                    break
    
            right_cnt = 0
            for i in range(e, -1, -1):
                if b_list[i] == b_list[e]:
                    right_cnt += 1
                else:
                    break
            res += left_cnt * right_cnt
            s += left_cnt
            e -= right_cnt
        elif temp > 0:
            e -= 1
        else:
            s += 1
    print(res)

   ```

3. 해설

   - AB합/CD합 구한 후 각각 오름차순 정렬
   - AB는 작은것부터, CD는 큰것부터 서로 더해가기 시작
   - 더한값이 0보다 크면 CD index를 내리고, 0보다 작으면 AB index를 올림
   - 더한값이 0이라면 중복값의 갯수를 찾아서 모두 더함