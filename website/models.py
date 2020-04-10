# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from PIL import Image as PILImage
from PIL import ImageOps

from io import BytesIO
import base64
from django.core.files.base import ContentFile, File
from copy import copy

# Create your models here.

class ProjectType(models.Model):
    title = models.CharField(max_length = 1000)
    priority = models.IntegerField(null = True, blank = True)
    def __str__(self):
        return self.title

class Review(models.Model):
    album_name = models.CharField(max_length = 10000, null = True, blank = True)
    artist_name = models.CharField(max_length = 10000, null = True, blank = True)
    date_reviewed = models.DateField(null = True, blank = True)
    review_text = models.TextField(max_length = 1000000, null = True, blank = True)
    album_image = models.ImageField(upload_to = '', blank = True, null = True)
    link = models.URLField(max_length = 1000000, blank = True, null = True)
    def __str__(self):
        return self.album_name

class Project(models.Model):
    project_type = models.ForeignKey(ProjectType, models.SET_NULL, null=True,blank=True)
    title = models.CharField(max_length = 1000000, null = True, blank = True)
    description = models.TextField(max_length = 1000000, null = True, blank = True)
    link = models.URLField(max_length = 1000000, blank = True, null = True)
    proj_image = models.ImageField(upload_to = '', blank = True, null = True)
    last_updated = models.DateField(null = True, blank = True)
    tools_used = models.CharField(max_length = 100000, null = True, blank = True)
    source_code = models.URLField(max_length = 100000, blank = True, null = True)
    priority = models.IntegerField(null = True, blank = True)
    image_data_uri = models.CharField(null=True, blank=True, default="", max_length=100000000)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        previous_image = copy(self.proj_image)
        super(Project, self).save(*args, **kwargs)

        #make smaller size of the image
        if (self.proj_image and previous_image.name != self.proj_image.name):
        #if there was an image and you're replacing with another one, do it
            image = PILImage.open(self.proj_image.path)
            if image.width > 1000 or image.height > 1000:
                if (image.width <= image.height):
                    ratio = 1000.0 / image.width
                elif (image.height <= image.width):
                    ratio = 1000.0 / image.height
                new_width = int(image.width * ratio)
                new_height = int(image.height * ratio)
                image = image.resize((new_width,new_height), PILImage.ANTIALIAS)
                tn_buffer = BytesIO()
                tn_buffer.seek(0)
                print("image saving")
                image.save(fp=tn_buffer, format='PNG')
                print("proj image saving")
                self.proj_image.save(self.proj_image.name,
                               ContentFile(tn_buffer.getvalue()), save=False)

            print("making data uri")
            #make data uri
            if (image.width <= image.height):
                ratio = 50.0 / image.width
            elif (image.height <= image.width):
                ratio = 50.0 / image.height
            new_width = int(image.width * ratio)
            new_height = int(image.height * ratio)
            image = image.resize((new_width,new_height), PILImage.ANTIALIAS)
            buffered = BytesIO()
            image.save(fp=buffered, format='PNG')
            im_data = buffered.getvalue()
            print("im data:")
            print(im_data)
            self.image_data_uri = 'data:image/png;base64,' + base64.b64encode(im_data).decode(encoding="utf-8", errors="strict")
            image.close()
            super(Project, self).save(*args, **kwargs)

