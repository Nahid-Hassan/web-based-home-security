from django.views.generic import TemplateView
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from objrecog.camera	import VideoCamera



class HomeView(TemplateView):
    template_name = 'objrecog/home.html'


class AboutView(TemplateView):
    template_name = 'objrecog/about.html'


class LiveRecognitionView(TemplateView):
    template_name = 'objrecog/liverecognition.html'


class RecordsView(TemplateView):
    template_name = 'objrecog/records.html'


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
