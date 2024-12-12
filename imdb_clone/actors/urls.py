from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActorViewSet

# Crear un router para las vistas basadas en viewsets
router = DefaultRouter()
router.register(r"actors", ActorViewSet)  # Registro de la vista de actores

urlpatterns = [
    path(
        "", include(router.urls)
    ),  # Incluir las rutas generadas automáticamente por el router
]
