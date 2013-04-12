from django.views.generic import TemplateView
from django.contrib.auth.models import User

from ..models import Knowledge

class ProfileView(TemplateView):
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        #user=self.request.user
        user = User.objects.get(username='admin') #prototype
        knowledge_list = Knowledge.objects.filter(user=user).all()
        return {
            'params': kwargs,
            'knowledge_list': knowledge_list,
        }
