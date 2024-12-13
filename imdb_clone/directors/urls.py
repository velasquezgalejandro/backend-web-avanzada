from django.urls import path, include
from rest_framework.routers import DefaultRouter
from directors.views import DirectorViewSet

# Crear un router para las vistas basadas en viewsets
router = DefaultRouter()
router.register(r"directors", DirectorViewSet)  # Registro de la vista de directores

urlpatterns = [
    path(
        "", include(router.urls)
    ),  # Incluir las rutas generadas automáticamente por el router
]
