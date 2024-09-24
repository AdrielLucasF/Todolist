from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    completo = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Tag(models.Model):
    nome = models.CharField(max_length=30)
    tarefas = models.ManyToManyField(Tarefa, related_name='tags')

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=50)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor} na tarefa {self.tarefa.titulo}'
