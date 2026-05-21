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

## entrada de dados e tipos

# monstro 1 
nome_m1 = input("\nNome do monstro 1: ")
pontos_vida_m1 = int(input("\nPontos de vida do monstro 1 (HP): "))
pontos_ataque_m1 = int(input("Pontos de ataque do monstro 1: "))

# monstro 2 
nome_m2 = input("\nNome do monstro 2: ")
pontos_vida_m2 = int(input("\nPontos de vida do monstro 2 (HP): "))
pontos_ataque_m2 = int(input("Pontos de ataque do monstro 2: "))


## funções

# função de atacar
def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):
    dano = pontos_vida_m1 - pontos_ataque_m2
    vida_atualizada = pontos_vida_m1 - dano
    print(f"\n\t{nome_atacante} atacou {nome_defensor} e causou {dano} de dano!!!!")
    print(f"\n\t\tVida atual de {nome_defensor}: {vida_atualizada} HP")
    return vida_atualizada

# função que exibe placar
def exibir_placar(nome_m1, pontos_vida_m1, nome_m2, pontos_vida_m2):
    print(f"\n\tVida de {nome_m1}: {pontos_vida_m1} HP")
    print(f"\n\tVida de {nome_m2}: {pontos_vida_m2} HP")
    return

