from django.shortcuts import render
from app1.models import Teacher
from app1.serializers import TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TeacherDetails(APIView):

    def get(self, request):
        teach = Teacher.objects.all()
        serializer = TeacherSerializer(teach, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherInfo(APIView):

    def get(self, request, pk):
        try:
            teach = Teacher.objects.get(id=pk)
        except Teacher.DoesNotExist:
            msg = {'msg': "Teacher Does not Exist."}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teach)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        try:
            teach = Teacher.objects.get(id=pk)
        except Teacher.DoesNotExist:
            msg = {'msg': "Teacher Does not Exist."}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teach, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request, pk):
        try:
            teach = Teacher.objects.get(id=pk)
        except Teacher.DoesNotExist:
            msg = {"msg": "Teacher Does not Exist."}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serilaizer = TeacherSerializer(teach, data= request.data, partial=True)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            teach = Teacher.objects.get(id=pk)
        except Teacher.DoesNotExist:
            msg = {'msg': "Teacher Does not Exist."}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        teach.delete()
        return Response({"msg":"Record Deleted..."}, status=status.HTTP_204_NO_CONTENT)
