from django.urls import path
from . import views

urlpatterns = [
    path('', views.Courses, name='home-page'),
    path('<int:couse_id>/', views.details, name='details'),
]
