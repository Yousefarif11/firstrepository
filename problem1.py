def multiples(n):
    sum_ = 0
    for i in range(n):
        if i % 3 == 0:
            sum_ += i
        elif i % 5 == 0:
            sum_ += i
    return sum_

print(multiples(1000))