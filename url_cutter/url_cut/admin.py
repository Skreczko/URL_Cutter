from django.contrib import admin
from .models import CutUrl


class CutUrlAdmin(admin.ModelAdmin):
	list_display = ['urlpath', 'urlcutted']
	readonly_fields = ['urlcutted']
	list_per_page = 50


	class Meta:
		model = CutUrl


admin.site.register(CutUrl, CutUrlAdmin)