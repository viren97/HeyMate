from django.db import models
from datetime import datetime

# Create your models here.
class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length= 200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)#for url

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category
class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory,default = 1, verbose_name = "category",on_delete = models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series


class tutorial(models.Model):
        tutorial_title = models.CharField(max_length=20)
        tutorial_content = models.TextField()
        tutorial_published = models.DateTimeField("date published", default= datetime.now())

        tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="series", on_delete= models.SET_DEFAULT)
        tutorial_slug = models.CharField(max_length=200, default=1)
        def __str__(self):
            return self.tutorial_title
