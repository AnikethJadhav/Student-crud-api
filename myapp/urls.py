from django.urls import path

from . import views

urlpatterns = [
  path('', views.StudentView.as_view()),
  path('students/<int:id>', views.update_student)
]