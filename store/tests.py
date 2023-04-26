from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse
from .models import *

class MyViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.my_model = MyModel.objects.create(name='test')
    
    def test_my_view(self):
        url = reverse('my_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My View')
        
    def tearDown(self):
        self.my_model.delete()
