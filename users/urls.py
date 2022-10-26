from users.views import *
from django.urls import path

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
]