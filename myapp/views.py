from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import StudentSerializer
from .models import Student

# Create your views here.

class StudentView(APIView):
  def get(self, request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET','PATCH', 'DELETE'])
def update_student(request, id):
  if request.method == 'GET':
    try:
      student = Student.objects.filter(id=id)
    except Exception as e:
      return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)

  if request.method == 'PATCH':
    try:
      student = Student.objects.filter(id=id)
    except Exception as e:
      return Response(status=status.HTTP_404_NOT_FOUND)
    student.update(**request.data)
    return HttpResponseRedirect(f'{int(id)}')

  if request.method == 'DELETE':
    try:
      student = Student.objects.filter(id=id)
    except Exception as e:
      return Response(status=status.HTTP_404_NOT_FOUND)
    student.delete()
    return HttpResponse('{"message": "data deleted successfully"}', status=status.HTTP_204_NO_CONTENT)