from django import forms
from .models import CutUrl

class CutUrlForm(forms.ModelForm):
	class Meta:
		model = CutUrl
		fields = ['urlpath']
		label = {
			'urlpath': 'URL to cut'
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['urlpath'].widget.attrs['placeholder'] = 'http://www.google.com'