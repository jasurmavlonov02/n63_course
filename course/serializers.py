from rest_framework import serializers
from .models import Subject,Course
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.pagination import LimitOffsetPagination



class CourseModelSerializers(serializers.ModelSerializer):
    subject_title = serializers.StringRelatedField(source='subject.title')
    subject_slug = serializers.SlugRelatedField(
        source = 'subject',
        slug_field = 'slug',
        read_only = True
    )  
    username = serializers.CharField(source = 'owner.username')
    
    
    class Meta:
        model = Course
        fields = '__all__'



class SubjectSerializers(serializers.ModelSerializer):
    
    # def get_course_count(self,instance):
    #     return instance.courses.count()
    
    class Meta:
        model = Subject
        fields = '__all__'
        
   
    

class UserModelSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

        
    
    def validate_password(self,value):

        if len(value) < 6:
            raise serializers.ValidationError("Parol kamida 6 ta belgidan iborat bo'lishi kerak.")
        
        return value

        
        

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        # Bu qism - token javobining tashqarisiga qo‘shiladigan maydonlar
        data['username'] = self.user.username
        data['user_id'] = self.user.id
        data['email'] = self.user.email
        data['created_at'] = datetime.now()
        return data