from django.urls import path,include
from .views import SubjectListCreateAPIView,SubjectDetailAPIView

urlpatterns = [
    # path('users/',UserInfo.as_view(),),
    path('subjects/',SubjectListCreateAPIView.as_view()),
    # path('subjects/create/',SubjectCreate.as_view()),

    path('subjects/<int:subject_id>',SubjectDetailAPIView.as_view()),
    
]