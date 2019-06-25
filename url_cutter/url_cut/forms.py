from django import forms
from .models import CutUrl

class CutUrlForm(forms.ModelForm):
	class Meta:
		model = CutUrl
		fields = ['url_path']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['url_path'].initial = 'http://www.google.com'