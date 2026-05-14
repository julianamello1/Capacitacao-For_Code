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

custo_diario_da_hospedagem = float(input("Qual é o custo da hospedagem, em reais? "))

qntd_dias = int(input("Qual a duração da viagem, em dias? "))

# organização e checagem dos dados inseridos:

print(f"\nPerfeito! Segundo seus dados inseridos, você fará uma viagem para {destino}, durante {qntd_dias} dias.")
print(f"\nSeu orçamento é de R$ {orcamento_disponivel}. O valor da passagem é de R$ {custo_da_passagem} e o da diária da hospedagem, R$ {custo_diario_da_hospedagem}.")


## lógica e cálculos

# converter moeda (função) = valor em reais x 6.10:
def conversao_real_euro(valor_em_reais):
    return valor_em_reais * 6.10

# calcular hospedagem (função) = valor da hospedagem (diário) x quantidade de dias:
def calculo_hospedagem(valor_hospedagem, qntd_dias):
    return valor_hospedagem * qntd_dias

# calcular custo total (função) = valor passagem + total hospedagem:
def calculo_custo_total(valor_passagem, valor_total_hospedagem):
    return valor_total_hospedagem + valor_passagem

# validação do orçamento (função) = se custo_total for <= orçamento_disponivel, POSSÌVEL
# se custo_total > orçamento_disponível, NÃO POSSÌVEL
def validacao_orcamento(custo_total, orcamento_disponivel):
    if(custo_total <= orcamento_disponivel):
        print("\n\tDe acordo com os custos totais e o orçamento disponível, sua viagem é viável!")
        return True
    else:
        print(f"\n\tInfelizmente, por conta do orçamento, essa viagem não seria possível :( )")
        return False

# status final da viagem (função) = viavel se orçamento valido && qntd dias > 0
# calculo do quanto sobrará (orçamento - custo) ou quanto faltará (custo - orçamento)