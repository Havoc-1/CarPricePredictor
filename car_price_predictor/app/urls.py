from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('streamlit/', views.streamlit_app, name='streamlit_app'),
]