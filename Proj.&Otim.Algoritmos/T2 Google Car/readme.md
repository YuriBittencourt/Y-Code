# Google Car 
 Dado uma tripla (x,y,z) de destino, calculará o número de caminhos possíveis a se chegar no destino. Os movimentos aceitos são todos que caminham em direção do destino, movimentos contrários são rejeitados pois aí poderíamos ter infinitos caminhos.
 - Em um universo unidimensional, só temos um movimento aceito: Leste.
 - Em um bidimensional temos 3 movimentos aceitos: Norte, Leste e Nordeste. Ou podemos pensar em: (x+1,y), (x,y+1) e (x+1,y+1) respectivamente.
 - Em um tridimensional temos 7 movimentos aceitos: Norte, Leste, Nordeste, Profundidade, Norte-Profundidade, Leste-Profundidade e Nordeste-Profundidade. Ou podemos pensar em: (x+1,y,z), (x,y+1,z), (x+1,y+1,z), (x,y,z+1), (x+1,y,z+1), (x,y+1,z+1), (x+1,y+1,z+1)\
 Há uma fórmula que se verifica verdade para esses casos dos movimentos aceitos: 2<sup>n</sup> -1 onde n é o número de dimensões.
 
 ### Há 3 formas de calcular:
    
1. [Rota recursiva](RotaRecur.java) Do ponto à origem, recursivamente;
2. [Rota recursiva com memorização](RotaRecurOtim.java) Do ponto à origem memorizando oque já fora calculado, recursivamente;
3. [Rota simples](RotaSimples.java) Da origem ao ponto memorizando oque já fora calculado, iterativo;

Note que o resultado será o mesmo em todas as execuções, o tempo de execução pode variar.
- [ ] Refazer os algoritmos em Python 3.X
