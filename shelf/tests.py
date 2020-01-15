from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Shelf

class ShelfTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'charlie',
            email = 'cg@cg.com',
            password = '12345678'
        )
        self.Shelf = Shelf.objects.create(
            title = 'the lion king',
            author = self.user,
            description = 'some description about a movie about lions',
            img = 'fakeimg.jpg'
        )

    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_status(self):
        url = reverse('detail', args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_template(self):
        url = reverse('detail', args='1')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_shelf_content(self):
        self.assertEqual(f'{self.Shelf.title}', 'the lion king')
        self.assertEqual(f'{self.Shelf.author}', 'charlie')
        self.assertEqual(f'{self.Shelf.description}', 'some description about a movie about lions',)
        self.assertEqual(f'{self.Shelf.img}', 'fakeimg.jpg')