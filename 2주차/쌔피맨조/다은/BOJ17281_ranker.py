import sys
from itertools import permutations
sys.stdin = open('input.txt')

if __name__ == "__main__":
    n = int(sys.stdin.readline())  # 이닝 수
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    people = [1, 2, 3, 4, 5, 6, 7, 8]
    answer = 0
    for turn in permutations(people, 8):
        turn = list(turn)
        turn = turn[:3] + [0] + turn[3:]
        score = 0
        index = 0
        for inning in range(1, n + 1):
            out_cnt = 0  # 아웃 카운트
            base_1, base_2, base_3 = 0, 0, 0  # 1, 2, 3루 주자
            while out_cnt < 3:
                if data[inning - 1][turn[index]] == 0:
                    out_cnt += 1
                elif data[inning - 1][turn[index]] == 1:
                    score += base_3
                    base_1, base_2, base_3 = 1, base_1, base_2
                elif data[inning - 1][turn[index]] == 2:
                    score += (base_2 + base_3)
                    base_1, base_2, base_3 = 0, 1, base_1
                elif data[inning - 1][turn[index]] == 3:
                    score += (base_1 + base_2 + base_3)
                    base_1, base_2, base_3 = 0, 0, 1
                elif data[inning - 1][turn[index]] == 4:
                    score += (base_1 + base_2 + base_3 + 1)
                    base_1, base_2, base_3 = 0, 0, 0
                index += 1
                if index == 9:
                    index = 0
        answer = max(answer, score)  # (타자 순서, 현재 타자 번호, 득점)
    print(answer)

from itertools import permutations as p

u = input
n=int(u())
a=0
I=[[*map(int,u().split())]for _ in'a'*n]

for l in p(range(1,9),8):
    l=list(l);
    l.insert(3,0);
    c=0;s=0
    for i in I:
        out=0;
        x,y,z=0,0,0
        while out<3:
            k=i[l[c]]
            if k==0:out+=1
            if k==1:s+=z;x,y,z=1,x,y
            if k==2:s+=y+z;x,y,z=0,1,x
            if k==3:s+=x+y+z;x,y,z=0,0,1
            if k==4:s+=x+y+z+1;x,y,z=0,0,0
            c=(c+1)%9
    a=max(a,s)
print(a)