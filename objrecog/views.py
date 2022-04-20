from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from objrecog.camera	import VideoCamera
from .models import RecordListDB


class HomeView(TemplateView):
    template_name = 'objrecog/home.html'


class AboutView(TemplateView):
    template_name = 'objrecog/about.html'


class LiveRecognitionView(TemplateView):
    template_name = 'objrecog/liverecognition.html'


class RecordsView(ListView):
    model = RecordListDB
    
    paginate_by = 10
    ordering = ['-record_datetime']

    template_name = 'objrecog/records.html'
    context_object_name = 'record_list'



# ------------ Live CC Start --------------------------
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def stream(request):
	return StreamingHttpResponse(gen(VideoCamera()),
                              content_type='multipart/x-mixed-replace; boundary=frame')

# ------------ Live CC End --------------------------