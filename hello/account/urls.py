from . import views
from django.urls import path

urlpatterns = [
    # path('', )
    path('login/', views.user_login, name='login'),
]