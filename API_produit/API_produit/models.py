from django.db import models

class Produit(models.Model):
    """
    Modèle pour représenter un produit
    """
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits" 