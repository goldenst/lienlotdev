from django.db import models

class Seller(models.Model):
  name = models.CharField(max_length=200)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  def __str__(self):
    return self.name