from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject
from rest_framework.status import HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from .serializers import SubjectModelSerializers
# Create your views here.


class UserInfo(APIView):
    def get(self,request):
        user_data = {
            '1':{
                'name':'Iphone 16',
                'description':'blahblablha',
                'price':2525,
                'image':'htpps://www.com',
                'cateogry':'Apple'
            }
        }
        return Response(user_data)
    


class SubjectList(APIView):
    def get(self,request):
        subjects = Subject.objects.all().order_by('id')
        serializers = SubjectModelSerializers(subjects,many=True)
        return Response(serializers.data,status=HTTP_200_OK)
    
    
class SubjectDetail(APIView):
    def get(self,request,pk):
        try:
            subject = Subject.objects.get(id = pk)
            serializer = SubjectModelSerializers(subject)
            return Response(serializer.data,status=HTTP_200_OK)
        except Subject.DoesNotExist:
            subject = None
            data = {
                'status':HTTP_404_NOT_FOUND,
                'message':'Subject NOT FOUND'
            }
            return Response(data)
        
        
class SubjectCreate(APIView):
    def post(self,request):
        serializer = SubjectModelSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f'{serializer.data['title']} successfully created',status=HTTP_201_CREATED)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        
        
        
'''



[
    {
        "id": 1,
        "title": "Web dasturlash",
        "course_count":4
        "image": "/media/subjects/web.jpeg",
        "courses":[
            {},
            {},
            {}
        ]
    },
    {
        "id": 2,
        "title": "SMM Pro",
        "image": "/media/subjects/smm.jpeg"
    },
    {
        "id": 3,
        "title": "test",
        "image": null
    },
    {
        "id": 4,
        "title": "test2",
        "image": null
    },
    {
        "id": 5,
        "title": "sherali",
        "image": null
    }
]




'''