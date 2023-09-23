from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=1000)
    body = serializers.CharField(max_length=1000)
    created = serializers.DateTimeField()
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    class Meta:
        model = Note
        fields = '__all__'