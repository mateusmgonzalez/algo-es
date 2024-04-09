
def fibonacci(n):
    if n <= 0:
        return 0

    f = [0, 1]

    for i in range(2, n + 1):
        f.append(-1)

    return fibonacci_topdown(n, f)

def fibonacci_topdown(n, f):
    if f[n] == -1:
        return fibonacci_topdown(n - 1, f) + fibonacci_topdown(n - 2, f)
    return f[n]


def fibonacci_old(n):
    if n <= 2:
        return 1

    return fibonacci_old(n - 1) + fibonacci_old(n - 2)

if __name__ == '__main__':
    print(fibonacci(10))


    print(fibonacci_old(10))
