### Trilha de Python:

1) [calculadora_viagem.py]

-> Explicação do funcionamento do programa:  
O programa funciona da seguinte maneira:  
O usuário insere cada uma das informações pedidas, sendo elas orçamento pra viagem (em reais), destino, valor da passagem (em reais), custo diário da hospedagem (em euros) e quantidade de dias.   

Antes de inicializar e pedir essas variáveis, eu fiz uma função que valida se cada um dos inputs é positivo.
Além disso, eu faço um casting de cada input para todos se encaixarem ao tipo de variável pedido no enunciado e também faço uma rápida verificação do que foi inserido com um print de tudo.
Então, fiz as funções da lógica e cálculos em si do código:
- a que converte valor de euro para real (multiplicando por 6.1);
- a que calcula o valor da hospedagem (que foi pedido em euro e é convertido dentro da função, multiplicando esse valor pela quantidade de dias);
- a que calcula o custo total da viagem (valor da hospedagem total somado com o valor da passagem);
- a que valida o orçamento (verifica se o custo total é ou não menor/igual ou maior que orçamento. se for menor/igual, orçamento é possível e função retorna boolean True. se for maior, orçamento é impossível e função retorna boolen False);
- a que averigua o status da viagem (se a funçao de valição do orçamento tiver retornado True - ou seja, custo é menor/igual ao orçamento - E a quantidade de dias for maior que zero, a funçao retorna True - viagem viável - e calcula o quando dinheiro sobraria - custo subtraído do orçamento. se a função de validação de orçamento tiver retornado False - custo maior que orçamento - OU a quantidade de dias for menor que zero, retorna False - viagem inviável - e calcula o quanto faltaria pra conseguir ter um orçamento possível - orçamento subtraído do custo);
Todas essas funções vão printando resultados para o usuário ter um mínimo controle e conhecimento do que está acontecendo

-> Instruções de uso:  
O usuário precisa apenas inserir as informações pedidas respeitando a unidade (real, euro, dias).  
A partir disso, todos os cálculos e resultados já são printados na tela.

-> Respostas às perguntas teóricas:  
■ Qual a diferença entre o comando git add . e git commit -m "mensagem"?
■ Por que é necessário realizar o casting (conversão de tipo) ao usar a função
input() em Python para cálculos matemáticos?
■ O que acontece se tentarmos somar uma variável do tipo str com uma do
tipo float?
