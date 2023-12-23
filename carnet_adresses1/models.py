from django.db import models


class Groupe(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Adresse(models.Model):
    rue = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.rue}, {self.code_postal} {self.ville}"


class Contact(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    autres_informations = models.TextField(blank=True)
    groupes = models.ManyToManyField(Groupe, related_name='contacts')

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        db_table = 'contact'  # Nom de la table dans la base de données MySQL
