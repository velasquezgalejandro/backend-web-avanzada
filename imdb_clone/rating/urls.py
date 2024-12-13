from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rating.views import RatingViewSet

# Crear un router para las vistas basadas en viewsets
router = DefaultRouter()
router.register(r"rating", RatingViewSet)  # Registro de la vista de películas

urlpatterns = [
    path(
        "", include(router.urls)
    ),  # Incluir las rutas generadas automáticamente por el router
]
