from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'comentario']

    def save(self, commit=True):
        comentario = super().save(commit=False)
        comentario.status = 'pendente'  # Define o status como pendente
        if commit:
            comentario.save()
        return comentario

