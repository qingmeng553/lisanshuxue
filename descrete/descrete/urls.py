from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/lab01/', include('lab01.urls')),
    path('api/lab02/', include('lab02.urls')), 
]