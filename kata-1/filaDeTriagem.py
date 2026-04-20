# calcula a prioridade, se irá atualizar ou não, considerando idade e urgência original
def prioridade(p):
    nivel = p["urgencia"]

    if p["idade"] < 18: # menor de idade sobe o nivel de urgência
        nivel += 1

    if p["idade"] >= 60 and nivel == 2: # idoso com urgência média sobe para alta
        nivel = 3

    return nivel


def ordenar_fila(pacientes): # ordena por urgência (considerando atualizações) e depois por horário de chegada
    def criterio(p):
        return (-prioridade(p), p["chegada"])

    return sorted(pacientes, key=criterio)

def ler_horario(): # lê o horário de chegada, garantindo o formato HH:MM
    while True:
        h = input("Chegada (HH:MM): ")
        try:
            horas, minutos = map(int, h.split(":"))
            if 0 <= horas < 24 and 0 <= minutos < 60:
                return h
        except:
            pass
        print("Formato inválido! Use HH:MM (ex: 09:30)")

def ler_urgencia(): # lê a urgência, garantindo que seja um número entre 1 e 4, e que não ocorra nenhum erro de entrada
    while True:
        print("Urgência: 1=BAIXA | 2=MEDIA | 3=ALTA | 4=CRITICA")
        try:
            valor = int(input("Escolha: "))
            if valor in [1, 2, 3, 4]:
                return valor
            else:
                print("Digite um número entre 1 e 4!")
        except:
            print("Entrada inválida!")

def urgencia_texto(valor): # converte o valor numérico da urgência para texto
    if valor == 1:
        return "BAIXA"
    elif valor == 2:
        return "MEDIA"
    elif valor == 3:
        return "ALTA"
    else:
        return "CRITICA"

def urgencia_atualizada(p): # calcula a urgência efetiva, considerando as regras de prioridade, mas limitando o nível máximo a 4 (CRITICA)
    nivel = prioridade(p)
    nivel = min(nivel, 4)
    return urgencia_texto(nivel)

def exibir_fila(pacientes): # exibe a fila de atendimento, mostrando a urgência final
    fila = ordenar_fila(pacientes)

    print("\n=== ORDEM DE ATENDIMENTO ===")
    for p in fila:
        original = urgencia_texto(p["urgencia"])
        atualizada = urgencia_atualizada(p)
        if original != atualizada:
            status = f"{atualizada}"
        else:
            status = original

        print(f"{p['nome']} - Idade: {p['idade']} - {status} - Chegada: {p['chegada']}")

# lista inicial

pacientes = [
    {"nome": "Guilherme", "idade": 25, "urgencia": 2, "chegada": "09:30"},
    {"nome": "Maria", "idade": 17, "urgencia": 3, "chegada": "09:45"},
    {"nome": "João", "idade": 65, "urgencia": 2, "chegada": "09:40"},
    {"nome": "Ana", "idade": 30, "urgencia": 1, "chegada": "09:35"}
]


# menu inicial

while True:
    print("\n SISTEMA DE TRIAGEM")
    print("1 - Adicionar paciente")
    print("2 - Ver fila de atendimento")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1": # adicionar paciente
        print("\nNovo paciente")

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        urgencia = ler_urgencia()
        chegada = ler_horario()

        # adiciona o paciente à lista.

        pacientes.append({ 
            "nome": nome,
            "idade": idade,
            "urgencia": urgencia,
            "chegada": chegada
        })

        print("Paciente adicionado com sucesso!")
        exibir_fila(pacientes)

    elif opcao == "2": # exibir fila de atendimento
        exibir_fila(pacientes)

    elif opcao == "0": # sair do sistema
        print("Encerrando sistema...")
        break

    else: # opção inválida
        print("Opção inválida!")