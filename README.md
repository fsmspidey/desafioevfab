# desafioevfab
Desafio EV

# Requerimentos
- Windows 10
- Python 3.7

# INSTALAÇÃO

$ cd desafioevfab
$ virtualenv env
$ env\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser


## Inserindo valores pela api
### Atletas
$ http --auth user:pass POST http://127.0.0.1:8000/api/v1/olimpiada/atletas/ nome=Joao sobrenome=MAGUILA sexo=M nascimento_data=1978-12-28
Ou acessar o endpoint: 
http://localhost:8000/api/v1/olimpiada/atletas/

### Olimpiadas
$ http --auth user:pass POST http://127.0.0.1:8000/api/v1/olimpiada/olimpiadas/ nome="Olimpiadas do Faustao" inicio_data="1978-12-28 12:00" final_data="2018-12-30 00:00"
Ou acessar o endpoint: 
http://localhost:8000/api/v1/olimpiada/olimpiadas/