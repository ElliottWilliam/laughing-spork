import math

lists = []
mean_lists = 0
p = 0
k = 0
o = 0
q = 0
h = 0
s = 1


def appender():
    global s
    print('Insert data point', s, ':')
    x = int(input())
    lists.append(x)
    s += 1


def mane():
    global mean_lists
    global lists
    mean_lists = sum(lists) / len(lists)


def squarer():
    for number in range(len(lists)):
        global p
        lists[p] = (lists[p] - mean_lists) ** 2
        p += 1


def sum_square():
    global d
    global o
    global q
    global lists
    global h
    o = (sum(lists)) / len(lists)
    h = math.sqrt(o)
    h = round(h, d)


print('How many data points?')
y = int(input())
print('How many Deviations?')
v = int(input())
print('How many Decimal places?')
d = int(input())
for i in range(y):
    appender()

mane()
squarer()
sum_square()

print('Your Standard Deviation is : ', h * v)
