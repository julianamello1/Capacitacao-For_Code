'''
Contexto

Junior é um novo membro da for_code e está desenvolvendo um protótipo
em texto para um novo Trading Card Game (Jogo de Cartas Colecionáveis).
Antes de se preocupar com interfaces gráficas ou motores de jogo, ele
precisa garantir que a matemática básica e o fluxo de turnos do jogo
funcionem perfeitamente.
Para ajudá-lo, você deve desenvolver um programa em Python que simule
um duelo entre duas cartas de monstros, gerenciando os turnos, calculando
os danos e declarando o vencedor.

Objetivo

Desenvolver um programa em Python que utiliza estruturas de repetição,
controle de fluxo e funções para simular uma batalha em turnos até que os
pontos de vida (HP) de um dos monstros cheguem a zero.

'''

# função de validação 
def validar(valor):
    if (valor <= 0):
        print("\n\tVALOR INVÁLIDO. OS VALORES INICIAIS NÃO PODEM SER MENORES OU IGUAIS A ZERO.")
        '''
        tem que ficar aqui em cima pq eu chamo ela antes do "espaço" de definir as funções
        '''



## entrada de dados e tipos

# monstro 1 
nome_m1 = input("\nNome do monstro 1: ")
pontos_vida_m1 = int(input("\tPontos de vida do monstro 1 (HP): "))
validar(pontos_vida_m1)
pontos_ataque_m1 = int(input("\tPontos de ataque do monstro 1: "))
validar(pontos_ataque_m1)

# monstro 2 
nome_m2 = input("\nNome do monstro 2: ")
pontos_vida_m2 = int(input("\tPontos de vida do monstro 2 (HP): "))
validar(pontos_vida_m2)
pontos_ataque_m2 = int(input("\tPontos de ataque do monstro 2: "))
validar(pontos_ataque_m2)


## funções

# função de atacar
def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):
    dano = ataque
    vida_atualizada = hp_defensor - dano
    if(vida_atualizada < 0):
        vida_atualizada = 0
    print(f"\n\t{nome_atacante} atacou {nome_defensor} e causou {dano} de dano!!!!")
    print(f"\n\t\tVida atual de {nome_defensor}: {vida_atualizada} HP")
    return vida_atualizada # função retorna a vida do defensor

# função que exibe placar
def exibir_placar(nome_monstro1, pontos_vida_m1, nome_monstro2, pontos_vida_m2):
    print(f"\n\tVida de {nome_m1}: {pontos_vida_m1} HP")
    print(f"\n\tVida de {nome_m2}: {pontos_vida_m2} HP")
    return



## lógica de turnos e repetição

# duelo (laço de repetição)
print("\n\n\t\t----- DUELO INICIADO ------")

turno = 1
while pontos_vida_m1 > 0 and pontos_vida_m2 > 0:
    print(f"\n=== TURNO {turno} ===")
    pontos_vida_m2 = atacar(nome_m1, pontos_ataque_m1, nome_m2, pontos_vida_m2)
    # se monstro 2 sobreviver
    if pontos_vida_m2 > 0:
        # monstro 2 vira atacante
        pontos_vida_m1 = atacar(nome_m2, pontos_ataque_m2, nome_m1, pontos_vida_m1)

    exibir_placar(nome_m1, pontos_vida_m1, nome_m2, pontos_vida_m2)

    turno += 1 # aumenta turno


print ("\n\n\t\t----- DUELO FINALIZADO -----") # printa após loop, ou seja, após alguma das vidas zerar

if pontos_vida_m2 == 0:
        print(f"\n\t{nome_m2} foi derrotado por {nome_m1}, que restou com {pontos_vida_m1} HP de vida!!!\n")
else:
        print(f"\n\t{nome_m1} foi derrotado por {nome_m2}, que restou com {pontos_vida_m2} HP de vida!!!\n")  



