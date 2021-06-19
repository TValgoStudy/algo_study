import sys
sys.stdin = open("input2.txt", "r")


def cal_func(a, op, b):
    if op == '+': return str(int(a)+int(b))
    elif op == '-': return str(int(a)-int(b))
    elif op == '*': return str(int(a)*int(b))

def func(my_cal, IN):
    global result

    if len(IN) <= 2:
        stack = my_cal + IN
        stack.reverse()
        while len(stack) != 1:
            a, op, b = stack.pop(), stack.pop(), stack.pop()
            stack.append(cal_func(a, op, b))
        final = int(stack[0])
        if result < final:
            result = final
        return

    # 마지막 피연산자는 괄호 묶기 불가능
    for i in range(len(IN)-1):
        # 연산자면 패스
        if IN[i] in '+-*':
            continue

        # 괄호 만들기
        # 피연산자면 해당 부분 () 묶어서 계산
        tmp = cal_func(IN[i], IN[i+1], IN[i+2])
        stack = my_cal + IN[:i] + [tmp] if my_cal else IN[:i] + [tmp]
        # 길이가 1이 될 때까지 반복해서 계산
        stack.reverse()
        while len(stack) != 1:
            a, op, b = stack.pop(), stack.pop(), stack.pop()
            stack.append(cal_func(a, op, b))
        func(stack, IN[i+3:])

        # 괄호 만들지 않기 (이 부분을 안 해서 틀렸었다. state 그래프 생각하면서 풀기)
        stack = my_cal + IN[:] if my_cal else IN[:]
        stack.reverse()
        while len(stack) != 1:
            a, op, b = stack.pop(), stack.pop(), stack.pop()
            stack.append(cal_func(a, op, b))
        func(stack, [])


N = int(input())
IN = list(input())

if len(IN) == 1:
    print(int(IN[0]))
else:
    # 초기값 설정
    stack = IN[:]
    stack.reverse()
    while len(stack) != 1:
        a, op, b = stack.pop(), stack.pop(), stack.pop()
        stack.append(cal_func(a, op, b))
    result = int(stack[0])

    # 함수 실행
    func('', IN[:])
    print(result)