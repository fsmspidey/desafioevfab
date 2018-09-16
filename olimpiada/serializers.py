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

class RankingSerializer(serializers.Serializer):
    class RankingAtletaSerializer(serializers.Serializer):     
        sobrenome = serializers.CharField()  
        nome = serializers.CharField()  
        apelido = serializers.CharField()  

    class RankingCompeticaoSerializer(serializers.Serializer):
        nome = serializers.CharField()
        modalidade = serializers.CharField()
        unidade_pontuacao = serializers.CharField()

    class RankingOlimpiadaSerializer(serializers.Serializer):
        nome = serializers.CharField()
    
    class RankingFaseSerializer(serializers.Serializer):
        nome = serializers.CharField()

    def get_atleta(self, obj):
        return self.RankingAtletaSerializer(Atleta.objects.get(pk=obj['atleta'])).data        

    atleta = serializers.SerializerMethodField()
    valor_final = serializers.CharField()


       