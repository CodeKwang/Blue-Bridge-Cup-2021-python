#coding=utf-8
# 十一届省赛
# 试题A:贴门牌号
# 原问题：从1到2020中这些数字中有多少个2（注意：不是问多少个数字里有2）
ans = 0
for i in range(1,2021):
    ans += (str(i).count('2'))
print(ans)

# 试题B:
# 寻找2020
m=[]
f = open("./2020.txt","r")
while True:
    data = f.readline()
    if data[-1]!='\n':
        m.append(list(data))
        break
    else:
        data = data[:-1]
    a = list(data)
    m.append(a)
f.close()
row = len(m)
col = len(m[0])
count =0
for i in range(row):
    for j in range(col):
        if m[i][j]=='2':
            if j+3<col:
                if m[i][j]+m[i][j+1]+m[i][j+2]+m[i][j+3]=='2020':
                    count+=1
            if i+3<row :
                if m[i][j]+m[i+1][j]+m[i+2][j]+m[i+3][j]=='2020':
                    count+=1
            if i+3<row and j+3<col:
                if m[i][j]+m[i+1][j+1]+m[i+2][j+2]+m[i+3][j+3]=='2020':
                    count+=1
print(count)

# 3.跑步训练
import datetime
start = datetime.date(2000, 1, 1)
end = datetime.date(2020, 10, 1)
days = datetime.timedelta(days=1)
res = 0
while start <= end:
    if start.day == 1 or start.weekday() == 0:
        res += 2
    else:
        res += 1
    start += days

print(res)


# 4.蛇形填空
m = [[0 for _ in range(50)] for i in range(50)]
m[0][0] = 1
i = 0
j = 0
for k in range(20):
    if i == 0 and j % 2 == 0:
        j += 1
        m[i][j] = m[i][j-1]+1
        while j > 0:
            m[i+1][j-1] = m[i][j]+1
            i += 1
            j -= 1
    if j == 0 and i % 2 == 1:
        i += 1
        m[i][j] = m[i-1][j]+1
        while i > 0:
            m[i-1][j+1] = m[i][j]+1
            i -= 1
            j += 1
print(m[19][19])
# 发现规律
ans = 1
for i in range(1, 20):
    ans = ans + i*4
print(ans)

# 5.排序
for i in range(14,-1,-1):# 输入onmlkjihgfedcba
    print(chr(ord('a')+i),end='')
    # 答案：jonmlkihgfedcba
    '''
    【解析】：冒泡排序，要求字符串最短，那就假设完全逆序，设长度为n，则移动次数为 n*(n-1)/2，
    要求移动次数恰好大于100，则 n=15；移动次数105。要求字典序最小，则把第六个字符移动到第一个位置，
    前五个字符后移一位。纯逻辑推导，无代码。
    '''
print()
# 6.成绩统计

n = eval(input())
you = 0
jige = 0
for i in range(n):
    a = int(input())
    if a >= 60:
        jige += 1
        if a >= 85:
            you += 1
jige = format(jige/n,'.2f') # format方法可以四舍五入，但返回的是字符串形式
you = format(you/n,'.2f')
# print(jige)
print(f'{jige[2:]}%') # 取字符串’0.‘后面的数字
print(f'{you[2:]}%')

# 7.单词分析
'''
word = input()
new_word = sorted(list(set(word))) # 先转换为集合，再转换为列表，再排序
print(new_word)
max_word = None
max_count = 0
for i in new_word:# 遍历列表
    if max_count < word.count(i):# 一定要严格大于
        max_word = i
        max_count = word.count(i)
print(max_word)
print(max_count)
'''

# 8.数字三角形

N = int(input())
m = []
for i in range(N):
    m.append(list(map(int,input().split())))
# 动态规划
for i in range(N): 
    for j in range(i):
        m[i][j] += max(m[i-1][j-1],m[i-1][j])
        print(i,j,m[i][j])
# 加了条件的输出
print(m[N-1][N//2] if N%2 == 1 else max(m[N-1][N//2-1],m[N-1][N//2]))


#  9.平面切分
N = int(input())
li = []
point_count = 0
for _ in range(N):
    a,b = map(int, input().split())
    if [a,b] in li: # 去掉重复线
        continue
    li.append([a,b])
    point = []
    for i in range(len(li)-1):
        if li[i][0] - li[len(li)-1][0] == 0: # 去掉平行线
            continue
        x = (li[len(li)-1][1]-li[i][1])/(li[i][0]-li[len(li)-1][0])
        y = x*li[i][0]+li[i][1]
        if [x,y] in point:
            continue
        point.append([x,y])
    point_count += len(point)

print(len(li)+point_count+1)

# 10.装饰珠
N = []
for i in range(6):
    N.append(list(map(int,input().split())))
