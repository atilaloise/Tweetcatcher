# Plano de trabalho

## Introdução 

Este projeto se encaixa em um contexto de testes para posição de SRE/DevOps, se faz necessário medir o nível de conhecimento e habilidades em múltiplas ferramentas que em conjunto entreguem uma aplicação com valor agregado relevante.

## Justificativa

O monitoramento de atividade e tópicos em alta no Twitter tem grande potencial para que empresas, profissionais da área de dados e produtores de conteúdo possam direcionar suas campanhas, identificar oportunidades e direcionar o esforço corporativo para atender áreas de interesse ou até mesmo identificar novos nichos de mercado.

## Metas

### Construir uma aplicação para coleta de tweets vinculados a uma ou várias hashtags.

Para tal fixa-se as seguintes bases:

- Capturar até 100 Tweets para cada #tag;
- Armazenar Tweets em uma base de dados de forma com que seja possível recuperar tais informações;
- Apresentar o TOP 5 users da amostra baseado na quantidade de seguidores;
- Apresentar o total de Tweets agrupados por hora do dia, independente da hashtag;
- Apresentar o total de Tweets contando cada hashtag, agrupando por idioma/país do usuário;
- Expor as apresentações de dados através de uma API, expondo métricas de execução;
- Criar uma interface web para interação com a API e apresentação dos resultados;

### Mostrar eventos de execução da API em tempo real 

- Implementar ferramenta de Logging;
- Criar Queries para Warnings, Errors, Debug, Info, etc.;
- Implementar ferramenta de Monitoramento;
- Criar Dashboard de Numero de execuções;
- Criar Dashboard de Tempo de execução (latência);
- Criar Dashboard de quantidade de erros de API;


## Recursos necessários 

Para atingir as metas declaradas será necessário:

- Criação de repositório Git para versionamento da aplicação;
- Definir Estrutura de pastas do projeto;
- Definir arquitetura e fluxos;
- Conta de desenvolvedor no Twitter
- App criado na conta de desenvolvedor
- Chaves de acesso a API do Twitter

## Restrições

Prazo de entrega: 18/03/2020 às 18:00

## Plano de Ação

* [11/03]:
    * Criação do plano de Trabalho;
    * Criação das conta de Desenvolvedor, app e chaves de acesso;
    * Criação do Repositório GIT;
    * Definição de estrutura base de pastas;

* [12/03]:
    * Definir arquitetura;
    * Criar modelo de banco de dados;
    * Criar feature getTweet e testes unitários;

* [13/03]:
    * Criar feature parseTweet e testes unitários;
    * Criar feature storeTweet e testes unitários;
    * Criar feature getTopFiveUsers e testes unitários;

* [14/03]:
    * Criar feature getTweetTotalsGroupedByDayHours e testes unitários;
    * Criar feature getHashtagsTotalsGroupedByCountry e testes unitários;
    * Criar rotas de acesso na API;
    * Expor metricas de execução da API;

* [15/03]:
    * Revisar e refatorar features;
    * Documentar features;

* [16/03]:
    * Conectar Ferramentas de logging e Monitoramento;
    * Criar testes da API com todas as funcionalidades;
    * Gerar DockerFile para deploy da aplicação em contêiner;

* [17/03]:
    * Gerar Pipeline de testes;
    * Criar interface Web;
    * Criar formulario de autenticação;
    * Criar formulario de entrada de HashTags;

* [18/03]:
    * Criar Docker-compose para deploy local da stack;
    * Documentar procedimento de deploy local da Stack;
