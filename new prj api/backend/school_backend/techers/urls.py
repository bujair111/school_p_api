from django.urls import path
from . import views

app_name = 'teachers'


urlpatterns = [
    path('teachers',views.teachers,name = 'teachers')

]