from django.shortcuts import render
from rest_framework import viewsets

from .models import Atleta, Competicao, Fase, Olimpiada, Resultado
from olimpiada.serializers import AtletaSerializer, CompeticaoSerializer, FaseSerializer, OlimpiadaSerializer, ResultadoSerializer


class AtletaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer

class CompeticaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer

class FaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fase.objects.all()
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
