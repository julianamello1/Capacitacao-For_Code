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

# monstro 1 (dictionary)
monstro1 = {}
monstro1["nome"] = input("\nNome do monstro 1: ")
monstro1["pontos_vida"] = int(input("\tPontos de vida do monstro 1 (HP): "))
validar(monstro1["pontos_vida"])
monstro1["pontos_ataque"] = int(input("\tPontos de ataque do monstro 1: "))
validar(monstro1["pontos_ataque"])

# monstro 2 (dictionary)
monstro2 = {}
monstro2["nome"] = input("\nNome do monstro 2: ")
monstro2["pontos_vida"] = int(input("\tPontos de vida do monstro 2 (HP): "))
validar(monstro2["pontos_vida"])
monstro2["pontos_ataque"] = int(input("\tPontos de ataque do monstro 2: "))
validar(monstro2["pontos_ataque"])


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
    print(f"\n\tVida de {monstro1["nome"]}: {monstro1["pontos_vida"]} HP")
    print(f"\n\tVida de {monstro2["nome"]}: {monstro2["pontos_vida"]} HP")
    return



## lógica de turnos e repetição

# duelo (laço de repetição)
print("\n\n\t\t----- DUELO INICIADO ------")

turno = 1
while monstro1["pontos_vida"] > 0 and monstro2["pontos_vida"] > 0:
    print(f"\n=== TURNO {turno} ===")
    #monstro 1 ataca
    monstro2["pontos_vida"] = atacar(monstro1["nome"], monstro1["pontos_ataque"], monstro2["nome"], monstro2["pontos_vida"])
    # se monstro 2 sobreviver
    if monstro2["pontos_vida"] > 0:
        # monstro 2 vira atacante
        monstro1["pontos_vida"] = atacar(monstro2["nome"], monstro2["pontos_ataque"], monstro1["nome"], monstro1["pontos_vida"])

    exibir_placar(monstro1["nome"], monstro1["pontos_vida"], monstro2["nome"], monstro2["pontos_vida"])

    turno += 1 # aumenta turno


print ("\n\n\t\t----- DUELO FINALIZADO -----") # printa após loop, ou seja, após alguma das vidas zerar

if monstro2["pontos_vida"] == 0:
        print(f"\n\t{monstro2['nome']} foi derrotado por {monstro1['nome']}, que restou com {monstro1['pontos_vida']} HP de vida!!!\n")
else:
        print(f"\n\t{monstro1['nome']} foi derrotado por {monstro2['nome']}, que restou com {monstro2['pontos_vida']} HP de vida!!!\n")  



