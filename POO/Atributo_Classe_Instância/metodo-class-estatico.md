# Métodos estáticos

Um método estático não recebe um primeiro argumento
explícito. Ele também é um método vinculado à classe e não ao
objeto da classe. Este método não pode acessar ou modificar o
estado da classe. Ele está presente em uma classe porque faz
sentido que o método esteja presente na classe.

# Métodos de classe

Métodos de classe estão ligados à classe e não ao objeto. Eles
têm acesso ao estado da classe, pois recebem um parâmetro
que aponta para a classe e não para a instância do objeto.

## Métodos de classe x métodos estáticos

• Um método de classe recebe um primeiro parâmetro que
aponta para a classe, enquanto um método estático não.

• Um método de classe pode acessar ou modificar o estado
da classe enquanto um método estático não pode acessá-lo
ou modificá-lo.