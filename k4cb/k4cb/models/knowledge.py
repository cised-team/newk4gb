from django.db import models
from django.contrib.auth.models import User

from .skill import Skill
from .topic import Topic

class Knowledge(models.Model):
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    skill = models.ForeignKey(Skill)
    score = models.IntegerField()
    
    def __unicode__(self):
        return "%s:%s:%s:%s"%(self.user, self.topic, self.skill, self.score)
    
    class Meta:
        app_label = "k4cb"
