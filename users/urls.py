from users.views import *
from django.urls import path

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    # path('create/', AdCreateView.as_view()),
    # path('<int:pk>/delete/', AdDeleteView.as_view()),
]