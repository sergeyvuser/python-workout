def mysum(*args):
    summ = 0
    for number in args:
        summ += number
    return summ

print(mysum(10, 20, 30, 40))

def mysum2(start: int = 20, *args):
    summ = 0
    for number in args:
        summ += number
    return summ + start

print(mysum2(10, 20, 30, 40, 10))


