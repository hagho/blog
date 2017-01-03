from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100) #blog title
    category = models.CharField(max_length = 50, blank = True) #blog tag
    date_time = models.DateTimeField(auto_now_add = True) # blog date
    content = models.TextField(blank = True,  null = True) #blog content

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']