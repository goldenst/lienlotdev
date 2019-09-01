from django.db import models
from datetime import datetime
from sellers.models import Seller

class Listing(models.Model):
  seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
  # yard = models.CharField(max_length=20)
  # lot_num = models.IntegerField()
  year = models.CharField(max_length=4)
  make = models.CharField(max_length=20)
  model = models.CharField(max_length=20)
  vin = models.CharField(max_length=17)
  engine = models.CharField(max_length=20)
  fuel = models.CharField(max_length=20)
  # reg_date = models.DateTimeField(blank=True)
  catagory = models.CharField(max_length=20)
  price = models.IntegerField()
  # odom = models.IntegerField()
  keys = models.BooleanField(default=True)
  comment = models.TextField(blank=True)
  avalible_date = models.DateTimeField(blank=True)
  is_published = models.BooleanField(default=True)
  photo_main = models.ImageField(upload_to='photos/%Y%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y%m/%d/', blank=True)
  def __str__(self):
    return self.make

  

