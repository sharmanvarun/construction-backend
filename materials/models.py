from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    image = models.ImageField(upload_to='material_images/', null=True, blank=True)

    def __str__(self):
        return self.name
