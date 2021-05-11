from django.test import TestCase
from .models import Editor,Article,tags
# Create your tests here.

class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.macrine= Editor(first_name = 'Macrine', last_name ='Alice', email ='alicakrynne@outlook.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.macrine,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.macrine.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
    
