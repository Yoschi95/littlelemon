from django.test import TestCase
from restaurant.models import Menu, Booking
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=150, inventory=50)
        Menu.objects.create(title="Burger", price=120, inventory=75)

    def test_getAll(self):
        # Next, add another test_getall() instance method to retrieve all the Menu objects added for the test purpose. 
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

        # The retrieved objects must serialized, so make sure the method runs assertions to check if the serialized data equals the response.
        self.assertEqual(response.data[0]['title'], 'IceCream')
        self.assertEqual(response.data[1]['title'], 'Pizza')
        self.assertEqual(response.data[2]['title'], 'Burger')

        self.assertEqual(response.data[0]['price'], '80.00')
        self.assertEqual(response.data[1]['price'], '150.00')
        self.assertEqual(response.data[2]['price'], '120.00')

        self.assertEqual(response.data[0]['inventory'], 100)
        self.assertEqual(response.data[1]['inventory'], 50)
        self.assertEqual(response.data[2]['inventory'], 75)