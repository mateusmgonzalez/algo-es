

def swap(lista, i, j):
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp


def select_sort(lista):
    i = 0
    while i < len(lista) - 1:  # percorre a lista de 0 a len - 2
        min_index = i  # inicializa o min_index
        j = i + 1  # j e o indice que vai ser escolido para realizar o swap
        while j < len(lista):  # j vai de i + 1 ate len - 1
            if lista[j] < lista[min_index]:  # verifica se o valor atual de j e menor do que o do index_min
                min_index = j  # troca
            j += 1
        if min_index != i:
            swap(lista, min_index, i)
        i += 1


if __name__ == '__main__':
    lista = [5,3,1,2,4]
    select_sort(lista)
    print(lista)