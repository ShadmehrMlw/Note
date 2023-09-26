from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=1000)
    body = serializers.CharField(max_length=1000)
    created = serializers.DateTimeField()
    is_active = serializers.BooleanField(default=True)
    username = serializers.StringRelatedField()


    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    class Meta:
        model = Note
        fields = '__all__'