#coding=utf-8
# 十一届国赛
# 试题A:美丽的2
ans=0
for i in range(1,2021):
    if str(i).count("2")!=0:
        ans+=1
print(ans)

# 试题B:合数个数
ans = 0
for i in range(4,2021):
    t=i//2+1 #取整
    for j in range(2,t):
        if i%j==0:
            ans+=1
            break
print(ans)

# 试题C: