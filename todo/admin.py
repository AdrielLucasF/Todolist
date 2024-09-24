from django.contrib import admin
from .models import Tarefa, Tag, Comentario

admin.site.register(Tarefa)
admin.site.register(Tag)
admin.site.register(Comentario)