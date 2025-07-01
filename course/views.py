from django.shortcuts import render
from django.db.models import Avg,Count,Max
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject,Course
from rest_framework.status import HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from .serializers import SubjectModelSerializers,CourseModelSerializers
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.


class SubjectListCreateAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectModelSerializers
    
    def get_queryset(self):
        queryset = Subject.objects.all()
        queryset = queryset.annotate(course_count=Count('courses'))
        queryset = queryset.order_by('course_count')
        return queryset
    
    
class SubjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectModelSerializers
    # lookup_field = 'subject_id'
    lookup_url_kwarg = 'subject_id'


# class SubjectList(APIView):
#     def get(self,request):
#         subjects = Subject.objects.all().order_by('id')
#         serializers = SubjectModelSerializers(subjects,many=True,context = {"request": request})
#         return Response(serializers.data,status=HTTP_200_OK)
    
    
# class SubjectList(ListAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectModelSerializers
    
    
# class SubjectDetail(APIView):
#     def get(self,request,pk):
#         try:
#             subject = Subject.objects.get(id = pk)
#             serializer = SubjectModelSerializers(subject)
#             return Response(serializer.data,status=HTTP_200_OK)
#         except Subject.DoesNotExist:
#             subject = None
#             data = {
#                 'status':HTTP_404_NOT_FOUND,
#                 'message':'Subject NOT FOUND'
#             }
#             return Response(data)
        
        
# class SubjectCreate(APIView):
#     def post(self,request):
#         serializer = SubjectModelSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(f'{serializer.data['title']} successfully created',status=HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        
        
class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializers
    