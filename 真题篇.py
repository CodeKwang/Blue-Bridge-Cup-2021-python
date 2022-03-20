# 4.1不同子串
'''
s = '0100110001010001'
sep = 1
num = 1
v = []
while sep < len(s):
    v.append(s[0:sep])
    for i in range(len(s)-sep):
        if s[i+1:i+sep+1] in v:
            continue
        else:
            v.append(s[i+1:i+sep+1])
    sep +=1
    num += len(v)
    v = []
print(num)
'''
# 4.2年号字串
'''
n=2019
while n>0:
    t = n%26
    n = int(n/26)
    print(chr(ord('A')+t-1),end='')
print()
'''
# 4.3数列求值
'''
arr = [0 for _ in range(20190325)]
arr[0]=arr[1]=arr[2]=1
for i in range(3,20190324):
    arr[i]=(arr[i-1]+arr[i-2]+arr[i-3])%10000
print(arr[20190323])
'''
# 4.4 数的分解
'''
count = 0
def check(x):
    s_x = str(x)
    if '2' in s_x or '4' in s_x:
        return False
    return True

for i in range(1,2019):
    if check(i):
        for j in range(i+1,2019):
            if check(j):
                k=2019-i-j
                if k>j and check(k):
                    count += 1
                    # print(i,j,k)
print(count)
'''
# 4.6特别数的和
'''
n = int(input())
s = 0
for i in range(1,n+1):
    a = i

    while a != 0:
        temp = a%10
        a = int(a/10)
        if temp in [2,0,1,9]:
            s += i
            break
print(s)
'''

# 4.7完全二叉树的权值
'''
n = int(input())
data = list(map(int,input().split()))
deep = flag_deep = 1
max_sum = 0
while 2**deep -1 <= n:
    data_sum = sum(data[2**(deep-1)-1:(2**deep)-1])
    print(data[2**(deep-1)-1:(2**deep)-1])
    if max_sum<data_sum:
        max_sum=data_sum
        flag_deep=deep
    deep += 1
print(flag_deep)
'''

# 4.8等差数列
'''
n = int(input())
a = list(map(int,input().split()))
count = 0
d = float('inf')
a.sort()
for i in range(1,n):
    nd = a[i]-a[i-1]
    if nd < d:
        d = nd
for i in range(a[0],a[n-1],d):
    count += 1
print(count+1)
'''
# 4.9换钞票
for o in range(1,10):
    f = 0
    t = o*10
    m = 200-t*2-o
    if m%5==0:
        f=m/5
    count = o+t+f
    print(o,t,f,count)