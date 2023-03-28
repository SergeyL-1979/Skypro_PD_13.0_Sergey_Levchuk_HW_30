from django.urls import path

from category import views

urlpatterns = [
    path("", views.CategoryListViewSet.as_view()),
    path("<int:pk>/", views.CategoryDetailViewSet.as_view()),
    path("create/", views.CategoryCreateViewSet.as_view()),
    path("<int:pk>/update/", views.CategoryUpdateViewSet.as_view()),
    path("<int:pk>/delete/", views.CategoryDeleteViewSet.as_view()),
]
