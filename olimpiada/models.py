from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


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
		return self.nome + ' (' + self.modalidade + ')'
	
	class Meta:
		verbose_name_plural = "Competições"
		unique_together=("nome", "modalidade")

	def clean(self):
		if self.final_data<self.inicio_data:
			raise ValidationError('Data final menor que a data inicial')					

	
class Fase(models.Model):
	nome = models.CharField(max_length=90, unique=True)
	def __str__(self):
		return self.nome

class Olimpiada(models.Model):
	""" Olimpiada """
	nome = models.CharField(max_length=150, unique=True)
	inicio_data = models.DateTimeField()
	final_data= models.DateTimeField()

	def __str__(self):
		return self.nome

	def clean(self):
		if self.final_data<self.inicio_data:
			raise ValidationError('Data final menor que a data inicial')					

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
	valor = models.DecimalField(max_digits=8, decimal_places=3)
	
	def __str__(self):
		return "Resultado"

	def clean(self):
		"""
		Validacao importante das regras dos resultados. 
		Colabora para os dados permanecerem íntegros
		"""
		if timezone.now()<self.olimpiada.inicio_data:
			raise ValidationError('Essa Olimpíada ainda não começou')

		if timezone.now()>self.olimpiada.final_data:
			raise ValidationError('Essa Olimpíada já terminou')

		if timezone.now()<self.competicao.inicio_data:
			raise ValidationError('Essa Competição ainda não começou')

		if timezone.now()>self.competicao.final_data:
			raise ValidationError('Essa Competição já terminou')

		if self.atleta.sexo != self.competicao.modalidade:
			raise ValidationError('Atleta na modalidade errada')		

		if Resultado.objects.filter( \
			olimpiada=self.olimpiada,\
			competicao=self.competicao,\
			atleta=self.atleta,\
			fase=self.fase\
		).count() > self.competicao.tentativas:
			raise ValidationError('Este atleta já tem todas as tentativas que a competição permite')					
		

