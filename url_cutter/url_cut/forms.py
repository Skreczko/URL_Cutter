from django import forms
from .models import CutUrl

class CutUrlForm(forms.ModelForm):
	class Meta:
		model = CutUrl
		fields = ['url_path']
		label = {
			'url_path': 'URL to cut'
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['url_path'].widget.attrs['placeholder'] = 'http://www.google.com'