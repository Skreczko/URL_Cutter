import random, string
from django.db.models.signals import pre_save
from django.db import models
from .validators import validate_url_path

# Create your models here.

class CutUrl(models.Model):
	url_path = models.CharField(max_length=512, validators=[validate_url_path], verbose_name='URL to cut')
	url_cutted = models.CharField(max_length=5)

	def __str__(self):
		return f'{self.url_path} into {self.url_cutted}'


def check_url_cutted(instance):
	new_url_cutted = ''.join(random.choice(str(random.randint(0,10)) + string.ascii_uppercase + string.ascii_lowercase) for x in range(5))
	qs = CutUrl.objects.filter(url_cutted=new_url_cutted)
	if qs.exists():
		return check_url_cutted(instance)
	return new_url_cutted


def pre_save_CutUrl(instance, sender, *args, **kwargs):
	if not instance.url_cutted:
		instance.url_cutted = check_url_cutted(instance)


pre_save.connect(pre_save_CutUrl, sender=CutUrl)