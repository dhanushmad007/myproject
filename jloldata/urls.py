from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Default Home Page
    path('jloldata/', views.jloldata_view, name='jloldata'),  # JlolData Page
]
