from django.contrib import admin
from .models import (
    CoreAuthUser,
    CoreAuthGroup,
    CoreAuthPermission,
    CoreAuthUserGroups,
    CoreAuthUserUserPermissions,
    CoreAmbulatorio,
    CoreAtende,
    CoreConsulta,
    CoreConvenio,
    CoreMedico,
    CorePaciente,
    CorePossui,
    DjangoAdminLog,
    DjangoContentType,
    DjangoMigrations,
)



@admin.register(CoreAuthUser)
class CoreAuthUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)


@admin.register(CoreAuthGroup)
class CoreAuthGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(CoreAuthPermission)
class CoreAuthPermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'codename')
    search_fields = ('name', 'content_type__app_label')
    ordering = ('name',)


@admin.register(CoreAuthUserGroups)
class CoreAuthUserGroupsAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')
    search_fields = ('user__username', 'group__name')
    ordering = ('user',)


@admin.register(CoreAuthUserUserPermissions)
class CoreAuthUserUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission')
    search_fields = ('user__username', 'permission__name')
    ordering = ('user',)


@admin.register(CoreAmbulatorio)
class CoreAmbulatorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numleitos', 'andar')
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(CoreMedico)
class CoreMedicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'nome', 'especialidade', 'idade', 'salario')
    search_fields = ('nome', 'especialidade')
    ordering = ('nome',)


@admin.register(CorePaciente)
class CorePacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'idade')
    search_fields = ('nome', 'cidade')
    ordering = ('nome',)


@admin.register(CoreConvenio)
class CoreConvenioAdmin(admin.ModelAdmin):
    list_display = ('codconv', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(CoreConsulta)
class CoreConsultaAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'porcent')
    list_filter = ('data',)
    ordering = ('-data',)


@admin.register(CoreAtende)
class CoreAtendeAdmin(admin.ModelAdmin):
    list_display = ('medico', 'convenio')
    search_fields = ('medico__nome', 'convenio__nome')
    ordering = ('medico',)


@admin.register(CorePossui)
class CorePossuiAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'convenio', 'tipo', 'vencimento')
    search_fields = ('paciente__nome', 'convenio__nome')
    ordering = ('paciente',)


@admin.register(DjangoAdminLog)
class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'object_id', 'action_flag')
    search_fields = ('user__username',)
    ordering = ('-action_time',)


@admin.register(DjangoContentType)
class DjangoContentTypeAdmin(admin.ModelAdmin):
    list_display = ('app_label', 'model')
    search_fields = ('app_label', 'model')
    ordering = ('app_label',)


@admin.register(DjangoMigrations)
class DjangoMigrationsAdmin(admin.ModelAdmin):
    list_display = ('app', 'name', 'applied')
    search_fields = ('app', 'name')
    ordering = ('-applied',)



