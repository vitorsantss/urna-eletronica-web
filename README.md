# Urna Eletrônica - Projeto Django

## 1. Recursos necessários

Para desenvolver esse sistema foram usados este recursos:

- Linguagem: Python
- Framework: Django
- Database: SQLite

## 2. Procedimento de Instalação da Aplicação

2. Crie um ambiente virtual no seu terminal:
```
python -m venv .venv
```

2.3 Ative seu ambiente virtual:
```
.venv/Scripts/activate
```

2.4 Instale as bibliotecas utilizadas no projeto:
```
python -m pip install -r requirements.txt
```

2.5 Execute as migrações dos models:
```
python manage.py migrate
```

2.7 Pronto, agora é só executar o servidor:
```
python manage.py runserver
```

## 3. Implementação 

   ### 3.1 
   No Diretório /setup temos um arquivo urls.py nele temos todas as rotas para poder navegar pelas páginas do sistema.

   ### 3.2 
   No Diretório /static/urna temos um arquivo script.js nele é defino todas as funções para poder usar a urna como o botão corrigir, voto em branco, e atualizar DOM para conforme tudo que o usuário fizer.

   ### 3.3 Menu
   Esta é a tela de menu do sistema com quatro botões: ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20140859.png)
   Os botões "Votação" e "Resultado" estão desativados pois ainda não foi cadastrado nenhum candidato.

   ### 3.4 Candidatos
   Na tela Candidato: ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20140917.png)
   Aqui vemos todos os candidatos cadastrados no banco e podemos clicar para cadastrar.

   #### 3.4.1 Cadastrar Candidatos
   ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20141050.png)
   Aqui deve-se colocar o número do candidato, nome e partido e salvar, logo após o candidato será resgistrado no banco.![Menu](/imagens/Captura%20de%20tela%202023-12-30%20141119.png)

   ### 3.5 Cadastrar Eleitor

   Na Tela do Eleitor:
   ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20143917.png)
   Aqui vemos todos os eleitores cadastrados no banco e podemos clicar para cadastrar.

   #### 3.5.1 Cadastrar Eleitor
   ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20183335.png)
   Aqui coloca-se o titulo de eleitor eo nome do eleitor.Logo após o eleitor será resgistrado no banco.![Menu](/imagens/Captura%20de%20tela%202023-12-30%20144103.png)

   ### 3.6 Votação
   Ao clicar no botão "Votação" vemos essa tela:

   ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20144141.png)

   Aqui será feito a requisição pelo titulo de eleitor para saber se está cadastrado no banco e se ele ainda não votou. Caso ele tenha votado e tente novamente vamos para essa tela:
   
   ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20144446.png)

   Caso ele ainda não tenha votado vamos para urna de votação:

   ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20184411.png)

   Aqui o eleitor tem que colocar o seu voto, se ele colocar um número de um candidato registrado no banco, o nome e partido serão exibidos, caso o número não esteja no banco o voto resgitrado será nulo. O eleitor também pode registrar o voto como branco. 
   
   Após confirmar o voto vemos o comprovante da votação:

   ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20184425.png)

   ### 3.7 Resultado 
   Na tela de "resultado" vemos um relatório da seção de votação:

   ![Menu](/imagens/Captura%20de%20tela%202023-12-30%20153710.png)
   

   
