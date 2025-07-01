from rest_framework import serializers
from .models import Subject,Course




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



class SubjectModelSerializers(serializers.ModelSerializer):
    courses = CourseModelSerializers(many=True,read_only = True) # Nested serializer
    # full_image_url = serializers.SerializerMethodField(method_name='all_images')   
     
    # def all_images(self,instance):
    #     request = self.context.get('request')
    #     if instance.image:
    #         image_url = instance.image.url
    #         return request.build_absolute_uri(image_url)
    #     return None
    course_count = serializers.IntegerField()
    
    # def get_course_count(self,instance):
    #     return instance.courses.count()
    
    class Meta:
        model = Subject
        fields = '__all__'
        