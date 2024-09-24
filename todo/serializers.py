from rest_framework import serializers
from .models import Tarefa, Tag, Comentario

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'