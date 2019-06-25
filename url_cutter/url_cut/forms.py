from django import forms
from django.core.validators import URLValidator
from .models import CutUrl

class CutUrlForm(forms.ModelForm):
	class Meta:
		model = CutUrl
		fields = ['url_path']

	def clean_url_path(self):
		url_path = self.cleaned_data.get('url_path')
		val = URLValidator(verify_exists=False)
		try:
			val(f'{url_path}')

		except:
			raise forms.ValidationError('Incorrect website')
		else:
			return url_path
