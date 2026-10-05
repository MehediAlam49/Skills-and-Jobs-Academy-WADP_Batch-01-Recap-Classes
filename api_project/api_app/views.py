from rest_framework.decorators import api_view
from django.template.context_processors import request
from rest_framework.response import Response
from api_app.models import *
from api_app.serializers import *

# Create your views here.
@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        student_data= studentModel.objects.all()
        serializer_data= studentSerializer(student_data, many=True)
        return Response({
            "success": True,
            "message": "Student data get successfully",
            "data": serializer_data.data
        })

@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        serializer_data= studentSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                "success": True,
                "message": "Student created successfully",
                "data": serializer_data.data
            })
        return Response({
            "success": False,
            "error": serializer_data.errors
        })