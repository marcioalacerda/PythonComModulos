def leiaDinheiro(msg):
    '''
    -> Valida de dados para aceitar apenas valores
    que sejam monetário.
    :param txt: mensagem de entrada de dados.
    :return: retorna o preço válido
    '''
    from termcolor import colored
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(colored(f'ERRO! \"{entrada}\" é um preço inválido!', 'red'))
        else:
            válido = True
            return float(entrada)
