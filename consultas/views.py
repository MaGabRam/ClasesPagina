from django.shortcuts import render
from .serializer import EstudiantesSerializer
from .models import Estudiantes
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer

    def list(self, request):
        serializer = EstudiantesSerializer(self.queryset, many=True)
        print(queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            estudiante = Estudiantes.objects.get(carnet=pk)
            id_estudiante = estudiante.id
            task = Task.objects.get(foreign=id_estudiante)
            serializer = TaskSerializer(task, many=True)
            serializer = EstudiantesSerializer(estudiante)
            return Response(serializer.data)
        except Estudiantes.DoesNotExist:
            return Response('Estudiante no encontrado', status=404)
        except Exception as e:
            return Response('Error', status=500)

    def create(self, request):
        serializer = EstudiantesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        estudiante = Estudiantes.objects.get(carnet=pk)
        serializer = EstudiantesSerializer(
            instance=estudiante, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        estudiante = Estudiantes.objects.get(carnet=pk)
        estudiante.delete()
        return Response('Estudiante eliminado')


# Create your views here.
