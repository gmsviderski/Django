from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('part2', views.part2, name='part2'),
    path('part3', views.part3, name='part3'),
    path('artists', views.artists, name='personage')

]