from django.urls import path
from app1.views import TeacherDetails, TeacherInfo

urlpatterns = [
    path('td/', TeacherDetails.as_view()),
    path('td/<int:pk>/', TeacherInfo.as_view() )
]