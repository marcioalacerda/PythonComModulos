def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa/100)
    return res


def diminuar(preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    res = f'{moeda}{preço:.2f}'.replace('.', ',')
    return res