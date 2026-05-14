''' 
#Contexto
Mariana é uma nômade digital que precisa organizar suas finanças para sua
próxima viagem à Europa. Ela possui um orçamento total em Reais (BRL), mas seus
gastos planejados estão em diferentes moedas e categorias.
Para ajudá-la, você deve desenvolver um programa em Python que processe
esses dados, realize as conversões necessárias e verifique se o orçamento de
Mariana é suficiente para cobrir os custos previstos.

#Objetivo
Desenvolver um programa em Python que utilize lógica de programação e tipos de
dados fundamentais para calcular o balanço financeiro de uma viagem e versionar
o progresso via Git.

'''

## entradas dos dados

#obs: se nao for string no input, tem que fazer o casting

orcamento_disponivel = float(input("Qual o orçamento disponível para a sua viagem, em reais? "))

destino = input("Qual é o destino da sua viagem? ")

custo_da_passagem = float(input("Qual é o valor da passagem, em reais? "))

custo_da_hospedagem = float(input("Qual é o custo da hospedagem, em reais? "))

qntd_dias = int(input("Qual a duração da viagem, em dias? "))

# organização e checagem dos dados inseridos:

print(f"\nPerfeito! Segundo seus dados inseridos, você fará uma viagem para {destino}, durante {qntd_dias} dias.")
print(f"\nSeu orçamento é de R$ {orcamento_disponivel}. O valor da passagem é de R$ {custo_da_passagem} e o da hospedagem, R$ {custo_da_hospedagem}.")


