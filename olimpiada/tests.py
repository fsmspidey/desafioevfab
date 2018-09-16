from django.test import TestCase
from django.utils import timezone
from datetime import datetime, timedelta

from .models import Atleta, Competicao, Fase, Olimpiada, Resultado
class OlimpiadaModelTests(TestCase):

	def setUp(self):
		print ("\n* Configurado entrada de dados")
		#print("\t-- Criando Olimpiadas")
		Olimpiada.objects.create(
			nome="Olimpiada 1",
			inicio_data=timezone.now(),
			final_data=timezone.now()+ timedelta(days=1)
		)
		Olimpiada.objects.create(
			nome="Olimpiada 2",
			inicio_data=timezone.now(),
			final_data=timezone.now()
		)

		#print("\t-- Criando Atletas")
		Atleta.objects.create(
			nome="Joao",
			sobrenome="Roberto",
			apelido="",
			nascimento_data='1988-01-01',
			sexo='M'
		)
		Atleta.objects.create(
			nome="Maria",
			sobrenome="Leal",
			apelido="",
			nascimento_data='1981-12-01',
			sexo='F'
		)
		#print("\t-- Criando Competicoes")
		Competicao.objects.create(
			nome="100m Rasos",
			inicio_data=timezone.now(),
			final_data=timezone.now()+ timedelta(days=1),
			modalidade='M',
			unidade_pontuacao='s',
			criterio_pontuacao=0,
			tentativas=1
		)

		Competicao.objects.create(
			nome="Lancamento de Dardo",
			inicio_data=timezone.now(),
			final_data=timezone.now()+ timedelta(days=1),
			modalidade='M',
			unidade_pontuacao='m',
			criterio_pontuacao=0,
			tentativas=3
		)

	def testa_leitura_olimpiada(self):
		print ("* Testando o retorno das Olimpíadas")
		olimpiada1 = Olimpiada.objects.get(nome="Olimpiada 1")
		olimpiada2 = Olimpiada.objects.get(nome="Olimpiada 2")

		print("\t-- Olimpiada 1")
		self.assertEqual(olimpiada1.nome, 'Olimpiada 1')

		print("\t-- Olimpiada 2")
		self.assertEqual(olimpiada2.nome, 'Olimpiada 2')

	def testa_leitura_atleta(self):
		print ("* Testando o retorno dos Atletas")
		joao = Atleta.objects.get(nome="Joao")
		maria = Atleta.objects.get(nome="Maria")

		print("\t-- Atleta 1")
		self.assertEqual(joao.nome, 'Joao')

		print("\t-- Atleta 2")
		self.assertEqual(maria.nome, 'Maria')