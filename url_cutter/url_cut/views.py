from django.shortcuts import render

from .forms import CutUrlForm
from .models import CutUrl
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class CutUrlCreateView(SuccessMessageMixin, CreateView):
	model = CutUrl
	template_name = 'form.html'
	form_class = CutUrlForm
	success_message = "%(url_cutted)s is your link"

class CutUrlDetailView(DetailView):
	model = CutUrl

	def get(self, request, *args, **kwargs):
		pass
