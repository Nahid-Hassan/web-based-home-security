from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'objrecog/home.html'


class AboutView(TemplateView):
    template_name = 'objrecog/about.html'
