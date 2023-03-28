from django.db.models import Count, Q

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from users.models import Location, User
from users.serializers import (
    LocationListSerializer,
    LocationDetailSerializer,
    LocationCreateSerializer,
    LocationUpdateSerializer,
    LocationDestroySerializer,
    UserSerializer, UserCreateSerializer,
    UserUpdateSerializer, UserListSerializer
)


# ======== ГОТОВАЯ МОДЕЛЬ МЕСТОПОЛОЖЕНИЯ ======================
class LocationListViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer

# class LocationListAPIView(ListAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationListSerializer


class LocationDetailAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDetailSerializer


class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer


class LocationUpdateAPIView(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationUpdateSerializer


class LocationDeleteAPIView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDestroySerializer


# === ПАГИНАЦИЯ С ПОМОЩЬЮ REST FRAMEWORK ===================
class UserPagination(PageNumberPagination):
    page_size = 4


# ================= ГОТОВАЯ МОДЕЛЬ ПОЛЬЗОВАТЕЛЯ ==================
class UserDetailView(RetrieveAPIView):
    """ Отображает детальную информацию об объекте """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(ListAPIView):
    """ """
    queryset = User.objects.annotate(total_ads=Count("announcement", filter=Q(announcement__is_published=True)))
    serializer_class = UserListSerializer
    pagination_class = UserPagination

class UserCreateView(CreateAPIView):
    """ """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    """ """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    """ """
    queryset = User.objects.all()
    serializer_class = UserSerializer

