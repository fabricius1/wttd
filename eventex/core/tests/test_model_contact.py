from django.test import TestCase
from django.core.exceptions import ValidationError

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic',)

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net',)
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='21-996186180',)
        self.assertTrue(Contact.objects.exists())

    def test_kind_field_choices(self):
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net',)
        self.assertEqual('henrique@bastos.net', str(contact))
