1. Utilizei uma lista em Python porque ela é simples e funcional, e a lógica dela está presente nas tecnologias atuais como em array e em Jsons, além da facilidade de inserção de dados utilizando o append e flexibilidade pois cada elemento dentro da lista é um dicionario e pode mudar a qualquer momento.

2. O sorted fica mais lento conforme a lista cresce, com 1 milhão de pacientes ainda funciona, mas demora mais porque reordena tudo do zero toda vez que a fila é consultada. Uma das soluções seria usar um heap talvez, que já mantém a ordem automaticamente a cada inserção, sem precisar reordenar tudo sempre. 

3. Sim, interagem. A regra 5 roda primeiro e sobe nivel de 2 para 3, então quando a regra 4 checa nivel == 2 o valor já foi modificado. Não causa problema porque idade >= 60 já é falso. O paciente entra com urgência média e sobe para urgência alta.

4. O código atual lidaria mal, porque todas as regras estão dentro de prioridade(), adicionar uma 6ª regra iria mexer diretamente nessa função, o que aumenta o risco de quebrar as regras existentes por causa da dependência entre elas.


obs: todos os testes foram feitos a partir dos inputs no terminal