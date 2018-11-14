# flex_painel_precos
Aplicação WEB que permite o gerenciamento de promoções e listagem de preços para exibição em smartTV's ou outros dispositivo que possua navegador.

## Pré-requisitos para instalação em produção
- Python 3.6
- Servidor HTTP (Nginx + Gunicorn, Apache 2.4 + libapache2-mod-wsgi-py3, etc)
- PostgreSQL 9.6+ (Com estrutura compatível com o Flex)

## Preparando o banco de dados
Execute o arquivo [**install.sql**](https://github.com/camilossantos2809/flex-painel-preco/blob/master/install.sql) logado no banco de dados do Flex como superusuário, lembrando de substituir os dados de senha.

## Obtendo a versão mais recente do projeto
Crie um diretório para a aplicação num local apropriado. Acesse o diretório e extraia o conteúdo do [arquivo zip](https://github.com/camilossantos2809/flex-painel-preco/archive/master.zip) ou, se você possuir o `git` instalado, faça um clone do projeto.
`git clone https://github.com/camilossantos2809/flex-painel-preco.git .`

## Instalando as dependências
Dentro da pasta do projeto crie um ambiente virtual do python utilizando o **virtualenv**.
```
pip install virtualenv
virtualenv -p python3 venv
```
Ative o ambiente virtual
`source venv/bin/activate`
>No Windows o comando será: `venv\Scripts\activate.bat`

Com o ambiente virtual ativo faça o download e instalação das dependências
`pip install -r requirements.txt`

Para os próximos passos o ambiente virtual precisa estar sempre ativo.

## Configurando o banco de dados
Para setar as configurações de conexão com o banco de dados execute o arquivo **config.py**.
`python config.py`

Crie a estrutura necessária do banco de dados.
`python manage.py migrate`
>Em caso de erro de conexão com o banco de dados revise os dados informados ao executar o arquivo **config.py**. Verifique também a senha criada para o usuário *painel*, criado na execução do arquivo [install.sql](https://github.com/camilossantos2809/flex-painel-preco/blob/master/install.sql).

## Testando a aplicação
Para testar as configurações execute o servidor de desenvolvimento do *Django*.
`python manage.py runserver 8000`

Abra o navegador e acesse a página [http://localhost:8000](http://localhost:8000).

>Esse servidor só funcionará na máquina local e não deve ser usado em ambiente de produção.

## Colabore!
Fique a vontade para colaborar na construção do código fazendo um *pull request* ou informando alguma *issue*.
Sua opinião também é sempre bem vinda.