from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Dieison Borges', cpf='09196162678',
                    email='dieisoncomix@gmail.com', phone='41 3149-4222')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscriptionemail_to(self):
        expect = ['contato@eventex.com.br', 'dieisoncomix@gmail.com']

    def test_subscription_email_body(self):

        contents = ['Dieison Borges',
                    '09196162678',
                    'dieisoncomix@gmail.com',
                    '41 3149-4222',
                    ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

