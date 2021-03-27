from django.contrib import admin
from django.urls import path
from odb import views
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('anomalies/', views.anomalies),
    path('', views.index)
]
