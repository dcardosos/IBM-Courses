def desloca(x, k=1):
    ''' (list) -> NoneType

    RECEBE uma lista não vazia x de números inteiros.
    Faz um deslocamento cíclico na lista x.
    '''
    return x[-k:] + x[:-k]


def desloca_matriz(matA, k):
    ''' (matriz, int) -> NoneType

    RECEBE uma matriz não vazia matA com números inteiros e um inteiro positvo k.
    Faz k deslocamentos cíclicos na matriz matA, utilizando para isso a função desloca().
    '''
    new = []
    for l in matA:
        new.append(desloca(l, k))
    return new

