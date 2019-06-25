from django import forms
from django.core.validators import URLValidator
from .models import CutUrl

class CutUrlForm(forms.ModelForm):
	class Meta:
		model = CutUrl
		fields = ['url_path']
