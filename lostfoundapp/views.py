from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # For displaying messages
from .models import LostItem
from .forms import LostItemForm

def home(request):
    return render(request, "lostfoundapp/home.html")  # Ensure home.html is inside templates/lostfoundapp/

def index(request):
    # Get the condition filter from GET parameters, default to 'Lost'
    condition_filter = request.GET.get('condition', 'Lost')
    
    # Fetch all items based on condition ('Lost' or 'Found')
    items = LostItem.objects.filter(condition=condition_filter).order_by('-created_at')  # Corrected from 'date_reported'
    
    return render(request, 'lostfoundapp/index.html', {'items': items, 'condition_filter': condition_filter})

def add_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)  # Accepting file input
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully.')  # Success message
            return redirect('index')  # Redirect to the homepage after successful form submission
        else:
            messages.error(request, 'There was an error with your submission.')  # Error message
    else:
        form = LostItemForm()
    
    return render(request, 'lostfoundapp/add_lost_item.html', {'form': form})

def claim_item(request, item_id):
    # Get the lost item or return a 404 if not found
    item = get_object_or_404(LostItem, id=item_id)
    
    if item.claimed:
        messages.info(request, 'This item has already been claimed.')  # Inform user that it's already claimed
        return redirect('index')  # Redirect to the homepage if already claimed
    
    if request.method == 'POST':
        # Mark the item as claimed
        item.claimed = True
        item.save()
        messages.success(request, 'You have successfully claimed the item.')  # Success message
        return redirect('index')  # Redirect back to the index page after successful claim
    
    return render(request, 'lostfoundapp/claim_item.html', {'item': item})
