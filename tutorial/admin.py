from django.contrib import admin
from .models import tutorial,TutorialSeries,TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class tutorialAdmin(admin.ModelAdmin):


    fieldsets= [
            ('title/date', {'fields':['tutorial_title', 'tutorial_published']}),
            ('URL', {'fields':['tutorial_slug']}),
            ('Series', {'fields':['tutorial_series']}),
            ('content', {'fields':['tutorial_content']})
    ]
    formfield_overrides ={
       models.TextField:{'widget':TinyMCE()}
    }


admin.site.register(tutorial,tutorialAdmin)
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
