from ads.favorite import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', FavoriteViewSet)
urlpatterns = router.urls


