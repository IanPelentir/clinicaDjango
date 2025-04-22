# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.contrib.auth.models import User, Group, Permission

class CoreAuthGroup(Group):
    class Meta:
        db_table = 'core_auth_group'

    def __str__(self):
        return self.name

class CoreAuthUser(User):
    class Meta:
        db_table = 'core_auth_user'

    def __str__(self):
        return self.username

class CoreAuthPermission(Permission):
    class Meta:
        db_table = 'core_auth_permission'

    def __str__(self):
        return self.name

class CoreAuthUserGroups(models.Model):
    user = models.ForeignKey(CoreAuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(CoreAuthGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_auth_user_groups'

    def __str__(self):
        return f'{self.user.username} - {self.group.name}'

class CoreAuthGroupPermissions(models.Model):
    group = models.ForeignKey(CoreAuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey(CoreAuthPermission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_auth_group_permissions'

    def __str__(self):
        return f'{self.group.name} - {self.permission.name}'

class CoreAuthUserUserPermissions(models.Model):
    user = models.ForeignKey(CoreAuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(CoreAuthPermission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_auth_user_user_permissions'

    def __str__(self):
        return f'{self.user.username} - {self.permission.name}'

class CoreAmbulatorio(models.Model):
    nome = models.CharField(max_length=100)
    numleitos = models.IntegerField()
    andar = models.IntegerField()

    class Meta:
        db_table = 'core_ambulatorio'

    def __str__(self):
        return f'{self.nome} - {self.numleitos} leitos'

class CoreMedico(models.Model):
    crm = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    ambulatorio = models.ForeignKey(CoreAmbulatorio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_medico'

    def __str__(self):
        return f'{self.nome} ({self.crm}) - {self.especialidade}'

class CorePaciente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    idade = models.IntegerField()
    ambulatorio = models.ForeignKey(CoreAmbulatorio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_paciente'

    def __str__(self):
        return f'{self.nome} - {self.cidade}'

class CoreConvenio(models.Model):
    codconv = models.IntegerField()
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'core_convenio'

    def __str__(self):
        return f'{self.nome} ({self.codconv})'

class CoreConsulta(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    medico = models.ForeignKey(CoreMedico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(CorePaciente, on_delete=models.CASCADE)
    convenio = models.ForeignKey(CoreConvenio, on_delete=models.CASCADE)
    porcent = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'core_consulta'

    def __str__(self):
        return f'Consulta de {self.paciente.nome} com Dr(a). {self.medico.nome} em {self.data}'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user = models.ForeignKey(CoreAuthUser, on_delete=models.CASCADE)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    object_id = models.TextField()
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()

    class Meta:
        db_table = 'core_django_admin_log'

    def __str__(self):
        return f'{self.action_time} - {self.user.username}'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'core_django_content_type'

    def __str__(self):
        return f'{self.app_label} - {self.model}'

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'core_django_migrations'

    def __str__(self):
        return f'{self.app} - {self.name} - {self.applied}'




class CoreAtende(models.Model):
    medico = models.ForeignKey('CoreMedico', on_delete=models.CASCADE)
    convenio = models.ForeignKey('CoreConvenio', on_delete=models.CASCADE)

    class Meta:
        db_table = 'core_atende'

    def __str__(self):
        return f'{self.medico} atende {self.convenio}'


class CorePossui(models.Model):
    paciente = models.ForeignKey('CorePaciente', on_delete=models.CASCADE)
    convenio = models.ForeignKey('CoreConvenio', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1)
    vencimento = models.DateField()

    class Meta:
        db_table = 'core_possui'

    def __str__(self):
        return f'{self.paciente} possui o convênio {self.convenio}'
