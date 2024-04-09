



def busca_linear(arr, v):
    for i in range(len(arr)):
        if arr[i] == v:
            return i

    return None


def busca_binaria(arr, v, baixo, alto):
    if baixo > alto:
        return -1

    meio = (baixo + alto) // 2
    if arr[meio] == v:
        return meio
    elif arr[meio] < v:
        return busca_binaria(arr, v, meio + 1, alto)
    else:
        return busca_binaria(arr, v, baixo, meio - 1)