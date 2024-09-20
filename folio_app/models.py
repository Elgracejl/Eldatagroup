from django.db import models

# Create your models here.
class Blog(models.Model):
    titre=models.CharField(max_length=250)
    framework=models.CharField( max_length=50)
    image=models.ImageField(upload_to="blog/")
    create= models.DateField()
    Update= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class My_portfolio(models.Model):
    titre=models.CharField(max_length=250)
    description=models.CharField( max_length=50)
    image=models.ImageField(upload_to="my_portfolio/")
    categorie=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre
    
class Contact(models.Model):
    prenom=models.CharField(max_length=150)
    nom=models.CharField(max_length=150)
    email=models.EmailField( max_length=254, unique=False)
    sujet=models.CharField(max_length=100)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.sujet}"
    
