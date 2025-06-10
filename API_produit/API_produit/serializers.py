from rest_framework import serializers
from .models import Produit

class ProduitSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Produit
    """
    class Meta:
        model = Produit
        fields = ['id', 'nom', 'description', 'prix', 'date_creation', 'date_modification']
        read_only_fields = ['date_creation', 'date_modification'] 