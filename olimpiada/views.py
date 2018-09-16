from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions

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

#@api_view(['GET'])
def ranking_v1(request, olimpiada, competicao, modalidade, fase):
    queryset = Resultado.objects.filter(
        olimpiada=olimpiada,
        competicao=competicao,
        competicao__modalidade=modalidade,
        fase = fase
    ).all()
    serializer = RankingSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
