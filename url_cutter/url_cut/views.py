from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import CutUrlForm
from .models import CutUrl
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class CutUrlCreateView(SuccessMessageMixin, CreateView):
	model = CutUrl
	template_name = "form.html"
	form_class = CutUrlForm
	success_message = "%(full)s"

	def get_success_url(self):
		return reverse("base_html")

	def get_success_message(self, cleaned_data):
		return self.success_message % dict(
			cleaned_data,
			url_cutted=self.object.url_cutted,
			full=self.request.build_absolute_uri(reverse("cutted", kwargs={'link':self.object.url_cutted}))
		)


def redirect_by_short_url(request, link):
	object_url = get_object_or_404(CutUrl, url_cutted=link).url_path
	return redirect(object_url)


