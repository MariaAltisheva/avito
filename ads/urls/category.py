from ads.views.category import *
from django.urls import path

# urlpatterns = [
#     path('', CategoryListCreateView.as_view()),
#     path('<int:pk>', CategoryDetailView.as_view()),
# ]


urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view()),
    path('<int:pk>/update/', CategoryUpdateView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('<int:pk>/delete/', CategoryDeleteView.as_view()),
]