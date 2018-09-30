#-*-coding=utf-8-*-
'''def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

# 递归计算，求 1* 2 * 3

print fact(5)

print fact(1000)'''

def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print('fact(100) =', fact1(100))

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')