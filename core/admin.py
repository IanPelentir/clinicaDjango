from django.contrib import admin
from .models import (
    Ambulatorio,
    Paciente,
    Medico,
    Convenio,
    Consulta,
    Atende,
    Possui,
)

@admin.register(Ambulatorio)
class AmbulatorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'numleitos', 'andar')
    search_fields = ('nome',)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cidade', 'idade', 'ambulatorio')
    search_fields = ('nome', 'cidade')
    list_filter = ('cidade',)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'nome', 'especialidade', 'idade', 'salario', 'ambulatorio')
    search_fields = ('nome', 'especialidade')
    list_filter = ('especialidade',)

@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('codconv', 'nome')
    search_fields = ('nome',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'horario', 'medico', 'paciente', 'convenio', 'porcent')
    list_filter = ('data', 'convenio')
    search_fields = ('medico__nome', 'paciente__nome')

@admin.register(Atende)
class AtendeAdmin(admin.ModelAdmin):
    list_display = ('medico', 'convenio')
    search_fields = ('medico__nome', 'convenio__nome')

@admin.register(Possui)
class PossuiAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'convenio', 'tipo', 'vencimento')
    list_filter = ('tipo', 'vencimento')
    search_fields = ('paciente__nome', 'convenio__nome')
