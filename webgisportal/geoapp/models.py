from django.contrib.gis.db import models

# Create your models here.
class Tree(models.Model):
    tree_id = models.IntegerField(primary_key=True)
    position = models.PointField()