# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="/usr/share/nginx/html/media/")

# Create your models here.

class ProjectType(models.Model):
    title = models.CharField(max_length = 1000)
    priority = models.IntegerField(null = True, blank = True)
    def __str__(self):
        return self.title

class Project(models.Model):
    project_type = models.ForeignKey(ProjectType, models.SET_NULL, null=True,blank=True)
    title = models.CharField(max_length = 1000000, null = True, blank = True)
    description = models.TextField(max_length = 1000000, null = True, blank = True)
    link = models.URLField(max_length = 1000000, blank = True, null = True)
    proj_image = models.ImageField(upload_to = fs, blank = True, null = True)
    last_updated = models.DateField(null = True, blank = True)
    tools_used = models.CharField(max_length = 100000, null = True, blank = True)
    source_code = models.URLField(max_length = 100000, blank = True, null = True)
    priority = models.IntegerField(null = True, blank = True)
    def __str__(self):
        return self.title
