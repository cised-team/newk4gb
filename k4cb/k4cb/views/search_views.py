from django.views.generic import ListView
from ..models import TopicClass

class SearchTopicClassListView(ListView):
    template_name = 'search_topic_class.html'
    model = TopicClass
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super(SearchTopicClassListView, self).get_queryset()
        self.topic_id = self.request.GET.get('topic_id')
        try: self.topic_id = int(self.topic_id)
        except: pass
        self.search = self.request.GET.get('search')
        if self.topic_id:
            queryset = queryset.filter(topic__id=self.topic_id)
        if self.search:
            queryset = queryset.filter(name__contains=self.search)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(SearchTopicClassListView, self)\
                .get_context_data(**kwargs)
        context.update({'topic_id': self.topic_id,
                        'search': self.search})
        return context
