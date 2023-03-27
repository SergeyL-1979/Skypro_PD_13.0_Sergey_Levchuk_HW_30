import json

from django.core.paginator import Paginator
from django.db.models import Count, Avg, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt

from django.views import generic, View
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet

from users.models import Location, User
from avito import settings
from users.serializers import (
    LocationListSerializer,
    LocationDetailSerializer,
    LocationCreateSerializer,
    LocationUpdateSerializer,
    LocationDestroySerializer,
)


# Create your views here.
# UserList ================= ГОТОВАЯ МОДЕЛЬ ПОЛЬЗОВАТЕЛЯ ==================
class UserListView(generic.ListView):
    """Модель отображающая весь список пользователей и вывод на страницу не более 10"""

    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        # user_qs = User.objects.all().order_by("username")
        self.object_list = self.object_list.prefetch_related("location").order_by(
            "username"
        )

        # ========= ПАГИНАЦИЯ С ПОМОЩЬЮ DJANGO ===============
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append(
                {
                    "id": user.pk,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "password": user.password,
                    "role": user.role,
                    "age": user.age,
                    "location": list(map(str, user.location.all())),
                }
            )

        response = {
            "items": users,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
        }

        return JsonResponse(response, safe=False)


# UserDetail ====== ГОТОВАЯ МОДЕЛЬ ДЕТАЛИЗАЦИИ ПОЛЬЗОВАТЕЛЯ ==============
class UserDetailView(generic.DetailView):
    """Отображает детальную информацию об объекте"""

    model = User

    def get(self, request, *args, **kwargs):
        users = self.get_object()

        return JsonResponse(
            {
                "first_name": users.first_name,
                "last_name": users.last_name,
                "username": users.username,
                "password": users.password,
                "role": users.role,
                "age": users.age,
                # "location": users.location.name,
                "location": list(map(str, users.location.all())),
            }
        )


class UserAdsDetailView(View):
    def get(self, request):
        user_qs = User.objects.annotate(
            announce=Count("announcement"),
            filter=Q(announcement__is_published__exact=True),
        )

        paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append(
                {
                    "id": user.pk,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "age": user.age,
                    "location": list(map(str, user.location.all())),
                    "total_ads": user.announce,
                }
            )

        response = {
            "items": users,
            "total": paginator.count,
            "num_page": paginator.num_pages,
            "avg": user_qs.aggregate(avg=Avg("announcement"))["avg"],
        }

        return JsonResponse(response, safe=False)


# UserCreate ====== МОДЕЛЬ СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ =========================
@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(generic.CreateView):
    model = User
    fields = [
        "first_name",
        "last_name",
        "username",
        "password",
        "role",
        "age",
        "location",
    ]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        # При создании модели можно в списке прописать несколько локаций,
        # если таковой нет то добавить локацию в таблицу
        locations = user_data.pop("location")
        user = User.objects.create(**user_data)
        for loc_name in locations:
            loc, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(loc)

        return JsonResponse(
            {
                "id": user.pk,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": user.password,
                "role": user.role,
                "age": user.age,
                "location": list(map(str, user.location.all())),
            }
        )


# UserUpdate ==================== МОДЕЛЬ РЕДАКТИРОВАНИЯ =====================
@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(generic.UpdateView):
    model = User
    fields = [
        "first_name",
        "last_name",
        "username",
        "password",
        "role",
        "age",
        "location",
    ]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"]
        self.object.username = user_data["username"]
        self.object.password = user_data["password"]
        self.object.role = user_data["role"]
        self.object.age = user_data["age"]
        if "location" in user_data:
            self.object.location.clear()
            for loc_name in user_data.get("location"):
                loc, _ = Location.objects.get_or_create(name=loc_name)
                self.object.location.add(loc)
        self.object.save()

        return JsonResponse(
            {
                "id": self.object.pk,
                "first_name": self.object.first_name,
                "last_name": self.object.last_name,
                "username": self.object.username,
                "password": self.object.password,
                "role": self.object.role,
                "age": self.object.age,
                # "location": user.location,
                "location": list(map(str, self.object.location.all())),
            }
        )


# UserDelete ==================== МОДЕЛЬ УДАЛЕНИЕ =====================
@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(generic.DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"STATUS": "DELETE"})


# ================== ПОЛЬЗОВАТЕЛЬ ЗАВЕРШЕН =======================================================


# LocationList =============== ГООТОВАЯ МОДЕЛЬ МЕСТОПОЛОЖЕНИЯ =================
class LocationListViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer


# class LocationListAPIView(ListAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationListSerializer


# LocationDetail ====== МОДЕЛЬ ДЕТАЛИЗАЦИИ ==============
class LocationDetailAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDetailSerializer


# LocationCreate ====== МОДЕЛЬ СОЗДАНИЯ ==============
class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer


# LocationUpdate ======= МОДЕЛЬ РЕДАКТИРОВАНИЯ =======
class LocationUpdateAPIView(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationUpdateSerializer


# LocationDelete ======= МОДЕЛЬ УДАЛЕНИЯ =======
class LocationDeleteAPIView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDestroySerializer
