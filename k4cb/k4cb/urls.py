from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views.profile import ProfileView
from .views.topic_view import TopicView
from .views.search_views import SearchTopicClassListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'k4cb.views.home', name='home'),
    # url(r'^k4cb/', include('k4cb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^profile/', ProfileView.as_view()),
    url(r'^contact_us/',
        TemplateView.as_view(template_name="contact_us.html")),
    url(r'^faq/',
        TemplateView.as_view(template_name="faq.html")),
    url(r'^topic/(?P<pk>\d+)/', TopicView.as_view()),
    url(r'^topic_class/search/', SearchTopicClassListView.as_view()),
    #login logout
    url(r'^accounts/login/$','django.contrib.auth.views.login', 
        {'template_name': 'signin.html'}),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout_then_login'),
)
