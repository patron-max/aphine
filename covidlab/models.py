from django.db import models

'''
analis
============
slug, idnp, fio, Birthday, created_at, tested_at, laborant_name, valid_to, igG, igM, igA, url_qr_pics 
'''

class Analis(models.Model):
    nranalis = models.IntegerField(max_length=9, verbose_name='nranalis', unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    idnp = models.IntegerField(max_length=13, verbose_name='idnp')
    fio = models.CharField(max_length=255)
    birthday = models.DateTimeField(verbose_name='birthday')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    tested_at = models.DateTimeField(verbose_name='tested_at')
    laborant_name = models.CharField(max_length=255)
    valid_to = models.DateTimeField(verbose_name='valid_to')
    igG = models.IntegerField(default=0)
    igM = models.IntegerField(default=0)
    igA = models.IntegerField(default=0)
    url_qr_pics = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
