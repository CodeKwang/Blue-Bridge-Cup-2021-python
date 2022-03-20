#coding=utf-8

# 1.1 Fibonacci数列题
'''
n = eval(input())
Fib = [1 for i in range(n+1)]
k=3
while k <= n:
    Fib[k] = (Fib[k - 1] + Fib[k - 2]) % 10007
    k += 1
print(Fib)
print(Fib[n])
'''

# 1.2 圆的面积
'''
import math
r = int(input())
area = math.pi * r * r
print('%.7f' % area) # 四舍五入保留小数点后7位
'''

# 1.3 序列求和
'''
n = int(input())
s = n * (n + 1) / 2 # 等差数列公式，节省很多时间
print('%d' % s)
'''

# 1.4 A+B问题
'''
# 注意：本体数据规模较小，可以正常计算
# 若数据规模过大，则考虑用字符串存取大数，然后用大数加法来计算结果并输出
a, b = map(int, input().split())
print(a + b)
'''

# 2.1 数列排序
'''
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n - 1):
    print(arr[i], end=' ')
print(arr[n-1], end='')
'''

# 2.2 十六进制转八进制（十六进制转十进制，十进制转八进制）
'''
t = int(input())
for i in range(t):
    n=input()
    ans = format(int(n,16),'o')
    print(ans)
'''

# 2.3 十六进制转十进制
'''
n = input()
print(int(n, 16))
'''

# 2.4 十进制转十六进制
'''
n = int(input())
print(format(n, 'X')) # x 输出字母为小写 X 输出字母为大写
'''

# 2.5 特殊回文数
'''
import time
start = time.perf_counter()
def is_pal(i_):
    i_s = str(i_)
    if i_s == i_s[::-1]:
        return True
    else:
        return False

def sum_i(i_):
    s = 0
    i_s = str(i_)
    for j in range(len(i_s)):
        s+=int(i_s[j])
    return s

n = int(input())
i = 10000
while i<1000000:
    if is_pal(i):
        if sum_i(i)==n:
            print(i)
    i+=1
end = time.perf_counter()
print(end-start)
'''

# 2.6 回文数
'''
def is_pal(i_):
    i_s = str(i_)
    if i_s == i_s[::-1]:
        return True
    else:
        return False


i = 1000
while i < 10000:
    if is_pal(i):
        print(i)
    i += 1
'''

# 2.7 水仙花数
'''
def is_nar(i_):
    a=i_%10
    b=int((i_/10))%10
    c=int((i_/100))
    if i_==a**3+b**3+c**3:
        return True
    else:
        return False

i=100
while i<1000:
    if is_nar(i):
        print(i)
    i += 1
'''

# 2.8 杨辉三角
'''
n = eval(input())
k = 2
triangle_yang = []
for i in range(n):
    triangle_yang.append([0 for j in range(i+1)])

for i in range(n): # 第一列和最后一列为1
    triangle_yang[i][0] = triangle_yang[i][-1]=1

while k<n:
    m=1
    while m<k:# 两件数值之和
        triangle_yang[k][m] = triangle_yang[k-1][m-1]+triangle_yang[k-1][m]
        m+=1
    k+=1

for i in range(n):
    for j in range(i+1):
        print(triangle_yang[i][j],end=' ')
    print()
'''

#2.9 查找整数
'''
n = eval(input())
arr = input().split()
a = input()
i = 0
while i<n:
    if a==arr[i]:
        print(i+1)
        break
    i+=1
if i==n:
    print(-1)
'''

# 2.10列特征
'''
n = eval(input())
arr = input().split()
print(max(int(arr[i]) for i in range(n)))
print(min(int(arr[i]) for i in range(n)))
print(sum(int(arr[i]) for i in range(n)))
'''

# 2.11 字母图形
'''
    字符转ASCII码函数：ord(‘A’)–>64
    ASCII码转字符函数：chr(64)–>A
'''
'''
n, m = map(int, input().split())

graph = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if j>=i:
            graph[i][j] = chr(ord('A')+j-i) # 这里要发现题目规律
        else:
            graph[i][j] = chr(ord('A')+i-j)
for i in range(n):
    for j in range(m):
        print(graph[i][j],end='')
    print()
'''

#2.12 字串01
'''
    {0 : 0 > 3}
     │   │ │ │
     │   │ │ └─ 宽度为 3
     │   │ └─ 右对齐
     │   └─ 补位为 '0'
     └─ Element index（位置）
'''
'''
for i in range(32):
    print("{0:0>5}".format(format(i,"b")))

'''
# 2.13闰年判断
'''
def is_leap_year(year):
    if year%4 ==0 and year%100!=0 or year%400==0:
        return True
    return False
year=eval(input())
if is_leap_year(year):
    print("yes")
else:
    print("no")
'''

# 2.14阶乘计算

n = int(input())

a = s =1

while a <= n:
    s = s * a
    a += 1
print(s)
