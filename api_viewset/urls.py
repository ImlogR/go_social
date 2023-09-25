from .views import UserViewset
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'users', UserViewset, basename='user')
urlpatterns = router.urls