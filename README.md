# Desafio EV
Meu objetivo foi elaborar um sistema coeso e desacoplado, utilizando as boas práticas do DDD.\
As regras de negócio do enunciado proposto foram executadas de maneira a permitir outras Competições em situações similares sem a necessidade de reescrita do código e até mesmo outras Olimpíadas

# Testado em:
- Windows 10
- Python 3.7

# INSTALAÇÃO
Após baixar o projeto no diretorio que desejar\

$ cd desafioevfab\
$ virtualenv env\
$ env\Scripts\activate\
$ pip install -r requirements.txt\
$ python manage.py makemigrations\
$ python manage.py migrate\
$ python manage.py createsuperuser

# Testes
Para testar a aplicação, dentro da raiz do projeto, digite:

$ python manage.py test

# ADMIN
Para acessar o admin, basta rodar o comando abaixo e entrar na url padrao do Django (http://localhost:8000/admin), fornecendo seu login e senha:\
$ python manage.py runserver

# Entrada de dados
## Na tela inicial, siga os passos abaixo:
1. Primeiramente vamos criar uma "Olimpíada": clique no link "Olimpiadas" (adicionar)\
1.1. Preencha um nome e uma vigência para este evento

2. Crie uma "Competição", clicando no link "Competições" (adicionar)\
2.1. Preencha o nome da competição\
2.2. Preencha a Vigência (Só é permitida a inclusao de dados com a competição em andamento)\
2.3. Preencha a modalidade (Masculino ou Feminino)\
2.4. Preencha a unidade de pontuação (Metros, kg, segundos, etc)\
2.5. Preencha o critério de pontuação (pontua-se mais com o menor ou o maior valor?)\
2.6. Preencha a quantidade de "tentativas". Quantas tentativas podem ser inputadas no sistema por Atleta nesta competição?\

3. Crie uma "Fase", clicando no link "Fases" (adicionar)\
3.1. Preencha o nome da Fase, exemplos: "Classificacao", "Final", "Semifinal" etc\

4. Preencha os resultados dos Atletas em cada Competição, clicando no link "Resultados" (adicionar)\
4.1. Selecione de qual Olimpíada estamos falando\
4.2. Selecione qual a Competição em questão\
4.3. Selecione o Atleta desejado (Cuidado com o sexo do Atleta e a modalidade da Competição)\
4.4. Selecione a fase de que estamos falando\
4.5. Insira o valor (separador é ",")

## Inserindo valores pela api
### Atletas
$ http --auth user:pass POST http://127.0.0.1:8000/api/v1/olimpiada/atletas/ nome=Joao sobrenome=MAGUILA sexo=M nascimento_data=1978-12-28\
Ou acessar o endpoint:

http://localhost:8000/api/v1/olimpiada/atletas/

### Olimpiadas
$ http --auth user:pass POST http://127.0.0.1:8000/api/v1/olimpiada/olimpiadas/ nome="Olimpiadas do Faustao" inicio_data="1978-12-28 12:00" final_data="2018-12-30 00:00"

Ou acessar o endpoint:

http://localhost:8000/api/v1/olimpiada/olimpiadas/

### Fases
$ http --auth user:pass POST http://127.0.0.1:8000/api/v1/olimpiada/fases/ nome="Final"

Ou acessar o endpoint: 
http://localhost:8000/api/v1/olimpiada/fases/

### Competicao
$ http --auth user:pass POST http://127.0.0.1:8000/api/v1/olimpiada/competicoes/ nome="100m Rasos" inicio_data="1978-12-28 12:00" final_data="2018-12-30 00:00" modalidade="M" unidade_pontuacao="s" criterio_pontuacao=0 tentativas=1

Ou acessar o endpoint:\ 
http://localhost:8000/api/v1/olimpiada/competicoes/

### Resultados
$ http --auth user:pass POST http://127.0.0.1:8000/api/v1/olimpiada/resultados/ olimpiada=1 competicao=1 atleta=1 fase=1 valor="3.111"

Ou acessar o endpoint:\
http://localhost:8000/api/v1/olimpiada/resultados/

### Ranking
Preencha os valores correspondentes na url: (id da olimpiada, id da competicao, "M" ou "F" em modalidade e id da fase)

http://localhost:8000/api/v1/olimpiada/1/competicao/1/modalidade/M/fase/1/ranking/

#Obrigado pela oportunidade!