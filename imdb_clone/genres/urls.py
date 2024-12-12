from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet

# Crear un router para las vistas basadas en viewsets
router = DefaultRouter()
router.register(r"genres", GenreViewSet)  # Registro de la vista de géneros

urlpatterns = [
    path(
        "", include(router.urls)
    ),  # Incluir las rutas generadas automáticamente por el router
]
