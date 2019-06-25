from django.contrib import admin
from .models import CutUrl


class CutUrlAdmin(admin.ModelAdmin):
	list_display = ['url_path', 'url_cutted']
	readonly_fields = ['url_cutted']
	list_per_page = 50


	class Meta:
		model = CutUrl


admin.site.register(CutUrl, CutUrlAdmin)