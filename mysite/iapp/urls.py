from django.urls import path
from iapp import views
urlpatterns = [
    path('',views.home,name='home'),
]
