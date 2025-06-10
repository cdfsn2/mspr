from rest_framework import serializers
from .models import Produit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'nom', 'description', 'prix', 'quantité_en_stock']
