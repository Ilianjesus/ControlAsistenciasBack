from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, JovenViewSet, EventoViewSet, AsistenciaViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'jovenes', JovenViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'asistencias', AsistenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]