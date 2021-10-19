import sys
sys.stdin = open('input.txt')

input_data = int(input())
five = int(input_data / 5)
bag = 0
for i in range(five, -1, -1):
    three = (input_data - 5 * i) / 3
    if three == int(three):
        bag = three + i
        break
if bag == 0:
    print(-1)
else:
    print(int(bag))