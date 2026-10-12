from django.test import TestCase
from django.urls import reverse

from .models import Game


class CatalogViewsTests(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/home.html')

    def test_game_list_page(self):
        response = self.client.get(reverse('game_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/game_list.html')

    def test_game_is_displayed(self):
        Game.objects.create(
            title='Minecraft',
            genre='Sandbox',
            release_year=2011,
            description='Open-world game'
        )

        response = self.client.get(reverse('game_list'))

        self.assertContains(response, 'Minecraft')
        self.assertContains(response, 'Sandbox')


class GameModelTests(TestCase):

    def test_game_string_representation(self):
        game = Game(
            title='Minecraft',
            genre='Sandbox'
        )

        self.assertEqual(str(game), 'Minecraft')