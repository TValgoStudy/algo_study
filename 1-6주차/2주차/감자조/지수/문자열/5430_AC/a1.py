import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(int(input())):
    # 명령어 입력
    cmd = input().rstrip()
    # 배열(리스트)의 길이
    length = int(input())
    # 길이가 양수라면, 숫자만 뽑아서 li에 저장
    if length:
        li = list(input()[1:-2].split(','))
    # 길이가 0이하라면 li를 빈 리스트로 초기화
    else:
        _ = input()
        li = []

    # 명령어에서 D가 나오는 횟수 계산
    Dcount = cmd.count('D')
    # 배열의 총 길이보다 크다면 error 출력
    if Dcount > length:
        print('error')
    # 배열길이와 같다면 [] 출력
    elif Dcount == length:
        print('[]')
    else:
        # R을 기준으로 명령어 잘라서 Dlist에 연결된 D들의 길이를 저장
        Dlist = list(map(len, cmd.split('R')))
        # 왼쪽에서 잘라낼 개수
        popLeft = sum(Dlist[0::2])
        # 오른쪽에서 잘라낼 개수
        popRight = sum(Dlist[1::2])

        if popRight:
            li = li[popLeft:-popRight]
        # 오른쪽에서 하나도 뽑지 않아서 popRight가 0일 경우
        else:
            li = li[popLeft:]

        # R이 홀수개 였을 경우 마지막에 한번 리스트 뒤집음
        if len(Dlist) % 2 == 0:
            li.reverse()

        # 출력
        print('[' + ','.join(li) + ']')