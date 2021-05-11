from django.test import TestCase
from .models import Editor
# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Macrine= Editor(first_name = 'Macrine', last_name ='Alice', email ='alicakrynne@outlook.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Macrine,Editor))
    
