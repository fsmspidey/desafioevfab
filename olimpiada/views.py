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
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Atleta.objects.all().order_by("nome")
    serializer_class = AtletaSerializer

class CompeticaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Competicao.objects.all().order_by("nome")
    serializer_class = CompeticaoSerializer

class FaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fase.objects.all().order_by("nome")
    serializer_class = FaseSerializer


class OlimpiadaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Olimpiada.objects.all()
    serializer_class = OlimpiadaSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

@api_view(['GET'])
def ranking_v1(request, olimpiada, competicao, modalidade, fase):

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
        queryset = queryset.annotate(valor_final=Min('valor'))
    elif competicao.criterio_pontuacao == 1:        
        queryset = queryset.annotate(valor_final=Max('valor'))

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


    saida = '{ "olimpiada":' + json.dumps(olimpiada.data) + ','
    saida += '"competicao": ' + json.dumps(competicao.data) + ','
    saida += '"fase":' + json.dumps(fase.data) + ','
    saida += '"resultado_status":' + json.dumps(status_resultado) + ','
    saida += '"ranking": ' + json.dumps(ranking.data) + '}'

    return HttpResponse(saida, content_type="application/json")
