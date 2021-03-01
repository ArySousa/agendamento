from django.contrib import admin
from core.models import Evento
from equipamento.models import Equipamento




class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'titulo')


class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'modelo', 'numero_serie','movimentacao','data_movimentacao')

admin.site.register(Evento, EventoAdmin)
admin.site.register(Equipamento, EquipamentoAdmin)
