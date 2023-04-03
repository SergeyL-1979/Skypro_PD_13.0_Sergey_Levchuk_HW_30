from django.db.models import Q
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from ads.models import Announcement
from ads.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from ads.serializers import AnnouncementListSerializer, AnnouncementDetailSerializer, \
    AnnouncementSerializer, AnnouncementCreateSerializer


def root(request):
    return JsonResponse({"STATUS": "OK!"})


# AnnouncementList ================= ГОТОВАЯ МОДЕЛЬ ОБЪЯВЛЕНИЯ ========================
class AnnouncementPagination(PageNumberPagination):
    page_size = 5

class AnnouncementListViewSet(ListAPIView):
    """ """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListSerializer
    pagination_class = AnnouncementPagination

    def get(self, request, *args, **kwargs):
        announcement_text = request.GET.get("text", None)
        if announcement_text:
            self.queryset = self.queryset.filter(name__icontains=announcement_text)

        cat_name = request.GET.get("category", None)
        if cat_name:
            self.queryset = self.queryset.filter(category_id__in=cat_name)

        location_name = request.GET.get("location", None)
        if location_name:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=location_name
            )

        price = request.GET.getlist("price", None)
        price_q = None
        for p in price:
            if price_q is None:
                price_q = Q(price=p)
            else:
                price_q |= Q(price=p)

        if price_q:
            self.queryset = self.queryset.filter(price_q)

        return super().get(request, *args, **kwargs)

class AnnouncementDetailViewSet(RetrieveAPIView):
    """ """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailSerializer
    permission_classes = [IsAuthenticated, ]


class AnnouncementCreateViewSet(CreateAPIView):
    """ """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementCreateSerializer
    permission_classes = [IsAuthenticated, ]

class AnnouncementUpdateViewSet(UpdateAPIView):
    """ """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class AnnouncementDeleteViewSet(DestroyAPIView):
    """ """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly, IsOwnerOrReadOnly | IsAdminOrReadOnly]



