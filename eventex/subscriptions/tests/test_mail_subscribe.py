from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos',
                    cpf='12345678901',
                    email="h@gmail.com",
                    phone="(61)96161-6161")
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'fabriciobrasilemail@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['fabriciobrasilemail@gmail.com', 'h@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        infos = ('Henrique Bastos',
                 '12345678901',
                 'h@gmail.com',
                 '(61)96161-6161',)
        for info in infos:
            with self.subTest():
                self.assertIn(info, self.email.body)
