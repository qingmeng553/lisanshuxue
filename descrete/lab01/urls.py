from django.urls import path
from .views import truth_table

urlpatterns = [
    path('truth_table/', truth_table),
]