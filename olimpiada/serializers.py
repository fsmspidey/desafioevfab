from rest_framework import serializers

from .models import Atleta, Competicao, Fase, Olimpiada, Resultado

class AtletaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'

class OlimpiadaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Olimpiada
        fields = ('__all__')

class CompeticaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competicao
        fields = ('__all__')

class FaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fase
        fields = ('__all__')

class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resultado
        fields = ('__all__')
        