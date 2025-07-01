from django.urls import path,include
from .views import SubjectListCreateAPIView,SubjectDetailAPIView,CourseListAPIView

urlpatterns = [
    # path('users/',UserInfo.as_view(),),
    path('subjects/',SubjectListCreateAPIView.as_view()),
    # path('subjects/create/',SubjectCreate.as_view()),

    path('subjects/<int:subject_id>',SubjectDetailAPIView.as_view()),
    #course
    
    path('courses/',CourseListAPIView.as_view()),
    
]