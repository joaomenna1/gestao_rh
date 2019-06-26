from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from .models import Demanda
from  apps.funcionarios.models import Funcionario
import io
from django.http import HttpResponse
from reportlab.pdfgen import canvas


class DemandaList(ListView):
    model = Demanda

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Demanda.objects.filter(empresa=empresa_logada)


class DemandaCreate(CreateView):
    model = Demanda
    fields = ('entidade', 'municipio', 'endereco', 'atendimento', 'telefone', 'assunto', 'profissao',
              'encaminhamento', 'data', 'responsavel', 'situacao')


    def form_valid(self, form):
        demanda = form.save(commit=False)
        demanda.empresa = self.request.user.funcionario.empresa
        demanda.save()
        return super(DemandaCreate, self).form_valid(form)


class DemandaUpdate(UpdateView):
    model = Demanda
    fields = ('entidade', 'municipio', 'endereco', 'atendimento', 'telefone', 'assunto', 'profissao',
              'encaminhamento', 'data', 'responsavel', 'situacao')


class DemandaDelete(DeleteView):
    model = Demanda
    success_url = reverse_lazy('list_demanda')


def pdf_reportlab(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(150, 810, 'CONTROLE DE DEMANDA DE PROJETOS')

    demandas = Demanda.objects.all()

    str_ = 'ID: %s | Entidade: %s | Assunto: %s| Situação: %s '

    p.drawString(0, 800, '_' * 150)

    y = 750
    for demanda in demandas:
        p.drawString(10, y, str_ % (
            demanda.id, demanda.entidade, demanda.assunto, demanda.situacao))
        y -= 30

    p.setFont("Helvetica-Oblique", 16)
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response