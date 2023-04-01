from django.urls import path

from ads import views

urlpatterns = [
    path("", views.AnnouncementListViewSet.as_view()),
    path("<int:pk>/", views.AnnouncementDetailViewSet.as_view()),
    path("create/", views.AnnouncementCreateViewSet.as_view()),
    path("<int:pk>/update/", views.AnnouncementUpdateViewSet.as_view()),
    path("<int:pk>/delete/", views.AnnouncementDeleteViewSet.as_view()),

    # path("selection/", views.FavoriteViewSet.as_view()),
]
