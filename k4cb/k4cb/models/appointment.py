from django.db import models
from django.contrib.auth.models import User

from .topic_class import TopicClass
from .skill import TopicClassSkill

APPOINMENT_ACTIVE = 0
APPOINMENT_DONE = 1
APPOINMENT_CANCELED = 2
APPOINMENT_EXPIRED = 3

APPOINMENT_STATUS = ((APPOINMENT_ACTIVE, "Active"),
                     (APPOINMENT_DONE, "Done"),
                     (APPOINMENT_CANCELED, "Canceled"),
                     (APPOINMENT_EXPIRED, "Expired"))

class Appointment(models.Model):
    teacher = models.ForeignKey(User, related_name="appointment_teacher")
    students = models.ManyToManyField(User, related_name="appointment_user")
    topic_class = models.ForeignKey(TopicClass)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField(choices=APPOINMENT_STATUS)
    
    def __unicode__(self):
        return "%s (%s:%s)"%(self.topic_class, self.start_time, self.end_time)
    
    class Meta:
        app_label = "k4cb"

class AppointmentResult(models.Model):
    student_ok = models.BooleanField(default=False)
    teacher_ok = models.BooleanField(default=False)
    teacher_evaluation = models.IntegerField()
    
    def __unicode__(self):
        return "%s (%s:%s)"%(self.topic_class, self.start_time, self.end_time)
    
    class Meta:
        app_label = "k4cb"

class StudentEvaluation(models.Model):
    appointment_result = models.ForeignKey(AppointmentResult)
    student = models.ForeignKey(User)
    class_skill = models.ForeignKey(TopicClassSkill)
    evaluation = models.IntegerField()
    
    def __unicode__(self):
        return "%s:%s:%s"%(self.student, self.class_skill, self.evaluation)
    
    class Meta:
        app_label = "k4cb"
