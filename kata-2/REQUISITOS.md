5. O cliente pediu uma opção chamada “ver minhas tarefas”, que gera uma ambiguidade quando entende, se sistema será multiusuário (com login e banco de dados entre usuários e tarefas) ou local (com armazenamento simples)? Sem essa definição, fico em duvida para decidir a estrutura do sistema.

Além disso é preciso esclarecer se as tarefas terão apenas dois estados (pendentes/concluída) ou também incompletas (como “em andamento”), também não está definido o que acontece ao marcar como feita.

E por fim não foi definido se será possível editar tarefas ou apenas excluir e recriar. Também faltam regras importantes, como limite de caracteres do título e se ele pode ser vazio, o que dificulta o desenvolvimento perfeito da aplicação.

6. Perguntaria ao cliente se “minhas tarefas” implica contas individuais com login ou uma lista compartilhada. Sem resposta, adotaria um sistema monousuário/local, sem login, mas com banco de dados estruturado para suportar usuários no futuro.

Também questionaria se existem apenas os estados “pendentes” e “concluída” ou se há intermediários como “em andamento”, além de como exibir tarefas concluídas. Na ausência de definição, implementaria três estados (pendentes, em andamento e concluída), mantendo as concluídas visíveis e riscadas para melhor organização.

Por fim, perguntaria se tarefas podem ser editadas. Sem retorno, permitiria tanto edição quanto exclusão, garantindo uma experiência mais prática e alinhada ao uso comum.


7.  Requisitos Funcionais (RF)

RF01 – O sistema deve permitir a criação de tarefas com um título.
RF02 – O sistema deve permitir a visualização de todas as tarefas cadastradas em uma lista.
RF03 – O sistema deve permitir a edição do título de uma tarefa existente.
RF04 – O sistema deve permitir a exclusão de tarefas.
RF05 – O sistema deve permitir marcar tarefas com diferentes estados: “a fazer”, “em andamento” e “concluída”.
RF06 – O sistema deve permitir filtrar as tarefas por estado (a fazer, em andamento, concluída).
RF07 – O sistema deve exibir tarefas concluídas de forma diferenciada (ex: texto riscado).
RF08 – O sistema deve armazenar as tarefas em um banco de dados.
RF09 – O sistema deve funcionar como aplicação monousuário, sem necessidade de autenticação no MVP.
RF10 – O sistema deve possuir estrutura preparada para futura implementação de múltiplos usuários.

Requisitos Não Funcionais (RNF)

RNF01 – O sistema deve ter interface simples e intuitiva, adequada para uso pessoal.
RNF02 – O sistema deve apresentar tempo de resposta rápido para operações de CRUD (até 2 segundos).
RNF03 – O sistema deve garantir persistência dos dados utilizando banco de dados (ex: MySQL).
RNF04 – O sistema deve ser escalável, permitindo futura implementação de autenticação e múltiplos usuários.
RNF05 – O sistema deve validar entradas de dados (ex: impedir títulos vazios).
RNF06 – O sistema deve seguir boas práticas de organização de código (separação entre frontend, backend e banco de dados).
RNF07 – O sistema deve ser compatível com navegadores modernos (ex: Chrome, Edge, Firefox).
RNF08 – O sistema deve manter consistência visual na exibição dos estados das tarefas.

8. Eu trataria esse requisito como item de menor prioridade no backlog, sem entrar no escopo do MVP, mas já estruturado para não gerar retrabalho depois e uma restruturação completa no código.