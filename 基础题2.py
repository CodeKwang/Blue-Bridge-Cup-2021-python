# coding=utf-8

# 2.15长整数加法

'''
def change_length(arr,l): # 此方法使两字符串长度相等
    arr = '0'*(l-len(arr))+arr
    return arr

arr = input()
arr_2 = input()
# 两数长度若不等，短的数加前导0
if len(arr)>len(arr_2):
    arr_2=change_length(arr_2,len(arr))
elif len(arr)<len(arr_2):
    arr = change_length(arr,len(arr_2))
# 结果最多是最长数的长度加1
result=[0 for i in range(len(arr)+1)]
k=0 # 进位
for i in range(len(arr)):
    rs = k+int(arr[len(arr)-i-1])+int(arr_2[len(arr_2)-i-1])
    result[len(arr)-i] = rs%10
    k=0
    if rs>=10:
        k=int(rs/10)

if k!=0:# k != 0 则最高位为k
    result[0]=k
    for i in range(len(result)-1):
        print(result[i],end='')
    print(result[-1])
else:# 否则最高为为0不输出
    for i in range(len(result)-2):
        print(result[i+1],end='')
    print(result[-1])
'''

# 2.16哈夫曼树
'''
n = eval(input())
arr = list(map(int,input().split()))

price = [0 for i in range(n-1)]

for i in range(n-1):
    arr.sort()
    value = arr.pop(0)
    value_2 = arr.pop(0)
    price[i]=value+value_2
    arr.append(price[i])
print(sum(price))
'''

# 2.17N皇后问题
'''
    A存放每一个皇后所在的行（也可以看成每一个皇后所在列）
'''
'''
def queen(A,cur=0):
    if cur ==len(A):
        print(A)
        return 0
    for col in range(len(A)):
        A[cur],flag=col,True
        for row in range(cur):
            if A[row] == col or abs(col-A[row]) == cur-row:# 不能同一列 和 不能对角线
                flag = False
        if flag:
            queen(A,cur+1)
n = eval(input())

queen([None]*n)
'''
# 2.18 报时助手
# 兔子休息时，乌龟到达了终点，结束。
# 注意：有可能兔子在休息中，乌龟就到达了终点
# 所以休息时间未必循环完
# 如：兔子要休息10s，乌龟可能在兔子休息的第9s就到达了终点
# 这里的flag就起到提前结束的功能
'''
h,m=map(int,input().split())
'''
# 2.20龟兔赛跑预测
'''
data = list(map(int,input().split()))
rabbit = tortoise = time = 0
flag=False
while True:
    if rabbit == data[-1] or tortoise == data[-1]:
        break
    if rabbit-tortoise>=data[2]:
        for i in range(data[3]):
            tortoise+=data[1]
            time+=1
            if tortoise==data[-1]:
                flag=True
                break # 退出for循环
        if flag:
            break # 退出while循环
    time +=1
    rabbit+=data[0]
    tortoise+=data[1]

if rabbit>tortoise:
    print('R')
    print(time)
elif rabbit<tortoise:
    print('T')
    print(time)
else:
    print('D')
    print(time)
'''
# 2.21芯片测试
'''
    重点是好芯片比坏芯片多
    如果忽略这个问题就很难解决，本人开始你就不幸忽略了。。。
    既然好芯片比坏芯片多，那么我们只需记录每一列0的个数就行了，若个数超过n/2，则此芯片为坏芯片
    一个chip列表来记录芯片的好坏
'''
'''
n=int(input())
arr = [[] for _ in range(n)]
chip = [True for _ in range(n)]
for i in range(n):
    arr_ = input().split()
    for j in range(n):
        arr[i].append(int(arr_[j]))

for i in range(n):
    count=0
    for j in range(n):
        if arr[j][i] == 0:
            count +=1
    if count>n/2:
        chip[i]=False
for i in range(n):
    if chip[i]:
        print(i+1, end=' ')
'''

# 2.22 FJ字符串

n=eval(input())
str_n = ''
for i in range(n):
    str_n = str_n + chr(ord('A')+i)+str_n
    print(str_n)
print(str_n)

# 2.23 sin之舞
