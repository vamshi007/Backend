from rest_framework import routers
from .views import SampleViewset
router = routers.SimpleRouter()
router.register('',SampleViewset)

urlpatterns = router.urls
