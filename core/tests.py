from django.test import TestCase
from freezegun import freeze_time
from .models import Queue, Patient
from django.utils import timezone
# Create your tests here.
class PatientTests(TestCase):
    def setUp(self):
        Queue.objects.create(name='Common Q')
    
    def test_add_patients(self):
        q = Queue.objects.first()
        for n in range(10):
            Patient.objects.create(number='99449418342', q=q)
        patients = Patient.objects.all()
        self.assertEqual(10,len(patients))

        with freeze_time(timezone.now()+timezone.timedelta(days=1)):
            for n in range(10):
                Patient.objects.create(number='99449418342', q=q)
        patients = Patient.objects.all()
        self.assertEqual([patient.token for patient in patients], [i+1 for i in range(10)]*2)