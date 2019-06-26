from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from .models import Demanda


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