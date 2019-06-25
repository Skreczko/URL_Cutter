from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url_path(value):
	val = URLValidator()
	try:
		val(f'{value}')
	except:
		raise ValidationError('Incorrect website (i.e. http://www.google.com)')
	else:
		return value