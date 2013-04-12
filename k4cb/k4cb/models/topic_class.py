from django.db import models

from k4cb.models.topic import Topic

class TopicClass(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=250)
    html_content = models.TextField()
    #the dificulty is calculated bye the avg of the relevance*skill.score_min
    dificulty = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = "k4cb"
        verbose_name_plural = "topic classes"
