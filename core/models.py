from django.db import models
from django.utils import timezone
from ordered_model.models import OrderedModel
# Create your models here.
class Queue(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

def generate_token():
    patients_today = Patient.objects.filter(time__date = timezone.now().date())
    last_patient = patients_today.last()
    if last_patient:
        return last_patient.token + 1
    else:
        return 1

class Patient(OrderedModel):
    number = models.CharField(max_length=20)
    time = models.DateTimeField(default=timezone.now)
    token = models.IntegerField(default=generate_token)
    q = models.ForeignKey(Queue,models.CASCADE,'patients')
    order_with_respect_to = 'q'
    class Meta:
        unique_together = ('time','token')
    
    def __str__(self):
        return "{} | {} | {}".format(self.token, self.number, self.q.name)

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    greeting = models.TextField(blank=True,null=True)
    number = models.CharField(max_length=20, unique=True)

