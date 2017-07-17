# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 1000000, null = True, blank = True)
    description = models.TextField(max_length = 1000000, null = True, blank = True)
    link = models.URLField(max_length = 1000000, default = "https://sadieparker.net")
    image_name = models.CharField(max_length = 2000, default = "default")
    last_updated = models.DateField(null = True, blank = True)
    tools_used = models.CharField(max_length = 100000, null = True, blank = True)
    def __str__(self):
        return self.title

