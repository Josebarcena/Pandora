def suma_enteros_while(N):
    i = 1
    suma = 0

    while i <= N:
        suma = suma + i
        i += 1

    print("suma", suma)


def suma_enteros_for(N):
    suma = 0

    for i in range(N+1):
        suma = suma + i
        i += 1

    print("suma", suma)


def print_list():
    lista = [ 'París', 'Lyon', 'Marsella']

    for elemento in lista:
        print(elemento)


if __name__ == "__main__":
    suma_enteros_while(100)
    suma_enteros_for(100)
    print_list()
