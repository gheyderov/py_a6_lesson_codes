from core.models import Contact
from django.test import TestCase


class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = {
            'name' : 'John',
            'email' : 'john@google.com',
            'subject' : 'Test',
            'message' : 'message'
        }
        cls.contact = Contact.objects.create(**cls.data)

    def test_create_model(self):
        contact = Contact.objects.first()
        self.assertEqual(self.contact, contact)
    
    @classmethod
    def tearDownClass(cls) -> None:
        pass