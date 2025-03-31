from django.test import TestCase
from .models import LostItem
from django.urls import reverse

class LostItemModelTest(TestCase):
    def test_lost_item_creation(self):
        # Create a LostItem instance with condition "Lost"
        lost_item = LostItem.objects.create(
            name="Lost Wallet",
            description="A black wallet with ID cards",
            location="Park",
            date_lost="2025-03-31",
            contact_info="123-456-7890",
            condition="Lost"  # Ensure condition is set to 'Lost'
        )
        
        # Check if the LostItem is created successfully
        self.assertEqual(lost_item.name, "Lost Wallet")
        self.assertEqual(lost_item.description, "A black wallet with ID cards")
        self.assertEqual(lost_item.location, "Park")
        self.assertEqual(lost_item.date_lost, "2025-03-31")
        self.assertEqual(lost_item.contact_info, "123-456-7890")
        self.assertEqual(lost_item.condition, "Lost")  # Check the condition is set to 'Lost'
        self.assertFalse(lost_item.claimed)  # Ensure claimed is False by default

class LostItemViewTest(TestCase):
    def test_index_view(self):
        # Create Lost and Found items for testing
        LostItem.objects.create(
            name="Lost Wallet",
            description="A black wallet with ID cards",
            location="Park",
            date_lost="2025-03-31",
            contact_info="123-456-7890",
            condition="Lost"
        )
        LostItem.objects.create(
            name="Found Phone",
            description="A black phone",
            location="Mall",
            date_lost="2025-03-31",
            contact_info="987-654-3210",
            condition="Found"
        )

        # Test for Lost items
        response = self.client.get(reverse('index') + "?condition=Lost")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lost Wallet")
        self.assertNotContains(response, "Found Phone")

        # Test for Found items
        response = self.client.get(reverse('index') + "?condition=Found")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Found Phone")
        self.assertNotContains(response, "Lost Wallet")
        
    def test_add_item_view(self):
        # Make a GET request to the add item view (for Lost or Found items)
        response = self.client.get(reverse('add_item'))
        
        # Check if the response status code is 200 (successful)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_lost_item.html')  # Assuming 'add_lost_item.html' template is used

    def test_claim_item_view(self):
        # Create a LostItem instance
        lost_item = LostItem.objects.create(
            name="Lost Wallet",
            description="A black wallet with ID cards",
            location="Park",
            date_lost="2025-03-31",
            contact_info="123-456-7890",
            condition="Lost"  # Specify condition
        )
        
        # Make a GET request to claim the item (use the item's ID)
        response = self.client.get(reverse('claim_item', args=[lost_item.id]))
        
        # Check if the response status code is 302 (redirected)
        self.assertEqual(response.status_code, 302)
        
        # Check if the item has been marked as claimed
        lost_item.refresh_from_db()
        self.assertTrue(lost_item.claimed)
