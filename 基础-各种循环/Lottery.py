#年会抽奖程序
#某公司有300名员工，年会抽奖，奖项如下：
#     · 一等奖三名，奖励3090
#     · 二等奖六名，奖励2080
#     · 三等奖三十名，奖励1070
# 规则：
#     · 共抽三次，第一次抽三等奖，第二次抽二等奖，第一次抽一等奖
#     · 每个员工限中奖一次，不允许重复中奖
import random

#设定员工
data = []
i = 1
while i < 301:
    data.append(i)
    i += 1

#设定中奖名单
list3 = [] #三等奖
list2 = [] #二等奖
list1 = [] #一等奖

#设定抽奖次数
i = 3
#开始抽奖
while i > 0 :
    if i == 3:#抽三等奖 三十名
        for n in range(1,31):
            a = random.choice(data) #随机取出列表中的一个元素
            data.remove(a) #在列表中将该元素删除，以免重复中奖
            list3.append(a) #将该元素添加至中奖名单中
        i -= 1
    elif i == 2:#抽二等奖 六名
        for n in range(1,7):
            a = random.choice(data)
            data.remove(a)
            list2.append(a)
        i -= 1
    elif i == 1:#抽二等奖 六名
        for n in range(1,4):
            a = random.choice(data)
            data.remove(a)
            list1.append(a)
        i -= 1
print(f"获得一等奖的是{list1}",len(list1))
print(f"获得二等奖的是{list2}",len(list2))
print(f"获得三等奖的是{list3}",len(list3))


