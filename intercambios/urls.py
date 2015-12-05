from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'intercambios', views.IntercambioViewSet)
router.register(r'usuarios', views.UserViewSet)
