from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name='main_app/index.html'

class AboutView(TemplateView):
    template_name='main_app/about.html'


