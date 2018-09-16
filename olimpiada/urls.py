from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from olimpiada import views

router = routers.DefaultRouter()
router.register(r'atletas', views.AtletaViewSet)
router.register(r'competicoes', views.CompeticaoViewSet)
router.register(r'fases', views.FaseViewSet)
router.register(r'olimpiadas', views.OlimpiadaViewSet)
router.register(r'resultados', views.ResultadoViewSet)

urlpatterns = [
	url(r'^(?P<olimpiada>\d+)/competicao/(?P<competicao>\d+)/modalidade/(?P<modalidade>[MF])/fase/(?P<fase>\d+)/ranking/', views.ranking_v1),
	url(r'^', include(router.urls)),
]