from ..models import Topic

def base_processor(request):
    topics = Topic.objects.all()
    return {'topics': topics}