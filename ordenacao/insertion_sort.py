def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave


if __name__ == '__main__':
    lista = [5, 3, 1, 2, 4]
    insertion_sort(lista)
    print(lista)
