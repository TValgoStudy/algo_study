### 내 풀이

1. 실행시간

   - 896ms

2. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   # 폭발 연쇄 가능
   # 남은 문자 리턴, 없을 경우 FRULA 리턴
   
   # 스택 사용
   # 896ms 성공!
   
   text = input()
   bomb = input()
   
   T = len(text)
   B = len(bomb)
   
   stack = [''] * T
   si = 0
   
   for ti in range(T):
       stack[si] = text[ti]
   
       if si < B - 1:
           si += 1
           continue
   
       for ri in range(B):
           if stack[si-ri] != bomb[B-ri-1]:
               break
       else:
           si -= B
   
       si += 1
   
   if si:
       print(''.join(stack[:si]))
   else:
       print('FRULA')
   ```

3. 해석
   - 처음엔 replace로 해봤더니 역시 시간 초과
   - 이런 터지는 류의 문제는 프로그래머스에서 인형뽑기? 에서 스택 썻던 방법이 생각나서 스택으로 접근
   - 스택도 팝 쓰면 시간 너무 오래걸릴 거같아서 초기 문자열 길이만큼으로 고정하고 인덱스 접근
   - 하나씩 스택에 넣으면서, 폭발 단어가 있는지 체크 하고 있는 경우 폭발
     - 여기서 폭발은 팝이 아니라, 인덱스를 이전으로 돌리는 것으로 간단히 해결



### 다른 사람의 풀이

1. 실행시간

   - 56ms

2. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   def main():
       string = input().strip()
       bomb = input().strip()
       bombl = list(bomb)
       b_last = bomb[-1]
       bl = len(bomb)
   
       ans = []
       for l in string:
           ans.append(l)
           if b_last == l and bombl == ans[-bl:]:
               del ans[-bl:]
   
       print(''.join(ans) if ans else "FRULA")
   
   
   if __name__ == '__main__':
       main()
   ```
   
3. 해설

   - ?!?! 스택 쓰는건 같은데 왜 del이 이렇게나 빠르지!
   - 스택에 새로운 알파벳 하나씩 추가
   - 만약 폭발문자열의 마지막 문자와 새로 추가한 문자가 같고, 뒤에 있는 문자가 폭발 문자열과 같으면 del로 삭제
   - `pop`은 사실상 길이만큼 팝팝팝팝 여러번 해야하고, 할때마다 새로운 리스트를 만드는데, `del`은 지정한 범위(여기서는 [-bl:] 를 한번에 삭제하는거라서 빠른 듯)

