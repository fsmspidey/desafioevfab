from django.contrib import admin

from .models import Atleta, Competicao, Fase, Olimpiada, Resultado

class ResultadoAdmin(admin.ModelAdmin):
	list_filter=('olimpiada','competicao','fase')
	list_display=('atleta','valor','competicao','fase')

admin.site.register(Atleta)
admin.site.register(Competicao)
admin.site.register(Fase)
admin.site.register(Olimpiada)
admin.site.register(Resultado, ResultadoAdmin)