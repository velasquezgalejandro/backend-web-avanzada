from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comments.views import CommentsViewSet

# Crear un router para las vistas basadas en viewsets
router = DefaultRouter()
router.register(r"comments", CommentsViewSet)  # Registro de la vista de películas

urlpatterns = [
    path(
        "", include(router.urls)
    ),  # Incluir las rutas generadas automáticamente por el router
]
