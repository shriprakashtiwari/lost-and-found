from django.db import models
from django.utils import timezone

class LostItem(models.Model):
    CONDITION_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_lost = models.DateField(null=True, blank=True)  # Can be null for "Found" items
    found_date = models.DateField(null=True, blank=True)  # Date when the item was found (optional for lost items)
    contact_info = models.CharField(max_length=10)  # Limited to 10 digits
    condition = models.CharField(max_length=5, choices=CONDITION_CHOICES, default='Lost')  # New condition field
    claimed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)  # Optional image field

    def __str__(self):
        return self.name
