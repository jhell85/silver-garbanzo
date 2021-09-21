from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Ebook(models.Model):
  title = models.CharField(max_length=140)
  author = models.CharField(max_length=60)
  descrption = models.TextField()
  publication_date = models.DateField()
  
  def __str__(self):
    return self.title
  
class Review(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  review_author = models.CharField(max_length=8, blank=True, null=True)
  review = models.TextField(blank=True, null=True)
  rating = models.PositiveIntegerField(validators=[
                                                    MinValueValidator(1),
                                                    MaxValueValidator(5)])