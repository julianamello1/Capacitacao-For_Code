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