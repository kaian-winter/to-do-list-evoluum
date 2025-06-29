# Projeto - API To-Do list
Projeto de avaliação técnica da Evoluum de uma lista de gerenciamento de tarefas (To-Do List).
Permite cadastro e login de usuários, e também cadastro, busca, edição e deleção de ToDos.

## Como foi feito
Este projeto é uma API desenvolvida em Python com FastAPI, SQLAlchemy como ORM, e conta com duas tabelas em um banco de dados PostgreSQL, Todos e Users.
Suas rotas são divididas em ToDos, auth e Users.    

ToDos: Permite a busca de todos os ToDos do usuário, de apenas um específico, criação, edição, deleção e finalização de um ToDo.  
auth: Permite que o usuário se registre e que faça login para obtenção de um token (foi feito de forma estática como solicitado).  
Users: Permite que o usuário receba suas informações (uso em uma tela de perfil), e troque sua senha.  

## Conhecimentos utilizados
Foram utilizadas práticas de código limpo separando as camadas em Presentation, Domain e Data, e definindo o que deve ser mantido em cada uma.  
Na camada de presentation foram usados os conceitos de Rotas, Rate Limiting e os Status apropriados de cada retorno.  
Na camada de dominio, foram abstraídos ao máximo os acessos aos dados de banco, e sempre que possível oferecidas Hints de tipo.  
Na camada de dados foi utilizada a ORM SQLAlchemy com Alembic para realização das consultas e manter as migrações do banco espelhadas.  

## Utilização
1. Clone o repositório da aplicação:  
   git@github.com:kaian-winter/to-do-list-evoluum.git  

2. Crie e ative um ambiente virtual (recomendado):  
   cd to-do-list-evoluum  
   python3 -m venv venv  
   source venv/bin/activate  

3. Instale as dependências do projeto:  
   pip install -r requirements.txt (ou requirements-dev.txt em ambiente de desenvolvimento)    

4. Configure as variáveis de ambiente, criando um arquivo .env na raiz do projeto com as variáveis necessárias, como as credenciais do banco de dados:  
   DATABASE_URL="postgresql://postgres:admin@127.0.0.1:5432/to_do_list_evoluum"  
   STATIC_TOKEN="PD03JXKeO_XBNH_KJj4ZgqFII7UVSFNsuWd-piEkO1e6PrMMySQ_FlmUS8uonGkDB3j_VlA4AriDsBk40f5TEAQypDCJMmyufv3bWD1Q1EVzrjPuvpYnJt0m9HbnT02GLqf9lReBz7BFjoIAumo_n94BsGcGAvqaH3r-H592h7zaRKA5GuW6zPpdLNx6H4z5iAeiHFu6DkDsLh1QJjYOX7uRKsYF2I4Kv6O3-_VtC972FHio-EgNAZPNKNhn4wj3yoSvq_iahWJpA02rN8-KnMnIH63Z4OQtPgVSiM8ZnAVGEx3XgI8xR0GnRLM-pEUzJJ389iteK9jB-mNIGsF0LzyCPBQDV9"    

5. Inicie o servidor de desenvolvimento:  
   uvicorn src.main:app --reload
