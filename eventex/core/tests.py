from django.test import TestCase

# o TestCase é uma classe do Django que, por sua vez
# já estende o TestCase do unittest
class HomeTest(TestCase):
    def setUp(self):
        "Access the route '/' with GET method and save it in a class response attribute"
        self.response = self.client.get('/')        

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')
        