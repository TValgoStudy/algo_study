import sys
sys.stdin = open('input.txt')

L = int(sys.stdin.readline())
ad = sys.stdin.readline().rstrip()

# ad안에 특정 패턴이 발견된다면 패턴의 길이가 정답
# ad아네 패턴이 발견되지 않고 잘린다면, 예를 들어 abcda 이런식으로
# 이렇게 되면 abcda가 광고문구일수도 있고, abcd가 문구 일 수 도 있음
# abaca 라면? 광고문구가 abaca일수도 abac일수도 있음
# abcde 라면? abcde가 최소


def findPattern():
    pattern = ''

    for i in range(len(ad)):
        if pattern and pattern[0] == ad[i]: # 같은 문자열이 나온 경우
            m = len(ad) - i
            p = len(pattern)
            if pattern * (m // p) + pattern[:m%p] == ad[i:]:  # 뒷부분이 모두 동일한 경우
                return len(pattern)

        pattern += ad[i]

    return len(pattern)


print(findPattern())

