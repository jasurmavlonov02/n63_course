from django.shortcuts import render
from django.db.models import Avg,Count,Max
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject,Course
from rest_framework.status import HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT
from .serializers import SubjectSerializers,CourseModelSerializers,UserModelSerializers
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView)

from rest_framework import permissions,authentication,pagination
from .permissions import IsOwnerOrReadOnly,WeekDayOnlyAccess,IsJohnBlocked,CanJohnRead,WorkDayOnlyAccess,CanReadPremiumCourse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Prefetch




# Create your views here.


class SubjectListCreateAPIView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Subject.objects.all()
        queryset = queryset.annotate(course_count=Count('courses'))
        queryset = queryset.order_by('course_count')
        # queryset = queryset.prefetch_related('courses')
        return queryset
    
    
class SubjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers
    # lookup_field = 'subject_id'
    lookup_url_kwarg = 'subject_id'

    

class SubjectCoursesListAPIView(ListAPIView):
    serializer_class = CourseModelSerializers
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        queryset = Course.objects.filter(subject_id=subject_id).order_by('id')
        queryset = queryset.select_related('owner','subject')
        return queryset
    
    
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
    
    def get_queryset(self):
        queryset = Course.objects.all().select_related('owner','subject')
        return queryset
    
    # permission_classes = [WorkDayOnlyAccess]
    
class CourseDetailAPIVIew(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializers
    permission_classes = [WorkDayOnlyAccess]
    
class PremiumCourse(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializers
    permission_classes = [CanReadPremiumCourse]
    
    def get_queryset(self):
        queryset = Course.objects.filter(is_premium = True)
        return queryset
    
    
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserModelSerializers(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        'token': token.key,
                        'username':user.username
                        }
                    )
            else:
                return Response({'error': 'User Not Found'}, status=401)
            
        return Response(serializer.errors, status=400)



class LogoutAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response(
                    {"detail": "Token not found."},
                    status=HTTP_400_BAD_REQUEST
                )
        return Response(
            {"detail": "Logged out successfully."},
            status=HTTP_204_NO_CONTENT
            )
        
        
        
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
