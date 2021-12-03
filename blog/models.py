from typing import OrderedDict
from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
import datetime

class Posts(models.Model):
    title = CharField(max_length=100, verbose_name='Titulo')
    description = RichTextField(verbose_name='Descripcion')
    image = ImageField(upload_to="blog/images", verbose_name='Imagen')
    date = DateField(datetime.date.today)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
