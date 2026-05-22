### Trilha de Python: Resposta das questões

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
Todas essas funções vão printando resultados para o usuário ter um mínimo controle e conhecimento do que está acontecendo.


-> Instruções de uso:  
O usuário precisa apenas inserir as informações pedidas respeitando a unidade (real, euro, dias).  
A partir disso, todos os cálculos e resultados já são printados na tela.

-> Respostas às perguntas teóricas:  
■ Qual a diferença entre o comando git add . e git commit -m "mensagem"?  
São duas etapas diferentes do processo de salvar o projeto.  
O "git add " determina que arquivos terão as alterações salvas para serem mandadas, ou seja, o que será colocado no "staging area", uma área temporária. É como se preparasse o arquivo. No caso específico do "git add .", é que todas as alterações de toda a pasta e as subpastas serão colocadas.  
Enquanto isso, o "git commit -m "mensagem" representa o salvamento permanente desses arquivos que foram previamente preparados, junto com uma mensagem do que foi feito.  


■ Por que é necessário realizar o casting (conversão de tipo) ao usar a função
input() em Python para cálculos matemáticos?  
É necessário, pois a função input() sempre vai retornar uma string. Se não for feito o casting (forçar o que foi recebido a ser tratado e se comportar como algo que não é string), ao tentar combinar a string não convertida com algum número em uma operação, acontece um TypeError, já que os tipos não são compatíveis. Observação: se não fizer a conversão pra int, float etc e tentar somar, o Python irá concatenar as duas strings, ou seja, juntá-las, combiná-las.


■ O que acontece se tentarmos somar uma variável do tipo str com uma do
tipo float?  
Acontece um erro do tipo TypeError, já que os dois tipos de variáveis não são compatíveis para operações, já que, é apenas possível somar matematicamente números float, int etc e apenas possível "somar" (concatenar) strings.  




2) [simulador_tcg]
   
-> Explicação do funcionamento do programa:  
   O programa funciona, inicialmente, pedindo as informações (nome, HP e pontos de ataque) de cada monstro.  
   Uma função de validação certifica de que os dados numéricos inseridos são maiores do que zero.  
   A função de ataque funciona calculando o dano, e subtrai da vida do defensor (nesse primeiro caso, o 2), e retorna o HP do que foi atacado. Também faz com que, se a vida do defensor chegar a ser menor do que zero, ele vai mudar pra esse valor ser zero, já que não pode ser negativo.    
   A função de exibição do placar funciona printando na tela as informações de cada monstro.
   O loop while, que é do combate em si, roda enquanto a vida tanto do monstro 1 quanto do monstro 2 for maior do que zero.  
   Dentro dele, como foi previamente definido no enunciado, o monstro 1 ataca o mosntro 2. Então, abre uma condicional para se o monstro 2 tiver sobrevivido (ou seja, vida ainda é maior do que zero). Se sim, agora o atacante é ele.  
   O placar é exibido depois de cada ciclo.  
   Se o monstro 1 sobreviver a esse ataque (o loop while verifica isso), ele ataca novamente e assim vai, até um dos monstros chegar a um HP = zero.  
   Quando alguma das vidas for zerada, o loop acaba e uma condicional define o que printar na tela (dependendo do monstro vencedor).  
   Também tem, dentro do loop da batalha, um contador dos turnos de ataque.  
   

-> Instruções de como rodar o script:    
Tudo que o usuário precisaria fazer é escrever as informações pedidas pelo programa, respeitando o tipo de dado e s restrições (HP e ataque não podem ser inicializadas como zero ou como negativos).  


-> Respostas às perguntas teóricas:  
■ Qual é a principal diferença prática entre usar um laço for e um laço
while em Python? Por que o while foi a melhor escolha para este
duelo?  
A principal diferença é que, num loop for, a base é a iteração. Ou seja, ele funciona com uma quantidade pré-determinada de vezes que vai iterar.  
Já num loop while, a base é a condição. Ele roda e repete até u7ma condição pré-determinada acontecer, e isso pode ser depois de 1000 ou 3 iterações, não é possível determinar isso antes.  
Dito isso, foi a melhor escolha, pois o duelo acaba com base na CONDIÇÃO de algumas das vidas serem zeradas. Não é viável determinar isso, pois depende dos pontos de HP  do ataque de cada monstro que o usuário colocar, não havendo um geral para todas as vezes.  


■ Para que serve a palavra-chave return dentro de uma função? O que
acontece se uma função fizer um cálculo matemático mas não possuir
o return?  
O return de uma função determina o que ela vai retornar. Ou seja, quando é chamada e executada, ela precisa depois devolver um valor para quem a chamou (a linha de código que a "chama"), além de também determinar o fim dela, podendo passar para a próxima etapa do cógigo.  
Se um cálculo matemático for feito, mas sem return, a função irá calcular tudo perfeita e normalmente, mas esse resultado não irá para lugar nenhum, consequentemente deixando de existir ao final da função. Se um return não é colocado, a função retorna None, que é um "nada".  


■ O que é um "Loop Infinito" e como podemos evitá-lo ao construir uma
estrutura while?  
Um loop infinito é um loop que simplesmente não para de rodar. Seja por conta de uma condição de parada falha ou até mesmo nunca atingida.  
Para evitá-lo, o ideal é inicializar uma variável de controle que seja atualizada e utilizar uma condição de parada válida e atingível.

