from django.urls import path
from rest_framework.authtoken import views as auth_views
from . import views


urlpatterns = [
    path('signin/', auth_views.obtain_auth_token),
    path('polls/', views.api_polls_list),
    path('polls/<int:id>/', views.api_polls),
    path('answers/', views.api_answers),
]
