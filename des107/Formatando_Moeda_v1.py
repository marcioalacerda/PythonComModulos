'''Adapte o codigo, criando uma função adicional chamada moeda() que consiga mostrar valores com o valor monetário formatado'''
from des107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Aumantando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}.')
print(f'Reduzindo 13%, teos {moeda.moeda(moeda.diminuar(p, 13))}.')
