n=int(input())
t=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
s1=t*t
s2=rev*rev
s=str(s2)
if str(s1)==s[::-1]:
    print("True")
else:
    print("False")

    