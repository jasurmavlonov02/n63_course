from django.urls import path,include
from .views import SubjectListCreateAPIView,SubjectDetailAPIView,CourseListAPIView,CourseDetailAPIVIew,PremiumCourse,UserLoginView,LogoutAPIView,SubjectCoursesListAPIView

urlpatterns = [
    # path('users/',UserInfo.as_view(),),
    path('subjects/',SubjectListCreateAPIView.as_view()),
    # path('subjects/create/',SubjectCreate.as_view()),

    path('subjects/<int:subject_id>/',SubjectDetailAPIView.as_view()),
    path('subjects/<int:subject_id>/courses/',SubjectCoursesListAPIView.as_view()),
    #course
    
    path('courses/',CourseListAPIView.as_view()),
    path('premium/course/',PremiumCourse.as_view()),
    path('courses/<int:pk>/',CourseDetailAPIVIew.as_view(),),
    path('login/',UserLoginView.as_view(),),
    path('logout/',LogoutAPIView.as_view(),),
    
]