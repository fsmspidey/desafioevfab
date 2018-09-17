from django.test import TestCase, RequestFactory
from django.utils import timezone
from datetime import datetime, timedelta

from .models import Atleta, Competicao, Fase, Olimpiada, Resultado
from .views import ranking_v1

class OlimpiadaModelTests(TestCase):

	def setUp(self):
		print ("\n* Configurado entrada de dados")
		self.factory = RequestFactory()
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

		Fase.objects.create(nome="Classificação")
		Fase.objects.create(nome="Semi-final")

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
		atleta1 = Atleta.objects.get(nome="Joao")
		atleta2 = Atleta.objects.get(nome="Maria")

		print("\t-- Atleta 1")
		self.assertEqual(atleta1.nome, 'Joao')

		print("\t-- Atleta 2")
		self.assertEqual(atleta2.nome, 'Maria')

	def testa_leitura_competicao(self):
		print ("* Testando o retorno das Competicoes")
		competicao1 = Competicao.objects.get(nome="100m Rasos")
		competicao2 = Competicao.objects.get(nome="Lancamento de Dardo")

		print("\t-- Competicao 1")
		self.assertEqual(competicao1.nome, '100m Rasos')

		print("\t-- Competicao 2")
		self.assertEqual(competicao2.nome, 'Lancamento de Dardo')		

	def testa_leitura_fase(self):
		print ("* Testando o retorno das Fases")
		fase1 = Fase.objects.get(nome="Semi-final")
		fase2 = Fase.objects.get(nome="Classificação")

		print("\t-- Fase 1")
		self.assertEqual(fase1.nome, 'Semi-final')

		print("\t-- Fase 2")
		self.assertEqual(fase2.nome, 'Classificação')

	def testa_insercao_resultado(self):
		print ("* Testando a insercao dos resultados")
		olimpiada = Olimpiada.objects.get(nome="Olimpiada 1")
		atleta = Atleta.objects.get(nome="Joao")
		competicao = Competicao.objects.get(nome="100m Rasos")
		fase = Fase.objects.get(nome="Classificação")

		Resultado.objects.create(
			olimpiada=olimpiada,
			competicao=competicao,
			atleta=atleta,
			fase=fase,
			valor = 2.333
		)

		resultado1 = Resultado.objects.get(pk=1)
		print("\t-- Resultado 1")
		self.assertEqual(resultado1.pk, 1)

