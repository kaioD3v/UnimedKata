# Documentação – Sistema de Triagem de Pacientes

Esse sistema simula uma fila de atendimento hospitalar, onde os pacientes são organizados com base na urgência, idade e horário de chegada.

A ideia é priorizar quem realmente precisa mais, aplicando algumas regras automáticas.

O sistema roda no terminal (console) e tem um menu simples:

1 - Adicionar paciente
2 - Ver fila de atendimento
0 - Sair

A prioridade não é só a urgência original, ela pode mudar:

Menor de idade (< 18) → sobe +1 nível
Idoso (>= 60) com urgência média → vira alta
Máximo de urgência = CRÍTICA (4)

# Níveis de Urgência
Valor
1 - Baixa
2 - Média
3 - Alta
4 - Crítica

# A fila é ordenada por:

Maior urgência primeiro

Quem chegou mais cedo

Ou seja:

Mais grave, passa na frente

Empate, quem chegou antes

# Funções principais

prioridade(p)

Calcula a prioridade real do paciente com base nas regras de idade.

ordenar_fila(pacientes)

Ordena toda a lista de pacientes considerando prioridade e horário.

ler_horario()

Garante que o usuário digite um horário válido no formato HH:MM.

ler_urgencia()

Valida a entrada da urgência (1 a 4).

urgencia_texto(valor)

Transforma número em texto (ex: 2 - "MEDIA").

urgencia_atualizada(p)

Mostra a urgência final depois das regras aplicadas.

exibir_fila(pacientes)

Mostra a fila ordenada no terminal.

# Exemplo de saída:

=== ORDEM DE ATENDIMENTO ===
Maria - Idade: 17 - CRITICA - Chegada: 09:45
João - Idade: 65 - ALTA - Chegada: 09:40
Estrutura dos dados

Cada paciente é um dicionário assim:

{
  "nome": "João",
  "idade": 65,
  "urgencia": 2,
  "chegada": "09:40"
}


# Como executar

python filaDeTriagem.py


# Observações
O sistema é local (não salva em banco)
Tudo fica em memória (lista pacientes)
Já tem validação básica de entrada
Sempre que adiciona paciente, já mostra fila atualizada

# Possíveis melhorias

salvar em banco de dados
interface gráfica
sistema multiusuário
adicionar tempo de espera
remover paciente atendido