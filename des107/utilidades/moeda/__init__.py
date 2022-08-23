def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    '''
    -> Calcula a redução de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    '''
        -> Calcula o dobro de um determinado preço,
        retornando o resultado com ou sem formatação.
        :param preço: o preço que se quer reajustar.
        :param formato: quer a saída formatada ou não?
        :return: o valor reajustado, com ou sem formato.
        '''
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    '''
        -> Calcula a metade de um determinado preço,
        retornando o resultado com ou sem formatação.
        :param preço: o preço que se quer reajustar.
        :param formato: quer a saída formatada ou não?
        :return: o valor reajustado, com ou sem formato.
        '''
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    '''
    -> Formata o volar do preço e retorna em
    formato de valor monetário.
    :param preço: o preço que se quer formatar.
    :param moeda: formato monetário
    :return: o valor com formato monetário
    '''
    res = f'{moeda}{preço:.2f}'.replace('.', ',')
    return res


def resumo(preço=0, taxaa=10, taxar=5):
    '''
    -> Formatar todos os resultados e retornar
    em formato de tabela.
    :param preço: o preço que se quer reajustar.
    :param taxaa: taxa de aumento no reajuste.
    :param taxar: taxa de redução no reajuste.
    :return: todos os dados retornados pela
     outra funções formatado em tabela.
    '''
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metado do preço: \t{metade(preço, True)}')
    print(f'{taxaa:2}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar:2}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
