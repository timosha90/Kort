from random import randint
a = (1, 18, 55, 6, 78, 99, 78, 85, 12, 22 )
print(max(a))
print(min(a))


b = []
c = []
for i in range(10):
    b.append(randint(0, 5))
    c.append(randint(-5, 0))
b = tuple(b)
c = tuple(c)
print(b)
print(c)
d = b+c
print(d)
print(d.count(0))

A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
sum1 = 0
sum2 = 0
for i in A:
    sum1 += i
print(sum1)
for k in B:
    sum2 += k
print(sum2)
if sum1>sum2:
    print('Сумма больше в кортеже A')
else:
    print('Сумма больше в кортеже B')


a = ('а', 'b', 'c', 'dfgt', 'rtf')
c = list(a)
print(','.join(c))


