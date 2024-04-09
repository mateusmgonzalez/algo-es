from select_sort import swap


def bubble_sort(lista):
    n = len(lista)  # declaro uma variavel para guardar o valor do tamanho da lista
    while n > 1:  #
        i = 1
        while i < n:
            if lista[i] < lista[i - 1]:
                swap(lista, i, i - 1)
            i += 1
        n -= 1



if __name__ == '__main__':
    lista = [5,3,1,2,4]
    bubble_sort(lista)
    print(lista)