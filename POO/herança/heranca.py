# Herança

"""Em programação herança é a capacidade de uma class filha
derivar ou herdar as características e
comportamentos da classe pai (base)
"""
# Benefícios

"""
--Representa bem os relacionamentos do mundo real
--Fornece reutilização de código, não precisamos escrever
o mesmo código repetidamente. Além disso, permite adicionar
mais recursos a uma classe sem modificá-la.
--É de natureza transitiva, o que significa que, se a classe B
herdar da classe A, todas as subclasses de B herdarão
automaticamente da classe A
"""

# Herança Simples - Herda apenas uma classe PAI


class A:
    pass


class B(A):
    pass

# Herança múltipla - A class filha herda de várias classes pai


class C:
    pass


class D(A, C):
    pass
