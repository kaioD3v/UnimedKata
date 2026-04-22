Nome: Kaio Matheus Abdon de Moura
Telefone: (81) 9 7327-1298
Email: kaio15matheus@gmail.com

Nesses Katas, eu usei basicamente Python, React com TypeScript e MySQL, e escolhi cada um pensando no que fazia mais sentido pra resolver cada parte.

No Python, eu usei ele tanto na lógica da triagem quanto na API com Flask e no pipeline de dados. Escolhi Python porque é uma linguagem que eu já tenho mais facilidade e ela é muito boa pra escrever regras de negócio de forma clara, tipo o cálculo de prioridade dos pacientes. No caso do Flask, usei porque ele é bem simples e direto pra criar API, não precisa de muita configuração e já dá pra montar um backend funcional rápido. Já no pipeline, o Python ajuda muito com bibliotecas como pandas e numpy, que facilitam bastante na hora de limpar e tratar dados bagunçados (tipo datas em formatos diferentes e valores com vírgula).

No frontend, usei React com TypeScript. React porque é o que o mercado usa bastante e facilita muito separar a interface em componentes, deixando tudo mais organizado. E o TypeScript eu usei pra evitar erro bobo, principalmente na comunicação com a API, já que ele ajuda com tipagem e deixa o código mais previsível. Também usei axios pra fazer as requisições, porque é simples e funciona bem.

No banco de dados, usei MySQL. Escolhi ele porque é um banco relacional bem conhecido e confiável, além de ser fácil de integrar com Python usando pymysql. Como o projeto tem relacionamento entre dados (tipo paciente, fila, tarefas), o modelo relacional faz sentido porque ajuda a manter tudo organizado e consistente. Usei chave primária, estrangeira e UNIQUE pra garantir que não tenha dado duplicado ou errado. No geral, escolhi essa stack porque é prática, funciona bem junto e é bem próxima do que o mercado usa. Como ainda sou dev júnior, foquei em usar tecnologias que eu já tenho alguma familiaridade, mas que também são profissionais e escaláveis.


# As instruções para executar cada kata localmente estão nos docs dos respectivos katas


Se eu tivesse mais tempo, eu melhoraria principalmente a organização e a robustez do projeto como um todo. Hoje ele funciona bem, mas ainda está mais no nível de protótipo funcional. No backend, eu separaria melhor as responsabilidades, criando uma estrutura mais organizada (controllers, services, repositories), ao invés de deixar tudo mais direto no Flask. Também adicionaria validações mais completas e tratamento de erros mais detalhado, além de implementar autenticação básica na API.

No banco de dados, eu evoluiria o modelo, talvez adicionando mais controle de histórico (ex: mudanças de status das tarefas ou da fila), além de pensar melhor em índices para performance se o volume de dados crescesse. No frontend, eu melhoraria a experiência do usuário, adicionando feedbacks visuais (loading, erro, sucesso), e organizaria melhor os componentes. Também poderia usar algo como gerenciamento de estado mais estruturado se a aplicação crescesse.

Na parte do pipeline, eu deixaria ele mais próximo de um cenário real, talvez separando em etapas mais modulares, adicionando logs mais completos e tratamento de falhas, além de pensar em automatização (tipo rodar por agendamento). No geral, com mais tempo eu focaria em deixar o projeto mais próximo de um ambiente de produção, com melhor organização, escalabilidade e manutenção, e não só funcionando corretamente.
