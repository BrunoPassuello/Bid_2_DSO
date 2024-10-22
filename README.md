# Bid_2_DSO
# Trabalho 1 - Gestão Contratual e Organizacional de Clubes em Campeonatos

## Alunos:
- Henrique Rafael Sousa de Oliveira
- Bruno Correa Passuello

## Problema:
Implementar um sistema Orientado a Objetos que gerencie os dados contratuais e organizacionais de clubes em campeonatos.

## Escopo do Desenvolvimento:
O registro de jogadores é fundamental na organização dos clubes e para garantir a integridade e as boas práticas das competições. Por exemplo: impedindo que um jogador saia de um clube e jogue imediatamente contra seu time anterior, por uma nova equipe.

Tendo isso em vista, é necessário a implementação de regras e principalmente o controle de quais jogadores estão registrados em quais clubes, bem como seus salários e multas rescisórias.

Cada clube tem seu nome, cidade, lista de contrato de jogadores, lista de campeonatos em que participa e técnico. Quanto a suas ações, pode contratar e demitir jogadores e técnicos, alterar ou renovar contratos dos mesmos, bem como entrar e sair de campeonatos.

Cada jogador é registrado por um, e apenas um, clube. Possui posição, altura, peso, informação se é estrangeiro ou não e também possui contrato. Quanto a suas ações. Já o contrato por sua vez possui: clube, jogador, salário, multa rescisória e pode ou não ter cláusula de produtividade. Enquanto a posição possui apenas nome.

Os técnicos possuem apenas um tipo de licença e contrato. Tanto técnico quanto jogador herdam da classe Pessoa que possui nome, idade e cidade. Já a classe licença possui apenas tipo, enquanto a classe contrato técnico possui clube, técnico, salário e multa rescisória.

Já os campeonatos possuem nome, premiação, lista de clubes e regras. Quanto à regra, que está diretamente associada ao campeonato, ela possui número de times por clube, número de estrangeiros máximo permitido na competição, bem como número máximo de jogadores relacionados permitidos na competição.

O sistema permitirá o relatório de qual a maior e menor folha salarial, bem como qual a maior e menor multa rescisória, para eventual comparação destas informações entre os times da competição, como por exemplo primeiro e segundo lugar, o primeiro e último lugar.

### Considerações de Restrição:
1. Um jogador não pode ser registrado por 2 ou mais clubes.
2. Nenhum clube que exceda a quantidade de jogadores estrangeiros permitida será considerado. Desclassificação imediata.

## Divisão das Funções da Dupla:
- **Bruno**: Implementação das entidades e da maior parte dos métodos, design/modelagem do UML.
- **Henrique**: Implementação das verificações e dos testes, documentação do sistema.