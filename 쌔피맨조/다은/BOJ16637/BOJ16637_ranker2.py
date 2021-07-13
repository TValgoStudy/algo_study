import sys
sys.stdin = open("input2.txt", "r")

N=int(input())
list= list(map(str,input()))
yun=['#']
num=[]

for k in range(N):
    if k%2==0:
        num.append(list[k])
    else:
        yun.append(list[k])
ans=num[0]
maxi=-10000

def call(ans,yun1,ans2,cnt):
    global maxi,yun
    if cnt==N//2+1:
        kk=eval(ans+yun1+ans2)
        if kk>maxi:
            maxi=kk
        return

    if yun1=="":
        yun1=yun[cnt]
        ans2+=num[cnt]
        newans2=str(eval(ans2))
        call(ans,yun1,newans2,cnt+1)
        newans=str(eval(ans+yun1+newans2))
        call(newans,"","",cnt+1)

    else:
        ans2+=yun[cnt]
        ans2+=num[cnt]
        newans2=str(eval(ans2))
        newans=str(eval(ans+yun1+newans2))
        call(newans,"","",cnt+1)

call(ans,"","",1)
print(maxi)