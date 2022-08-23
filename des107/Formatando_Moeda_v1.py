'''Criando um pacote chamado utilidades que tenha dois modulos internos chamados moedas e dados.
Transferindo todas as funções do modulo moeda para o pacote moeda e mantendo tudo funcionando.'''
from des107.utilidades import moeda, dado

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)
