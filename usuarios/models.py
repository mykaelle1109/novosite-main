from django.db import models

# Create your models here.
class Nota(models.Model):
    nome_aluno = models.CharField(max_length= 200) #CharField se refere ao tipo de atributo que nesse caso é Char
    disciplina = models.CharField(max_length= 200)
    nota_atividades = models.IntegerField(default=0)
    nota_trabalho = models.IntegerField(default=0)
    nota_prova = models.IntegerField(default=0)
    media = models.IntegerField(blank = True, default=0)#blank true significa que não será preenchido diretamente pelo usuário