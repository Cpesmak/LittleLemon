from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Pizza", price=12.99, inventory=20)
        self.item2 = Menu.objects.create(title="Burger", price=8.50, inventory=50)

    def test_get_all_menu_items(self):
        menu_items = Menu.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        expected_data = [
            {
                'id': self.item1.id,  # Ensure this matches serializer output
                'title': self.item1.title,
                'price': str(self.item1.price),  # Convert to string if serializer does
                'inventory': self.item1.inventory
            },
            {
                'id': self.item2.id,
                'title': self.item2.title,
                'price': str(self.item2.price),
                'inventory': self.item2.inventory
            }
        ]

        self.assertEqual(serializer, expected_data)