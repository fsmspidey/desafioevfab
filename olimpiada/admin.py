from django.contrib import admin

from .models import Atleta, Competicao, Fase, Olimpiada, Resultado


class CompeticaoAdmin(admin.ModelAdmin):
	list_filter=('modalidade','criterio_pontuacao')
	list_display=('nome','modalidade','criterio_pontuacao')


class ResultadoAdmin(admin.ModelAdmin):
	list_filter=('olimpiada','competicao','fase')
	list_display=('atleta','valor','competicao','fase')

admin.site.site_header = 'Desafio EV / Fabricio'

admin.site.register(Atleta)
admin.site.register(Competicao, CompeticaoAdmin)
admin.site.register(Fase)
admin.site.register(Olimpiada)
admin.site.register(Resultado, ResultadoAdmin)