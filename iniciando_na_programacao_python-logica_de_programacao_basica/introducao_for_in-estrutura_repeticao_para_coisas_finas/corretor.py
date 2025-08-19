# atividade 1 

# cargo = input("Digite o Cargo do funcionario:").lower()
# dia = input("Digite o Cargo do funcionario:").lower()

# if cargo == "gerente":
#     print("Acesso permitido")
# elif cargo == "analista" and dia in ["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira"]:
#     print("Acesso permitido")
# elif cargo == "estagiario" and dia in ["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira"]:
#     print("Acesso permitido")
# else:
#     print("Vaza daqui")

# atividade 2




# distancia = int(input("Digite a distancia percorrida (km): "))
# combustivel = float(input("Digite o total de combustivel gasto(L):"))

# consumo = distancia/combustivel

# print(f"{consumo:.1f} km/l")





# funcoes 

def recomendar_sala(participantes,tipo_reuniao):
    if participantes < 0:
        return "numero de participantes invalido. "
    
    if tipo_reuniao == "executiva":
        return "Sala Grande"
    elif participantes <= 5:
        return "Sala Pequena"
    elif participantes <= 15:
        return "Sala média"
    else: 
        return "Sala Grande"
participantes = int(input("Digite o numero de participantes: "))
tipo = input("Digite o tipo de reunião (normal/executiva):").lower()

print("recomendação:" , recomendar_sala(participantes,tipo))





def classificar_ped(valor_pedido,dias_para_entrega):
    if valor_pedido < 100 or dias_para_entrega > 7:
        return "normal"
    elif (100 <= valor_pedido <= 500) or (4 <= dias_para_entrega <= 7):
        return "Prioritario"
    elif valor_pedido > 500 or dias_para_entrega < 4:
        return "Urgente"
    else:
        return "indefinido"

valor = float(input("digite o valor do pedido: "))
dias = int(input("Digite os dias restantes para a Entrega: "))

print("Classificação: ", classificar_ped(valor,dias))
