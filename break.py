i = int(input("How many numbers to scan?: "))

for n in range(2, i):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', int(n / x))
            break
    else:
        print(n, 'is prime number')