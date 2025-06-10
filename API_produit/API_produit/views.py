from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Produit
from .serializers import ProduitSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les produits.
    Permet de créer, lire, mettre à jour et supprimer des produits.
    """
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    permission_classes = [IsAuthenticated] 