#-*-coding=utf-8-*-
#切片操作
list = ['历史','数学','语文','地理','化学','英语']

# 从索引0开始取，直到索引3为止，但不包括索引3
print list[0:3]

L = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

print L[:10]

#每5个取一个
print L[::5]

#前10个数，每两个取一个
L[:10:2]