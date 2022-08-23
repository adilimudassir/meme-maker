from rest_framework import routers

from meme.views import MemeViewSet
app_name = 'meme'


router = routers.DefaultRouter()
router.register(r"", MemeViewSet, basename="memes")

urlpatterns = router.urls