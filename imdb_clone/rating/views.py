# Create your views here.
from rest_framework import viewsets
from rating.models import Rating
from rating.serializers import RatingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# vista para Rating
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
