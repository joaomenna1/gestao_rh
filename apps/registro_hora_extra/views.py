import csv
import json
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
from django.http import HttpResponse
import xlwt


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horaExtra')

class HoraExtracreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtracreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        response = json.dumps(
            {'mensagem': 'Requisicao executada'}
        )
        return HttpResponse(response, content_type='aplication/json')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas'])

        for registro in registro_he:
            writer.writerow(
                [registro.id, registro.motivo, registro.funcionario,
                 registro.funcionario.total_horas_extra, registro.horas
                 ])

        return response

class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="meu_relatorio_excel.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = RegistroHoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.funcionario.total_horas_extra, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num += 1

        wb.save(response)
        return response
