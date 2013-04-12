from django.views.generic import DetailView

from..models import Topic

class TopicView(DetailView):
    template_name = 'topic.html'
    model = Topic