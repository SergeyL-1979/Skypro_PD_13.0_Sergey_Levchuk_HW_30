from rest_framework.viewsets import ModelViewSet

from category.models import Category
from category.serializers import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
    CategoryDestroySerializer,
)


# Create your views here.
class CategoryListViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


# class CategoryDetailViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailSerializer
#
# class CategoryCreateViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategoryCreateSerializer
#
# class CategoryUpdateViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategoryUpdateSerializer
#
# class CategoryDeleteViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDestroySerializer


# CategoryList ======================= ГОТОВАЯ МОДЕЛЬ КАТЕГОРИИ =================================
# @method_decorator(csrf_exempt, name="dispatch")
# class CategoryListView(generic.ListView):
#     """Модель отображает все объекты"""
#
#     model = Category
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         self.object_list = self.object_list.order_by("name")
#
#         paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#
#         category_list = []
#         for category in page_obj:
#             category_list.append(
#                 {
#                     "id": category.pk,
#                     "name": category.name,
#                 }
#             )
#
#         response = {
#             "items": category_list,
#             "total": paginator.count,
#             "num_page": paginator.num_pages,
#         }
#         return JsonResponse(
#             response, safe=False, json_dumps_params={"ensure_ascii": False}
#         )
#
#
# # CategoryDetail =============== ГОТОВАЯ КАТЕГОРИЯ ДЕТАЛИЗАЦИИ ==============
# class CategoryDetailView(generic.DetailView):
#     """Вывод деталей категории"""
#
#     model = Category
#
#     def get(self, request, *args, **kwargs):
#         category = self.get_object()
#
#         return JsonResponse(
#             {
#                 "id": category.pk,
#                 "name": category.name,
#             }
#         )
#
#
# # CategoryCreate ========= МОДЕЛЬ КАТЕГОРИЯ СОЗДАНИЯ ================
# @method_decorator(csrf_exempt, name="dispatch")
# class CategoryCreateView(generic.CreateView):
#     model = Category
#     fields = [
#         "name",
#     ]
#
#     def post(self, request, *args, **kwargs):
#         category_data = json.loads(request.body)
#
#         category = Category.objects.create(
#             name=category_data["name"],
#         )
#
#         return JsonResponse(
#             {
#                 "id": category.pk,
#                 "name": category.name,
#             }
#         )
#
#
# # CategoryUpdate =========== МОДЕЛЬ РЕДАКТИРОВАНИЯ КАТЕГОРИИ ===================
# @method_decorator(csrf_exempt, name="dispatch")
# class CategoryUpdateView(generic.UpdateView):
#     model = Category
#     fields = [
#         "name",
#     ]
#
#     def post(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#
#         category_data = json.loads(request.body)
#
#         self.object.name = category_data["name"]
#         self.object.save()
#
#         return JsonResponse(
#             {
#                 "id": self.object.pk,
#                 "name": self.object.name,
#             }
#         )
#
#
# # CategoryDelete =========== МОДЕЛЬ УДАЛЕНИЕ КАТЕГОРИИ ===================
# @method_decorator(csrf_exempt, name="dispatch")
# class CategoryDeleteView(generic.DeleteView):
#     model = Category
#     success_url = "/"
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({"STATUS": "DELETED"})
#
#
# # =========================== ЗАВЕРШЕНИЕ МОДЕЛИ КАТЕГОРИИ =============================
