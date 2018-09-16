from django.db import models

from datetime import datetime

# Create your models here.
class Atleta(models.Model):
	SEXO = (
    	('M', 'Masculino'),
    	('F', 'Feminino'),
	)
	nome = models.CharField(max_length=150)
	sobrenome = models.CharField(max_length=150)
	apelido = models.CharField(max_length=150, blank=True)
	nascimento_data = models.DateField(default=datetime.now)
	sexo = models.CharField(
		max_length=1,
		choices=SEXO,
		default=0
	)

	class Meta:
		unique_together=("nome", "sobrenome")

	def __str__(self):
		return self.nome + ' ' + self.sobrenome 

class Competicao(models.Model):
	""" Competicao """
	MODALIDADE = (
    	('M', 'Masculino'),
    	('F', 'Feminino'),
	)
	CRITERIO = (
    	(0, 'Menor Valor'),
    	(1, 'Maior Valor'),
	)
	UNIDADE = (
    	('Kg', 'Kilograma'),
    	('s', 'Segundos'),
    	('m', 'Metros')
	)

	nome = models.CharField(max_length=150)
	inicio_data = models.DateTimeField()
	final_data = models.DateTimeField()
	modalidade = models.CharField(
		max_length=2,
		choices=MODALIDADE,
		default='M'
	)
	unidade_pontuacao = models.CharField(
		max_length=2,
		choices=UNIDADE,
		default='m'

	)
	criterio_pontuacao = models.PositiveSmallIntegerField(
		choices=CRITERIO,
		default=0
	)
	tentativas = models.PositiveSmallIntegerField(default=1)

	def __str__(self):
		return self.nome
	class Meta:
		verbose_name_plural = "Competições"
	
class Fase(models.Model):
	nome = models.CharField(max_length=90)
	def __str__(self):
		return self.nome

class Olimpiada(models.Model):
	""" Olimpiada """
	nome = models.CharField(max_length=150)
	inicio_data = models.DateTimeField()
	final_data= models.DateTimeField()

	def __str__(self):
		return self.nome

class Resultado(models.Model):
	olimpiada = models.ForeignKey(
        'Olimpiada',
        on_delete=models.CASCADE,
    )
	competicao = models.ForeignKey(
		'Competicao',
		on_delete=models.CASCADE,
	)
	atleta = models.ForeignKey(
		'Atleta',
		on_delete=models.CASCADE,
	)
	fase = models.ForeignKey(
		'Fase',
		on_delete=models.CASCADE,
	)
	valor = models.IntegerField()
