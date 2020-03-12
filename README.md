# Tweetcatcher
Catch hundreds of tweets from specific tags

# Estrutura do projeto
```
.
├── Docker                      (Pasta com tudo relacionado a docker)
│   └── dbTests                 (Tudo de docker utilizado para testes com base de dados)
│       └── docker-compose.yml  (Compose utilizado para testes com mongodb)
├── LICENSE                     (Licença deste aplicativo)
├── Project                     (Informações detalhadas sobre este projeto)
│   ├── architecture.md         (Definições da arquitetura da aplicação)
│   ├── assets                  (imagens e outros arquivos utilizados nos arquivos de documentação)
│   │   └── architecture.jpg    (Imagem da diagramação da arquitetura do app)
│   └── planoDeTrabalho.md      (Plano de trabalho e cronograma de desenvolvimento)
├── README.md                   (Este arquivo)
└── src                         (Codigo!)
    ├── api                     (codigo da Api e suas libs)
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── __pycache__
    │   │   └── __init__.cpython-37.pyc
    │   ├── api.py
    │   ├── env
    │   ├── libs
    │   │   └── models
    │   │       ├── __init__.py
    │   │       ├── __pycache__
    │   │       │   └── __init__.cpython-37.pyc
    │   │       └── db_model.py
    │   └── requeriments.txt
    └── web
````