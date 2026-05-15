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

custo_diario_da_hospedagem = float(input("Qual é o custo da hospedagem, em euros? "))

qntd_dias = int(input("Qual a duração da viagem, em dias? "))

# organização e checagem dos dados inseridos:

print(f"\nPerfeito! Segundo seus dados inseridos, você fará uma viagem para {destino}, durante {qntd_dias} dias.")
print(f"Seu orçamento é de R${orcamento_disponivel}, o valor da passagem é de R${custo_da_passagem} e o da diária da hospedagem, {custo_diario_da_hospedagem} euros.")


## lógica e cálculos

# converter moeda (função) = valor em euro x 6.10:
def conversao_euro_real(valor_em_euro):
    return valor_em_euro * 6.10

# calcular hospedagem (função) = valor da hospedagem (diário) x quantidade de dias:
def calculo_hospedagem(valor_hospedagem_euro, qntd_dias):
    valor_hospedagem_convertido = conversao_euro_real(valor_hospedagem_euro) # primeiro converte o valor
    print(f"O valor total da hospedagem convertido para reais é R${valor_hospedagem_convertido}")
    return valor_hospedagem_convertido * qntd_dias # depois calcula o total

# calcular custo total (função) = valor passagem + total hospedagem:
def calculo_custo_total(valor_passagem, valor_total_hospedagem):
    return valor_total_hospedagem + valor_passagem

# validação do orçamento (função) = se custo_total for <= orçamento_disponivel, POSSÌVEL
# se custo_total > orçamento_disponível, NÃO POSSÌVEL
def validacao_orcamento(custo_total, orcamento_disponivel):
    if(custo_total <= orcamento_disponivel):
        print("\n\tDe acordo com os custos totais e o dinheiro disponível, seu orçamento parece possível!")
        return True
    else:
        print(f"\n\tInfelizmente, esse orçamento parece não ser possível :( ")
        return False

# status final da viagem (função) = viavel se orçamento valido && qntd dias > 0
# calculo do quanto sobrará (orçamento - custo) ou quanto faltará (custo - orçamento)
def status_viagem(validacao_orcamento, orcamento_disponivel, custo_total, qntd_dias):
    if validacao_orcamento and qntd_dias > 0:
        sobra = orcamento_disponivel - custo_total
        print(f"\tSua viagem é VIÁVEL!!! :D E ainda sobram R$ {sobra}!!!")
        return True
    else:
        falta = custo_total - orcamento_disponivel
        print(f"\tPoxa, sua viagem realmente não é viável :( Faltam R$ {falta} para fazer acontecer.....(ou a duração inserida é inválida)")
        return False
    

## calculando os valores com as funções

# valor da hospedagem convertido de euro pra real
total_hospedagem_real = calculo_hospedagem(custo_diario_da_hospedagem, qntd_dias)

# custo total
custo_total_viagem = calculo_custo_total(custo_da_passagem, total_hospedagem_real)

## validando orçamento
orcamento_valido = validacao_orcamento(custo_total_viagem, orcamento_disponivel)

## definindo status da viagem
eh_viavel = status_viagem(orcamento_valido, orcamento_disponivel, custo_total_viagem, qntd_dias)

