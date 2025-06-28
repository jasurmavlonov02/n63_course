from django.urls import path,include
from .views import UserInfo,SubjectList,SubjectDetail,SubjectCreate


urlpatterns = [
    path('users/',UserInfo.as_view(),),
    path('subjects/',SubjectList.as_view()),
    path('subjects/create/',SubjectCreate.as_view()),

    path('subjects/<int:pk>',SubjectDetail.as_view()),
    
]