from django.test import TestCase
from freezegun import freeze_time
from .models import Queue, Patient, Hospital
from django.utils import timezone
from django.shortcuts import reverse
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

class GreetingViewTest(TestCase):
    def setUp(self):
        Hospital.objects.create(name="Aarthy Eye Hospital",number="9944941964")
    
    def test_greeting(self):
        r = self.client.get(reverse('greet'),{'hospital_number':"9944941964"})
        self.assertContains(r,'Welcome')