from django.db import models


class Ambulatorio(models.Model):
    nome = models.CharField(max_length=200)
    numleitos = models.IntegerField()
    andar = models.IntegerField()

    class Meta:
        db_table = 'ambulatorio'
        managed = False
        verbose_name = 'Ambulatório'
        verbose_name_plural = 'Ambulatórios'

    def __str__(self):
        return f'{self.nome} - {self.numleitos} leitos'


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    idade = models.IntegerField()
    ambulatorio = models.ForeignKey(
        Ambulatorio, on_delete=models.CASCADE,
        db_column='idamb', related_name='pacientes'
    )

    class Meta:
        db_table = 'paciente'
        managed = False
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.nome} - {self.cidade}'


class Medico(models.Model):
    crm = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=12, decimal_places=2)
    ambulatorio = models.ForeignKey(
        Ambulatorio, on_delete=models.CASCADE,
        db_column='idamb', related_name='medicos'
    )

    class Meta:
        db_table = 'medico'
        managed = False
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        return f'Dr(a). {self.nome} - {self.especialidade} ({self.crm})'


class Convenio(models.Model):
    codconv = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        db_table = 'convenio'
        managed = False
        verbose_name = 'Convênio'
        verbose_name_plural = 'Convênios'

    def __str__(self):
        return f'{self.nome} ({self.codconv})'


class Consulta(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='medico')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente')
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, db_column='convenio')
    porcent = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'consulta'
        managed = False
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f"Consulta de {self.paciente.nome} com {self.medico.nome} em {self.data}"


class Atende(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='medico', primary_key=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, db_column='convenio')

    class Meta:
        db_table = 'atende'
        managed = False
        unique_together = (('medico', 'convenio'),)
        verbose_name = 'Atende'
        verbose_name_plural = 'Atende'

    def __str__(self):
        return f"{self.medico.nome} atende o convênio {self.convenio.nome}"


class Possui(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente',  primary_key=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, db_column='convenio')
    tipo = models.CharField(max_length=1)
    vencimento = models.DateField()

    class Meta:
        db_table = 'possui'
        managed = False
        unique_together = (('paciente', 'convenio'),)
        verbose_name = 'Possui'
        verbose_name_plural = 'Possui'

    def __str__(self):
        return f"{self.paciente.nome} possui o convênio {self.convenio.nome} - tipo {self.tipo}"
