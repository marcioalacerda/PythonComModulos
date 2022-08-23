'''Dentro do pacote utilidades que criamos na versão anterior, temos um módulo chamado dados.
Criamos uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação
de dados para aceitar apenas valores que sejam monetários.'''
from des112.utilidades import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)