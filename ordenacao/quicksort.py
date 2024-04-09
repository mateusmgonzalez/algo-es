from select_sort import swap


def quicksort(lista):
    quicksortHelper(lista, 0, len(lista) - 1)


def quicksortHelper(lista, left, right):
    if left < right:
        pivot = partition(lista, left, right)
        quicksortHelper(lista, left, pivot - 1)
        quicksortHelper(lista, pivot + 1, right)


def partition(lista, left, right):
    middle = (left + right) // 2
    pivot = lista[middle]
    lista[middle] = lista[right]
    lista[right] = pivot

    boundary = left
    for i in range(left, right):
        if lista[i] < pivot:
            swap(lista, i, boundary)
            boundary += 1
    swap(lista, right, boundary)
    return boundary
