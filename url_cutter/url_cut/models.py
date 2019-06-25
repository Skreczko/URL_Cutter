import random, string
from django.db.models.signals import pre_save
from django.db import models
from .validators import validate_url_path

# Create your models here.

class CutUrl(models.Model):
	urlpath = models.CharField(max_length=512, validators=[validate_url_path], verbose_name='URL to cut')
	urlcutted = models.CharField(max_length=5)

	def __str__(self):
		return f'{self.urlpath} into {self.urlcutted}'


def check_url_for_cutted(instance):
	newurlcutted = ''.join(random.choice(str(random.randint(0,10)) + string.ascii_uppercase + string.ascii_lowercase) for x in range(5))
	qs = CutUrl.objects.filter(urlcutted=newurlcutted)
	if qs.exists():
		return check_url_for_cutted(instance)
	return newurlcutted


def pre_save_CutUrl(instance, sender, *args, **kwargs):
	if not instance.urlcutted:
		instance.urlcutted = check_url_for_cutted(instance)


pre_save.connect(pre_save_CutUrl, sender=CutUrl)