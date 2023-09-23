from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NoteSerializer
from api.models import Note


# Create your views here.

class HomeView(APIView):
    def get(self, request):
        note = Note.objects.all()
        srz_data = NoteSerializer(instance=note, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)

class CreateNoteView(APIView):
    def post(self, request):
        srz_data = NoteSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateNoteView(APIView):

    def put(self, request, pk):
        note = Note.objects.get(pk=pk)
        srz_data = NoteSerializer(instance=note, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteNoteView(APIView):
    def delete(self, request, pk):
        note = Note.objects.get(pk=pk)
        note.delete()
        return Response({'message : Note deleted'}, status=status.HTTP_200_OK)
