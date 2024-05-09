# [-5,-13,-10,-2]
import random
import timeit


def find_max_crossing_subarray(arr, low, mid, high):
    lsum = float('-inf')
    sum = 0
    lmax = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > lsum:
            lsum = sum
            lmax = i

    rsum = float('-inf')
    sum = 0
    rmax = 0
    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > rsum:
            rsum = sum
            rmax = i

    return lmax, rmax, lsum + rsum


def find_max_subarray(arr, low, high):
    if len(arr) == 0:
        return 0, 0, 0
    if low == high:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2

        (llow, lhigh, lsum) = find_max_subarray(arr, low, mid)
        (rlow, rhigh, rsum) = find_max_subarray(arr, mid + 1, high)
        (mlow, mhigh, msum) = find_max_crossing_subarray(arr, low, mid, high)

        if lsum > rsum and lsum > msum:
            return llow, lhigh, lsum
        elif rsum > lsum and rsum > msum:
            return rlow, rhigh, rsum
        else:
            return mlow, mhigh, msum


def find_max_subarray_forca_bruta(arr):
    result_sum = float('-inf')
    il = 0
    ir = 0

    for l in range(len(arr)):
        soma = 0
        for r in range(l, len(arr)):
            soma += arr[r]
            if soma > result_sum:
                result_sum = soma
                il = l
                ir = r

    return il, ir, result_sum


def max_profit(arr):
    profit = 0
    min_price = arr[0]
    for i in range(1, len(arr)):
        profit = max(profit, arr[i] - min_price)
        min_price = min(min_price, arr[i])

    return profit


# Função para gerar arrays aleatórios de tamanho n
def generate_random_array(n):
    return [random.randint(-100, 100) for _ in range(n)]


if __name__ == '__main__':
    array_sizes = [10, 100, 1000, 10000]  # Tamanhos dos arrays a serem testados

    for size in array_sizes:
        arr = generate_random_array(size)
        execution_time = timeit.timeit(lambda: find_max_subarray_forca_bruta(arr), number=10)
        print("Tamanho do array:", size, "Tempo de execução:", execution_time)
        execution_time = timeit.timeit(lambda: find_max_subarray(arr, 0, size - 1), number=10)
        print("Tamanho do array:", size, "Tempo de execução:", execution_time)
