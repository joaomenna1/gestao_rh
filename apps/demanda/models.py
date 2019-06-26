from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa

class Demanda(models.Model):
    entidade = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    atendimento = models.CharField(max_length=100)
    telefone = models.CharField(max_length=9)
    assunto = models.CharField(max_length=100)
    data = models.CharField(max_length=10)
    profissao = models.CharField(max_length=100)
    encaminhamento = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    situacao = models.CharField(max_length=100)



    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('list_demanda')

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {}'.format(
            self.entidade, self.municipio,
            self.endereco, self.atendimento, self.telefone,
            self.assunto, self.data, self.profissao,
            self.encaminhamento, self.responsavel, self.situacao
        )
