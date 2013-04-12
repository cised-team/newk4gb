from django.db import models

class TopicCategory(models.Model):
    name = models.CharField(max_length=100);
    description = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = "k4cb"
        verbose_name_plural = "topic categories"

class Topic(models.Model):
    category = models.ForeignKey(TopicCategory)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = "k4cb"
