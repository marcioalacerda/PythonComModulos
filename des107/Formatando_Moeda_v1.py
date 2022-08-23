'''Adicione ao módulo moeda.py, uma função chamada resumo(),que mostra na tela algumas informações geradas pelas funções
que já temos no modulo criado até aqui.'''
from des107 import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)
