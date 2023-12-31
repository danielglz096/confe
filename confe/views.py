from .models import Instituciones
from .serializers import InstitucionesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def institucion_list(request, format=None):
        
        if request.method == 'GET':
            instituciones = Instituciones.objects.all()
            serializer = InstitucionesSerializer(instituciones, many=True)
            return Response(serializer.data)
    
        elif request.method == 'POST':
            serializer = InstitucionesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def institucion_detail(request, id, format=None):

    try:
        institucion = Instituciones.objects.get(pk=id)
    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InstitucionesSerializer(institucion)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = InstitucionesSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif  request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    