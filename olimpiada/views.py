from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db.models import Max, Min
from django.shortcuts import get_object_or_404
from django.utils import timezone
import json


from .models import Atleta, Competicao, Fase, Olimpiada, Resultado
from .serializers import AtletaSerializer, CompeticaoSerializer, FaseSerializer, OlimpiadaSerializer, ResultadoSerializer, RankingSerializer


class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all().order_by("nome")
    serializer_class = AtletaSerializer

class CompeticaoViewSet(viewsets.ModelViewSet):
    queryset = Competicao.objects.all().order_by("nome")
    serializer_class = CompeticaoSerializer

class FaseViewSet(viewsets.ModelViewSet):
    queryset = Fase.objects.all().order_by("nome")
    serializer_class = FaseSerializer


class OlimpiadaViewSet(viewsets.ModelViewSet):
    queryset = Olimpiada.objects.all()
    serializer_class = OlimpiadaSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

@api_view(['GET'])
def ranking_v1(request, olimpiada, competicao, modalidade, fase):
    """
    View que retorna o ranking de uma competição durante uma olimpiada.
    Os registros já vem ordenados pela posição, entao o registro "0" é a primeira posição
    """
    competicao = get_object_or_404(Competicao, pk=competicao)
    olimpiada = get_object_or_404(Olimpiada, pk=olimpiada)
    fase = get_object_or_404(Fase, pk=fase)

    queryset = Resultado.objects.filter(
        olimpiada=olimpiada,
        competicao=competicao,
        competicao__modalidade=modalidade,
        fase = fase
    ).values('atleta')
    
    if competicao.criterio_pontuacao == 0:
        queryset = queryset.annotate(valor_final=Min('valor')).order_by("valor_final")
    elif competicao.criterio_pontuacao == 1:
        queryset = queryset.annotate(valor_final=Max('valor')).order_by("-valor_final")

    status_resultado = "Resultado Parcial"
    if timezone.now()>olimpiada.final_data:
        status_resultado = "Resultado Final"           
    elif timezone.now()<olimpiada.inicio_data: 
        status_resultado = "Nao Iniciado"
    elif timezone.now()<competicao.inicio_data:
        status_resultado = "Nao iniciado"
    elif timezone.now()>competicao.final_data:
        status_resultado = "Resultado Final"

    olimpiada = RankingSerializer.RankingOlimpiadaSerializer(olimpiada)
    competicao = RankingSerializer.RankingCompeticaoSerializer(competicao)
    fase = RankingSerializer.RankingFaseSerializer(fase)    
    ranking = RankingSerializer(queryset, many=True)


    saida_json = '{ "olimpiada":' + json.dumps(olimpiada.data) + ','
    saida_json += '"competicao": ' + json.dumps(competicao.data) + ','
    saida_json += '"fase":' + json.dumps(fase.data) + ','
    saida_json += '"resultado_status":' + json.dumps(status_resultado) + ','
    saida_json += '"ranking": ' + json.dumps(ranking.data) + '}'

    return HttpResponse(saida_json, content_type="application/json")
