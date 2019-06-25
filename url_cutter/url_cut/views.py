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
			urlcutted=self.object.urlcutted,
			full=self.request.build_absolute_uri(reverse("cutted", kwargs={'link':self.object.urlcutted}))
		)


def redirect_by_short_url(request, link):
	objecturl = get_object_or_404(CutUrl, urlcutted=link).urlpath
	return redirect(objecturl)


