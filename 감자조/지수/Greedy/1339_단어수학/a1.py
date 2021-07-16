import sys
sys.stdin = open('input.txt')

n=int(input())
w,r,s=[0]*26,0,9
for i in range(n):
	ii=input()
	for i in range(len(ii)):
		w[ord(ii[i])-ord('A')]+=10**(len(ii)-i-1)
w.sort(reverse=True)
for i in w:
	r,s=r+i*s,s-1
print(r)