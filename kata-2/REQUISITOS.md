5. O cliente pediu uma opção chamada “ver minhas tarefas”, que gera uma ambiguidade quando entende, se sistema será multiusuário (com login e banco de dados entre usuários e tarefas) ou local (com armazenamento simples)? Sem essa definição, fico em duvida para decidir a estrutura do sistema.

Além disso é preciso esclarecer se as tarefas terão apenas dois estados (a fazer/concluída) ou também incompletas (como “em andamento”), também não está definido o que acontece ao marcar como feita.

E por fim não foi definido se será possível editar tarefas ou apenas excluir e recriar. Também faltam regras importantes, como limite de caracteres do título e se ele pode ser vazio, o que dificulta o desenvolvimento perfeito da aplicação.

6. Perguntaria ao cliente se “minhas tarefas” implica contas individuais com login ou uma lista compartilhada. Sem resposta, adotaria um sistema monousuário/local, sem login, mas, a estrutura de dados (com ID das tarefas) permite futura adaptação para múltiplos usuários.

Também questionaria se existem apenas os estados “pendentes” e “concluída” ou se há intermediários como “em andamento”, além de como exibir tarefas concluídas. Na ausência de definição,optei por uma abordagem simples com dois estados: “a_fazer” e “concluida”, essa decisão foi baseada na lógica já implementada no código, incluindo: botão de alternância de status, filtro por estado e estilização de tarefas concluídas (texto riscado)

Por fim, perguntaria se tarefas podem ser editadas. Sem retorno, permitiria edição via modal.


7.  Requisitos Funcionais (RF)

RF01 – O sistema deve permitir a criação de tarefas com título válido (não vazio).
RF02 – O sistema deve exibir todas as tarefas em lista.
RF03 – O sistema deve permitir editar o título de uma tarefa por meio de um modal.
RF04 – O sistema deve permitir excluir tarefas.
RF05 – O sistema deve permitir alternar o estado da tarefa entre “a_fazer” e “concluida”.
RF06 – O sistema deve permitir filtrar tarefas por estado.
RF07 – O sistema deve exibir tarefas concluídas com estilo visual diferenciado (riscado).
RF08 – O sistema deve consumir dados de uma API REST para persistência.
RF09 – O sistema deve funcionar como aplicação monousuário no MVP.
RF10 – O sistema deve permitir fechar o modal de edição via clique fora ou tecla ESC.
RF11 – O sistema deve evitar atualização quando não houver alteração no título da tarefa.

Requisitos Não Funcionais (RNF)

RNF01 – O sistema deve possuir interface simples e intuitiva.
RNF02 – O sistema deve apresentar resposta rápida nas operações de CRUD.
RNF03 – O sistema deve garantir persistência via backend (API REST).
RNF04 – O sistema deve ser estruturado para futura escalabilidade (multiusuário).
RNF05 – O sistema deve validar entradas (ex: impedir título vazio).
RNF06 – O sistema deve seguir boas práticas de separação entre frontend e backend.
RNF07 – O sistema deve ser compatível com navegadores modernos.
RNF08 – O sistema deve manter consistência visual nos estados das tarefas.
RNF09 – O sistema deve utilizar componentes reativos (React) para atualização dinâmica da interface.


8. Eu trataria esse requisito como item de menor prioridade no backlog, sem entrar no escopo do MVP, mas já estruturado para não gerar retrabalho depois e uma restruturação completa no código.