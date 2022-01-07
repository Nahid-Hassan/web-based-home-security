from django.urls import path

from .views import HomeView, AboutView, LiveRecognitionView, RecordsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('liverecog/', LiveRecognitionView.as_view(), name='liverecog'),
    path('records/', RecordsView.as_view(), name='records'),
]
