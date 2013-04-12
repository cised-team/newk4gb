from django.db import models

from k4cb.models.topic import TopicCategory
from k4cb.models.topic_class import TopicClass

class Skill(models.Model):
    topic = models.ForeignKey(TopicCategory)
    name = models.CharField(max_length=100);
    relevance = models.IntegerField() # 1..10
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = "k4cb"

class TopicClassSkill(models.Model):
    topic_class = models.ForeignKey(TopicClass)
    skill = models.ForeignKey(Skill)
    score_min = models.IntegerField()
    score_max = models.IntegerField()
    
    def __unicode__(self):
        return "%s:%s (%s:%s)"%(self.topic_class, self.skill,
                                self.score_min, self.score_max)
    
    class Meta:
        app_label = "k4cb"
