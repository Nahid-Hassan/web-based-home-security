from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'objrecog/home.html'


class AboutView(TemplateView):
    template_name = 'objrecog/about.html'


class LiveRecognitionView(TemplateView):
    template_name = 'objrecog/liverecognition.html'


class RecordsView(TemplateView):
    template_name = 'objrecog/records.html'
