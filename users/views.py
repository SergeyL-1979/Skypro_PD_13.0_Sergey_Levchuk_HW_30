from django.db.models import Count, Q
from rest_framework import status

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from users.models import Location, User
from users.serializers import (
    LocationListSerializer,
    UserSerializer, UserCreateSerializer,
    UserUpdateSerializer, UserListSerializer
)


# ======== ГОТОВАЯ МОДЕЛЬ МЕСТОПОЛОЖЕНИЯ ======================
class LocationListViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer


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


class Logout(APIView):
    """ """
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
