# Diagnostico

1. A causa raiz da lentidão é um backend desorganizado, com muitas funções acumuladas e várias requisições desnecessárias, o que sobrecarrega o sistema em horários de pico e mostra falta de otimização e estrutura. O risco é que o sistema não consiga responder bem sob alta demanda, causando lentidão, falhas ou até indisponibilidade, impactando diretamente a experiência do usuário e gerando perda de vendas e confiança. Por isso, é um problema urgente e importante, pois já afeta o funcionamento em momentos críticos e o resultado do negócio.

2.A duplicidade de pedidos ocorre devido ao acúmulo de funções e falta de organização no código, onde diferentes partes podem executar a mesma ação sem controle, principalmente com muitas requisições simultâneas e sem validação adequada. O risco é a continuidade desses erros, gerando inconsistência nos dados, cobranças indevidas, problemas logísticos e prejuízo financeiro, além de perda de confiança dos clientes. É um problema urgente e importante, pois já aconteceu em produção e impacta diretamente operações e receita.

3.O bug de frete corrigido direto em produção mostra um código desorganizado, com funções acumuladas e sem separação clara, além da ausência de processo como testes e revisão, o que leva a correções inseguras. O risco é a introdução de novos erros sem perceber, causando cálculos incorretos, prejuízo financeiro e falhas em cascata no sistema. Por isso, é um problema importante e urgente, pois mesmo corrigido, ainda representa alto risco de instabilidade e novos problemas ocultos.

4. O arquivo com mais de 4000 linhas é resultado do acúmulo de funções e regras de negócio sem organização ou arquitetura definida, onde tudo é implementado no mesmo lugar sem padronização. O risco é tornar o sistema difícil de manter e evoluir, aumentando a chance de erros, bugs em cascata e retrabalho, além de impactar a qualidade das entregas. É um problema importante, mas não urgente no curto prazo, pois não quebra o sistema imediatamente, mas sustenta vários outros problemas.

5.A ausência de testes automatizados vem da falta de organização e processo, onde o foco está apenas em entregar rápido, acumulando código sem planejamento e sem validação. O risco é que erros passem despercebidos e se espalhem pelo sistema, gerando bugs em produção, instabilidade, retrabalho e prejuízo para o negócio. É um problema extremamente importante, mas não urgente de forma imediata, pois não causa falha instantânea, mas compromete toda a base do sistema a longo prazo.


# Ações 

Para profissionalizar o sistema e estancar os erros mais críticos, a primeira medida será uma refatoração estrutural e otimização, o foco será decompor o arquivo principal em módulos menores e mais organizados, além de implementar um sistema de cache para aliviar as requisições repetitivas que sobrecarregam o banco. O tempo estimado para essa organização é de 5 a 8 dias, e saberemos que deu certo quando a lentidão do sistema cair consideravelmente e o servidor parar de apresentar picos de fluxo em horários de alta demanda.

Na sequência, precisamos resolver a duplicidade de pedidos através de uma trava contra cliques duplos, a solução técnica consiste em gerar um identificador único para cada transação no frontend, garantindo que o backend processe a operação apenas uma vez, mesmo que receba múltiplos cliques ou requisições simultâneas. Essa tarefa deve levar entre 3 a 4 dias de desenvolvimento e testes. O critério de sucesso será a ausência total de registros duplicados no banco de dados, a partir de testes de caixa cinza, garantindo a integridade financeira das operações.

Por fim, a terceira prioridade é criar uma sequência de testes antes do deploy, funcionando como um "ensaio geral" para garantir que nenhuma correção quebre o site ao vivo, vamos configurar um servidor idêntico ao oficial onde testaremos as mudanças primeiro, impedindo qualquer alteração direta no código que está rodando para os clientes. Esse ajuste de infraestrutura deve levar de 2 a 3 dias, e saberemos que o problema foi resolvido quando todas as atualizações forem validadas nesse ambiente seguro antes de chegarem à produção, eliminando erros inesperados e "gambiarras" de última hora.


# Decisão de arquitetura

Escolho a Opção A, pois, em um sistema em produção sem testes e com o time ocupado, uma reescrita do zero (Opção B) geraria um risco altíssimo de "parar o negócio" por bugs imprevistos. A extração gradual permite criar uma rede de segurança (testes) enquanto limpamos o código, garantindo estabilidade e entregas constantes sem comprometer a operação atual.

# RNF

A Capacidade de Crescimento está prejudicada porque, como o código está "pesado" e desorganizado, o sistema não aguenta um aumento súbito de acessos, se a loja crescer e o número de clientes dobrar amanhã, o backend atual provavelmente não daria conta do recado e para acompanhar isso, podemos medir o Volume de Pedidos por Minuto, observando até que ponto o sistema processa as vendas com sucesso antes de começar a apresentar lentidão.

A Disponibilidade também é um problema, pois um site que trava ou apresenta erros de frete no momento do pico é, na prática, um site que está fora do ar para o cliente, se o usuário não consegue concluir a jornada de compra, a confiança na marca é perdida. O ideal aqui é o Tempo de Funcionamento, que monitora a porcentagem de tempo que o sistema ficou totalmente disponível e sem erros para os usuários durante o mês.

Por fim, a Organização das Informações está em risco devido às duplicidades e correções improvisadas, o que deixa o banco de dados confuso. Isso pode causar problemas sérios, como o estoque dizer que tem um produto que já foi vendido duas vezes por erro e para controlar isso, podemos usar o Índice de Conflitos, que verifica quantos registros no banco de dados precisam ser corrigidos manualmente por estarem duplicados ou com informações erradas.