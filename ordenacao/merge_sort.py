def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    il = 0
    ri = 0

    while il < len(left) and ri < len(right):
        if left[il] < right[ri]:
            result.append(left[il])
            il += 1
        else:
            result.append(right[ri])
            ri += 1

    result.extend(left[il:])
    result.extend(right[ri:])

    return result


if __name__ == '__main__':
    lista = [5, 3, 1, 2, 4]
    print(merge_sort(lista)
)
