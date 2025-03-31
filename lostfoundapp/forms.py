from django import forms
from .models import LostItem

class LostItemForm(forms.ModelForm):
    # Optional image upload field (file is not required)
    image = forms.ImageField(required=False)

    # Adding a condition field explicitly to match the model
    condition = forms.ChoiceField(choices=LostItem.CONDITION_CHOICES, required=True)

    class Meta:
        model = LostItem
        # Including all the relevant fields from the model
        fields = ['name', 'description', 'location', 'contact_info', 'condition', 'date_lost', 'found_date', 'image']

    def clean(self):
        # Call the base clean method to gather cleaned data
        cleaned_data = super().clean()

        # Retrieve the 'condition', 'date_lost', and 'found_date' from the cleaned data
        condition = cleaned_data.get('condition')
        date_lost = cleaned_data.get('date_lost')
        found_date = cleaned_data.get('found_date')

        # Ensure that for "Found" items, found_date is provided
        if condition == 'Found' and not found_date:
            self.add_error('found_date', 'Found date is required for Found items.')

        # Ensure that for "Lost" items, date_lost is provided
        if condition == 'Lost' and not date_lost:
            self.add_error('date_lost', 'Date lost is required for Lost items.')

        return cleaned_data
