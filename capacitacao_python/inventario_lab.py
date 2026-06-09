'''
Contexto:
Em um laboratório de Engenharia Química, os reagentes são recebidos
em grandes remessas, resultando na presença de múltiplos frascos do
mesmo composto e lote na prateleira. Além disso, o armazenamento de
materiais de anos anteriores faz com que um mesmo reagente possa estar
associado a diferentes lotes, cada um com seu respectivo laudo de pureza.
O sistema de inventário exportou os dados atuais dos 30 frascos
disponíveis em três listas separadas:
● nomes dos reagentes;
● códigos de lote (incluindo ano e identificação do produto);
● percentual de pureza (%) correspondente a cada frasco.
Seu papel é desenvolver uma solução em Python para processar essas
informações, identificar os tipos únicos de reagentes disponíveis e
automatizar a seleção de frascos adequados para experimentos que exigem
alta pureza.

Objetivo
Desenvolver um programa em Python que utilize:
● manipulação de iteráveis (set e zip);
● técnica de unpacking em listas de tuplas;
● list comprehension com condicional if.
Todo o desenvolvimento deve ser versionado utilizando Git.
'''

## Base de dados inicial 

# Dados do inventário físico (cada índice representa um frasco individual)

reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona',
'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona', 'Ácido Acético', 'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol', 'Ácido Acético',
'Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico', 'Benzeno', 'Etanol', 'Acetona',
'Metanol', 'Ácido Sulfúrico', 'Acetona', 'Ácido Acético', 'Etanol']

lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01',
'2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01',
'2024-TOL-01', '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02',
'2023-BEN-01', '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01',
'2023-ACE-01', '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01',
'2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01',
'2023-ETA-02']

purezas = [99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8, 99.5, 92.0, 99.2,
96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0, 98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 98.0, 98.5,
95.0, 96.0]

## Passos do programa

# Passo 1: Identificação dos Tipos de Reagentes (Set)

# como set() é uma estrutura de dados que armazena elementos únicos, podemos usá-lo para identificar os tipos únicos de reagentes disponíveis no inventário.
tipos_reagentes = set(reagentes)
print("\nTipos únicos de reagentes disponíveis:", tipos_reagentes)

# para exibir a quantidade, é preciso usar a função len(), que conta o numero de elementos em um iterável. 
print("\nQuantidade de reagentes únicos:", len(tipos_reagentes))


# Passo 2: Estruturação do Inventário (Zip)

# a função zip() é usada para combinar listas em uma única estrutura de dados, onde cada elemento é uma tupla contendo as informações correspondentes das 3 listas juntas.
inventario = list(zip(reagentes, lotes, purezas))
print("\nInventário (reagente, lote, pureza): ")

# loop que vai printar cada item do inventário, onde cada item é uma tupla (lista imutável) contendo as informações do reagente, lote e pureza.
for item in inventario:
    print(item)


# Passo 3: Geração de Relatório (Unpacking)

# pra fazer unpacking, pode fazer com for normal e um print(f"{lote} {reagente} {pureza}")
# ou usando o enumerate(), que percorre a lista e devolve em tuplas tbm

# com for normal:
#for reagentes, lotes, purezas in inventario:
#   print(f"LOTE: [{lotes}] | REAGENTE: [{reagentes}] | PUREZAS: [{purezas}%] ")

# com enumerate()
for indice, (reagente, lote, pureza) in enumerate(inventario):
    print(f"LOTE: [{lote}] | REAGENTE: [{reagente}] | PUREZA: [{pureza}%] ")

# a vantagem do enumerate é que ele literalmente numera os itns, então, se quisesse saber o índice de cada frasco, teria que usar ele


# Passo 4: Filtragem por Critério de Qualidade (List Comprehension)

# experimentos sensíveis exigem pureza >= 98.0%

lotes_aprovados_exp_sensiveis = [lote for reagente, lote, pureza in inventario if pureza >= 98.0]
# [obs] list comprehension: lista = [(o que quer guardar na lista) for (item/ns na lista) in (lista de onde to colocando) if (condição)]
# ou seja, ve na lista original os itens e, se obedecer a condição coloca o que eu falei nessa nova lista
# por isso coloco no começo "lotes", já que essa seria a informação da lista original que eu quero colocar na lista nova
# tenho que colocar "reagentes, lotes, purezas" pq cada item do na lista inventario é uma tupla com essas 3 informações
# e eu quero só uma delas na minha lista nova e quero analisar a condição de só uma delas tbm
print(f"Lotes Aprovados para Experimentos Sensíveis: {lotes_aprovados_exp_sensiveis}")

