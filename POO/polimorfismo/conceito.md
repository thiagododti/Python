# Polimorfismo

A palavra polimorfismo significa ter muitas formas. 
Na programação , polimorfismo significa o mesmo nome de função
(mas assinaturas diferentes) sendo usado para tipos diferentes.

## Exemplo

len("Python")
len([10,20,30])

O Len ele conta a quantidade de itens dentro de um objeto.

Ao passar uma string ele conta as letras
E ao passar uma lista ele conta quantos elementos contém dentro da lista

## Mesmo método com comportamento diferente

Na herança, a classe filha herda os métodos da classe pai. No entanto, é
possível modificar um método em uma classe filha herdada da classe pai.
Isso é particularmente útil nos casos em que o método herdade da classe
pai não se encaixa perfeitamente na classe filha.