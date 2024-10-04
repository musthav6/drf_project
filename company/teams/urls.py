# teams/urls.py
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'people', PersonViewSet)

urlpatterns = router.urls
