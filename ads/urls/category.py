from ads.views.category import *
from django.urls import path

urlpatterns = [
    path('', CategoryListCreateView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view()),
]