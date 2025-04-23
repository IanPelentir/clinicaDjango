from django.shortcuts import render
from django.db.models import Count
from .models import Paciente, Medico, Consulta, Convenio
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os


def relatorio_pacientes_por_cidade(request):
    dados = (
        Paciente.objects
        .values('cidade')
        .annotate(total=Count('id'))
        .order_by('-total')
    )
    return render(request, 'core/relatorio_pacientes_por_cidade.html', {'dados': dados})

def relatorio_medicos_por_especialidade(request):
    dados = (
        Medico.objects
        .values('especialidade')
        .annotate(total=Count('crm'))
        .order_by('-total')
    )
    return render(request, 'core/relatorio_medicos_por_especialidade.html', {'dados': dados})

def relatorio_consultas_por_convenio(request):
    data_inicio = request.GET.get('inicio')
    data_fim = request.GET.get('fim')
    dados = []

    if data_inicio and data_fim:
        consultas = Consulta.objects.filter(data__range=[data_inicio, data_fim])
        dados = (
            consultas
            .values('convenio__nome')
            .annotate(total=Count('id'))  # Corrigido: 'tatal' -> 'total'
            .order_by('-total')
        )

    contexto = {
        'dados': dados,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }
    return render(request, 'core/relatorio_consultas_por_convenio.html', contexto)

def grafico_convenios_pizza(request):
    dados = (
        Consulta.objects
        .values('convenio__nome')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    labels = [item['convenio__nome'] for item in dados]
    valores = [item['total'] for item in dados]

    return render(request, 'core/grafico_convenios_pizza.html', {
        'labels': labels,
        'valores': valores
    })

def grafico_consultas_por_medico(request):
    consultas = (
        Consulta.objects
        .values('medico__nome')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    total_geral = sum(item['total'] for item in consultas)

    nomes = [item['medico__nome'] for item in consultas]
    totais = [item['total'] for item in consultas]
    percentuais = [round((item['total'] / total_geral) * 100, 1) for item in consultas]

    contexto = {
        'nomes': nomes,
        'totais': totais,
        'percentuais': percentuais,
    }

    return render(request, 'core/grafico_consultas_por_medico.html', contexto)

def grafico_linha_consultas_por_dia(request):
    data_inicio = request.GET.get('inicio')
    data_fim = request.GET.get('fim')

    consultas = Consulta.objects.all()

    if data_inicio and data_fim:
        consultas = consultas.filter(data__range=[data_inicio, data_fim])

    # Agrupa as consultas por data
    dados = (
        consultas
        .values('data')
        .annotate(total=Count('id'))
        .order_by('data')
    )

    # Formata as datas para o formato desejado (dd/mm/yyyy)
    labels = [item['data'].strftime('%d/%m/%Y') for item in dados]
    valores = [item['total'] for item in dados]

    contexto = {
        'labels': labels,
        'valores': valores,
    }

    return render(request, 'core/grafico_linha_consultas_por_dia.html', contexto)

def pagina_inicial(request):
    # Gráfico 1: Consultas por Médico
    consultas_por_medico = (
        Consulta.objects
        .values('medico__nome')
        .annotate(total=Count('id'))
        .order_by('-total')
    )
    dados_consultas_por_medico_labels = [item['medico__nome'] for item in consultas_por_medico]
    dados_consultas_por_medico_values = [item['total'] for item in consultas_por_medico]

    # Gráfico 2: Consultas por Convênio
    convenios_por_pizza = (
        Consulta.objects
        .values('convenio__nome')
        .annotate(total=Count('id'))
        .order_by('-total')
    )
    dados_convenios_pizza_labels = [item['convenio__nome'] for item in convenios_por_pizza]
    dados_convenios_pizza_values = [item['total'] for item in convenios_por_pizza]

    # Gráfico 3: Consultas por Dia
    consultas_por_dia = (
        Consulta.objects
        .values('data')
        .annotate(total=Count('id'))
        .order_by('data')
    )
    labels = [item['data'].strftime('%d/%m/%Y') for item in consultas_por_dia]
    valores = [item['total'] for item in consultas_por_dia]

    contexto = {
        'dados_consultas_por_medico_labels': dados_consultas_por_medico_labels,
        'dados_consultas_por_medico_values': dados_consultas_por_medico_values,
        'dados_convenios_pizza_labels': dados_convenios_pizza_labels,
        'dados_convenios_pizza_values': dados_convenios_pizza_values,
        'labels': labels,
        'valores': valores,
    }
    return render(request, 'core/dashboard.html', contexto)

def dashboard_pdf(request):
    template_path = 'core/dashboard_pdf.html'  # você criará esse template
    context = {}  # se quiser passar dados, adicione aqui

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dashboard.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Erro ao gerar PDF', status=500)
    return response