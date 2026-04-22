1. Para datas, criei uma função que tenta converter a string testando cada formato um por um até algum funcionar. Se nenhum funcionar, retorna nulo. A decisão foi descartar pedidos com data nula porque sem ela não tem como calcular atraso — qualquer número que viesse daí estaria errado. Em produção isso precisaria gerar um alerta pra investigar de onde veio o dado ruim.

Para valores monetários, a função detecta se tem vírgula no número e converte pro padrão com ponto antes de virar float. Pedido com valor nulo foi preenchido com 0 em vez de descartado porque era um pedido cancelado, então zero faz sentido.

Para os órfãos em entregas, a decisão foi remover antes de fazer qualquer join. Não tem como consolidar uma entrega sem o pedido pai, qualquer cálculo ficaria incompleto. Numa situação real eu salvaria esses registros num arquivo separado pra auditoria em vez de só jogar fora.

Para cidades, o problema era "São Paulo", "sao paulo" e "SAO PAULO" sendo tratados como três cidades diferentes. Resolvi com unidecode() pra remover acento e .title() pra padronizar a capitalização. Os três viram "Sao Paulo" e agrupam certinho nos indicadores.

2. Sim, Rodar duas vezes produz o mesmo resultado porque o pipeline sempre sobrescreve os arquivos de saída, nunca acumula. Cada execução lê os CSVs do zero, aplica as mesmas transformações e grava por cima do que já existia, se tivesse um append em algum ponto, na segunda execução os registros apareceriam duplicados e o resultado mudaria. Como não tem, o comportamento é sempre o mesmo independente de quantas vezes rodar.

3. O problema principal é que hoje o pipeline carrega tudo na memória de uma vez com pandas. Com 10 milhões de linhas isso provavelmente estouraria a RAM ou ficaria muito lento, a primeira mudança seria usar Polars no lugar do pandas. Ele faz as mesmas operações mas é muito mais rápido e consome menos memória porque foi escrito em Rust. A API é parecida, então a migração não seria tão difícil.

Se o volume fosse ainda maior, a próxima opção seria mover os joins pra um banco de dados como PostgreSQL, porque banco é otimizado pra isso e consegue trabalhar sem carregar tudo na memória. Python ficaria só buscando o resultado final, além disso, com execução diária precisaria de alguma ferramenta pra agendar e monitorar, tipo Airflow, porque rodar python pipeline.py na mão todo dia não escala e não avisa quando quebra.

4. Usaria pytest e separaria em três partes, a primeira seriam testes unitários das funções isoladas, verificando se parse_data() entende cada um dos formatos de data, se parse_valor() converte "2.300,50" pra 2300.50, se normalizar_cidade() transforma "SAO PAULO" em "Sao Paulo", e se cada uma delas lida bem com valor vazio ou nulo sem quebrar.

A segunda seriam testes de integração rodando o pipeline com um CSV pequeno controlado, verificando se o atraso é calculado certo (previsto dia 10, realizado dia 15 deve dar 5), se órfãos são removidos e não aparecem no consolidado, e se o schema final tem exatamente as 11 colunas esperadas.

A terceira seriam verificações de qualidade no arquivo de saída, como checar se tem duplicata no id_pedido, se algum valor_total ficou negativo, e se os valores de status_entrega são só os esperados. Esse tipo de teste pega corrupções de dado que passariam despercebidas nos outros dois.

feat and doc: adicionando a automação pipeline, junto com outra automação para gerar dados sujos, além de adiconar a documentação