from django.contrib import admin
from .models import (
    Ambulatorio, Paciente, Medico, Convenio,
    Consulta, Atende, Possui
)


@admin.register(Ambulatorio)
class AmbulatorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numleitos', 'andar')
    search_fields = ('nome',)


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'idade', 'ambulatorio')
    search_fields = ('nome', 'cidade')
    list_filter = ('cidade', 'ambulatorio')


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'nome', 'especialidade', 'ambulatorio', 'idade')
    search_fields = ('nome', 'especialidade')
    list_filter = ('especialidade', 'ambulatorio')


@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('codconv', 'nome')
    search_fields = ('nome',)


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'medico', 'paciente', 'convenio', 'porcent')
    search_fields = ('paciente__nome', 'medico__nome')
    list_filter = ('data', 'medico', 'convenio')


@admin.register(Atende)
class AtendeAdmin(admin.ModelAdmin):
    list_display = ('medico', 'convenio')
    search_fields = ('medico__nome', 'convenio__nome')
    list_filter = ('medico', 'convenio')


@admin.register(Possui)
class PossuiAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'convenio', 'tipo', 'vencimento')
    search_fields = ('paciente__nome', 'convenio__nome')
    list_filter = ('tipo', 'vencimento')
