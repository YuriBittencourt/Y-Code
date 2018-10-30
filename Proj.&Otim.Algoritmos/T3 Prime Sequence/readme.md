# Sequência de primos
Dado um número *n* pertencente aos naturais (n>0), o programa retornará a primeira sequência de tamanho *n* satisfazendo os requisitos de cada etapa, sendo que as etapas seguintes incluem as anteriores:

1. Etapa: número atual somado com o próximo é primo.
2. Etapa: último número somado com o primeiro é primo, traz a ideia de ciclo.
3. Etapa: número atual somado com o seu correspondente na outra metade é primo.

Baseado nisso podemos inferir valores que já serão **inválidos.**\
### Válidos: ###
1. Etapa: Todos os valores de naturais desde que n > 2.
2. Etapa: _n%2=0_, ou seja, pares. Pois a sequência sempre será alternando entre números pares e ímpares, com um número ímpar teríamos que o ínicio seria um número par e o fim também.
3. Etapa: _n%4=2_, ou seja, pares não divísiveis por 4, ou dobro de ímpares.


- [ ] Criar imagens para explicação gráfica aqui. 