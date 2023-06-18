from django.db import models

# Create your models here.

class Comentario(models.Model):
    nome = models.CharField(max_length=20)
    comentario = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=False)

class Meta:
    ordering = ['publicado']

def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.nome)


